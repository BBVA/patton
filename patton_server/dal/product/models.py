from uuid import uuid4
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from patton_server.dal.database import Base
from . import fields


class Prod(Base):
    __tablename__ = 'prod'

    id = Column(String, primary_key=True)
    title = Column(String, index=True)
    title_lang = Column(String)

    references = relationship('ProdReference', backref='prod_reference')
    cpe23 = relationship('Cpe23', backref='cpe23')
    vulns = relationship('VulnProduct', back_populates='prod')

    def loader_map(root, existing_cpes: set):
        v = set(
            (
                fields.cpe_norm('prod', cpe.attrib['name']),
                cpe.find('{*}title').text,
                cpe.find('{*}title').attrib[
                    '{http://www.w3.org/XML/1998/namespace}lang']
            )
            for cpe in root.iter('{*}cpe-item')
        )

        return set(x for x in v if x[0] not in existing_cpes)


class ProdReference(Base):
    __tablename__ = 'prod_reference'
    id = Column(String, primary_key=True, default=fields.uuid)
    prod_id = Column(String, ForeignKey('prod.id'))
    href = Column(String)
    description = Column(String)

    def loader_map(root):
        v = (
            (
                uuid4().hex,
                fields.cpe_norm('prod_reference',
                                ref.getparent().getparent().attrib['name']),
                ref.attrib['href'],
                ref.text
            )
            for ref in root.iter('{*}reference')
        )

        return v


class Cpe23(Base):
    __tablename__ = 'cpe23'
    id = Column(String, primary_key=True)
    prod_id = Column(String, ForeignKey('prod.id'))

    def loader_map(root):
        return (
            (
                fields.cpe_norm('cpe23', cpe23.attrib['name']),
                fields.cpe_norm('cpe23', cpe23.getparent().attrib['name']),
            )
            for cpe23 in root.iter('{*}cpe23-item')
        )
