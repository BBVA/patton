from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from patton.dal.database import Base
from . import fields


class Prod(Base):
    __tablename__ = 'prod'
    id = Column(String, primary_key=True)
    title = Column(String)
    title_lang = Column(String)

    references = relationship('ProdReference', backref='prod_reference')
    cpe23 = relationship('Cpe23', backref='cpe23')
    vulns = relationship('VulnProduct', back_populates='prod')

    def loader_map(root):
        return [
            {
                'id': cpe.attrib['name'],
                'title': cpe.find('{*}title').text,
                'title_lang': cpe.find('{*}title').attrib['{http://www.w3.org/XML/1998/namespace}lang']
            }
            for cpe in root.iter('{*}cpe-item')
        ]

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'title_lang': self.title_lang,
            'references': self.references,
            'cpe23': self.cpe23,
        }


class ProdReference(Base):
    __tablename__ = 'prod_reference'
    id = Column(String, primary_key=True, default=fields.uuid)
    prod_id = Column(String, ForeignKey('prod.id'))
    href = Column(String)
    description = Column(String)

    def loader_map(root):
        return [
            {
                'id': fields.uuid(),
                'cpe': ref.getparent().getparent().attrib['name'],
                'href': ref.attrib['href'],
                'description': ref.text
            }
            for ref in root.iter('{*}reference')
        ]

    def to_dict(self):
        return {
            'href': self.href,
            'description': self.description,
        }


class Cpe23(Base):
    __tablename__ = 'cpe23'
    id = Column(String, primary_key=True)
    prod_id = Column(String, ForeignKey('prod.id'))

    def loader_map(root):
        return [
            {
                'id': cpe23.attrib['name'],
                'prod': cpe23.getparent().attrib['name'],
            }
            for cpe23 in root.iter('{*}cpe23-item')
        ]

    def to_dict(self) -> dict:
        return {
            'id': self.id
        }
