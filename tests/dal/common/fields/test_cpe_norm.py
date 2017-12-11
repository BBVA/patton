from patton.dal.common.fields import cpe


def test_cpe_22():
    assert cpe.same22('cpe:/a:adobe:acrobat:7.1.4:*') == 'cpe:/a:adobe:acrobat:7.1.4'
    assert cpe.same22('cpe:/a:adobe:acrobat:7.1.4:other_part') == 'cpe:/a:adobe:acrobat:7.1.4:other_part'
    assert cpe.same22('cpe:/a:adobe:acrobat_dc:::~~classic~~~') == 'cpe:/a:adobe:acrobat_dc:::~~classic~~~'


def test_trasform_cpe22_to_cpe_23():
    assert cpe.up('cpe:/a:adobe:acrobat') == 'cpe:2.3:a:adobe:acrobat:*:*:*:*:*:*:*:*'
    assert cpe.up('cpe:/a:adobe:acrobat_dc:::~~classic~~~') == 'cpe:2.3:a:adobe:acrobat_dc:*:*:*:*:classic:*:*:*'


def test_trasform_cpe23_to_cpe_23():
    assert cpe.same23('cpe:2.3:a:adobe:acrobat:*:*:*:*:*:*:*:*') == 'cpe:2.3:a:adobe:acrobat:*:*:*:*:*:*:*:*'
    assert cpe.same23('cpe:2.3:a:adobe:acrobat_dc:*:*:*:*:classic:*:*:*') == 'cpe:2.3:a:adobe:acrobat_dc:*:*:*:*:classic:*:*:*'  # noqa


def test_trasform_cpe23_to_cpe_22():
    assert 'cpe:/a:adobe:acrobat' == cpe.down('cpe:2.3:a:adobe:acrobat:*:*:*:*:*:*:*:*')
    assert 'cpe:/a:adobe:acrobat_dc:::~~classic~~~' == cpe.down('cpe:2.3:a:adobe:acrobat_dc:*:*:*:*:classic:*:*:*')
