from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base
# from .database import Base, engine

from .common import fields
from .product.models import Prod, ProdReference, Cpe23  # noqa
from .common.fields import __CpeNorm__  # noqa
from .vulnerability.models import Vuln  # noqa


class VulnProduct(Base):
    """
    many to many relation between product and vulnerabilities.
    """
    __tablename__ = 'vuln_product'
    id = Column(String, primary_key=True, default=fields.uuid)
    vuln_id = Column(String, ForeignKey('vuln.id'))
    prod_id = Column(String, ForeignKey('prod.id'))

    vuln = relationship('Vuln', back_populates='prods')
    prod = relationship('Prod', back_populates='vulns')

    def preload_fk_map(root, existing_cpes: set):
        # Use this way to ensure that there's not duplicates
        d = set(fields.cpe_norm('vuln_product', prod.text)
                for prod in root.iter('{*}product'))

        return ((x, None, None) for x in d.difference(existing_cpes))

    def loader_map(root):
        return (
            (
                fields.uuid(),
                prod.getparent().getparent().attrib['id'],
                fields.cpe_norm('vuln_product', prod.text),
            )
            for prod in root.iter('{*}product')
        )

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'vuln_id': self.vuln_id,
            'prod_id': self.prod_id,
            'vuln': self.vuln,
            'prod': self.prod,
        }


# Everything else...
# Base.metadata.reflect(bind=engine)
