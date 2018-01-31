from uuid import uuid4
from typing import List, Any

from sqlalchemy.sql.expression import insert
from sqlalchemy import Column, String

# from patton_server.dal.database import engine, Base
from patton_server.dal.database import Base

wild = '*'
fill = ''


def is_empty(part: str) -> bool:
    return part in ['_', '*', '']


def is_meaningful(arr: list) -> bool:
    if len(arr) > 1:
        for item in arr[1:]:
            if not is_empty(item):
                return True
    return False


def _rfill(arr: List, padding: int, value: Any):
    """ Extend a list to a size filling with a fixed value """
    arr.extend([value] * (padding - len(arr)))


def _safe_split(string: str) -> list:
    return string.replace('\:', '%3A').split(':')


def _cpe22_to_wfn(value: str) -> List[Any]:
    """ Digest cpe22 to well formed names """
    vals = _safe_split(value)
    _rfill(vals, 7, fill)

    # INFO: clean format `cpe:/{part}:{rest ...}` to a useful content
    vals[1] = vals[1].split('/')[1]

    # INFO: cpe23 to cpe22 sometimes is model as:
    # cpe:/o:microsoft:windows_vista:6.0:sp1:~-~home_premium~-~x64~-
    # so we check that the hack exists and has 6 entries
    if not is_empty(vals[6]):

        other = vals.pop()
        hack_mode = other.split('~')

        if is_meaningful(hack_mode):
            _rfill(hack_mode, 6, fill)
            vals.extend(hack_mode)
        else:
            vals.append(other)

    _rfill(vals, 12, fill)

    return vals[1:]


def _cpe23_to_wfn(value: str) -> List[Any]:
    """ Digest cpe23 to well formed names """
    vals = _safe_split(value)
    _rfill(vals, 13, wild)

    return vals[2:]


def _wfn_to_cpe23(
    part: str,
    vendor: str,
    product: str,
    version: str,
    update: str,
    edition: str,
    language: str,
    sw_edition: str,
    target_sw: str,
    target_hw: str,
    other: str
) -> str:
    optionals = f':{edition}:{language}:{sw_edition}:{target_sw}:{target_hw}:{other}'  # noqa
    return f'cpe:2.3:{part}:{vendor}:{product}:{version}:{update}{optionals}'


def _wfn_to_cpe22(
    part: str,
    vendor: str,
    product: str,
    version: str,
    update: str,
    edition: str,
    language: str,
    sw_edition: str,
    target_sw: str,
    target_hw: str,
    other: str
) -> str:
    if is_meaningful([edition, language, sw_edition, target_sw, target_hw, other]):
        optionals = f':{edition}~{language}~{sw_edition}~{target_sw}~{target_hw}~{other}'  # noqa
    else:
        optionals = f':{edition}'

    return f'cpe:/{part}:{vendor}:{product}:{version}:{update}{optionals}'.rstrip(':*')


class __CpeNorm__(Base):
    __tablename__ = 'cpe_norm'
    id = Column(String, primary_key=True)
    transformation = Column(String)
    origin = Column(String)
    input = Column(String)
    output = Column(String)


class cpe(object):
    @staticmethod
    def up(cpe: str) -> str:
        return _wfn_to_cpe23(*[i if i != fill else wild for i in _cpe22_to_wfn(cpe)])

    @staticmethod
    def down(cpe: str) -> str:
        return _wfn_to_cpe22(*[i if i != wild else fill for i in _cpe23_to_wfn(cpe)])

    @staticmethod
    def same22(cpe: str) -> str:
        return _wfn_to_cpe22(*_cpe22_to_wfn(cpe))

    @staticmethod
    def same23(cpe: str) -> str:
        return _wfn_to_cpe23(*_cpe23_to_wfn(cpe))


def _store_transform(transformation: str,
                     origin: str,
                     input: str,
                     output: str) -> str:
    if input != output:
        # engine.execute(insert(__CpeNorm__), {
        #     'id': uuid(),
        #     'transformation': transformation,
        #     'origin': origin,
        #     'input': input,
        #     'output': output
        # })
        pass
    return output


def normalize_cpe22(origin: str, value: str) -> str:
    return _store_transform(
        'normalize_cpe22', origin, value,
        cpe.same22(value)
    )


def normalize_cpe23(origin: str, value: str) -> str:
    return _store_transform(
        'normalize_cpe23', origin, value,
        cpe.same23(value)
    )


def cpe22_to_cpe23(origin: str, value: str) -> str:
    return _store_transform(
        'cpe22_to_cpe23', origin, value,
        cpe.up(value)
    )


def cpe23_to_cpe22(origin: str, value: str) -> str:
    return _store_transform(
        'cpe23_to_cpe22', origin, value,
        cpe.down(value)
    )


def cpe_norm(origin: str, value: str) -> str:
    return normalize_cpe23(origin, value) \
        if value.startswith('cpe:2.3') else normalize_cpe22(origin, value)


def uuid() -> str:
    return uuid4().hex
