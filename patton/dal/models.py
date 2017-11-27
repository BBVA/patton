from .database import Base, engine

from .product.models import Prod, ProdReference, Cpe23  # noqa
from .vulnerability.models import Vuln, VulnReference, VulnScore, VulnProduct  # noqa

# Everything else...
Base.metadata.reflect(bind=engine)
