from sanic import Sanic
from sanic.response import text, json
from sanic.exceptions import NotFound

from .dal.database import session_ctx
from .dal.models import VulnProduct
from . import config

app = Sanic(__name__)
app.config.from_object(config)


@app.route('/')
async def hello_world(*args, **kwargs):
    return text('Hello, World!')


@app.route('/pkg/<name>/<version>')
async def package_search(request, name, version, *args, **kwargs):
    with session_ctx() as session:
        query = session.query(VulnProduct).first()
    return json(query)


@app.exception(NotFound)
async def ignore_404s(request, exception):
    return text("", status=404)
