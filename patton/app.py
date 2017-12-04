from sanic import Sanic
from sanic.response import text, json
from sanic.exceptions import NotFound

from . import config
from . import __version__

app = Sanic(__name__)
app.config.from_object(config)


@app.route('/')
async def hello_world(*args, **kwargs):
    return text(f'Welcome to patton! {__version__}')


@app.route('/pkg/<name>/<version>')
async def package_search(request, name, version, *args, **kwargs):
    with session_ctx() as session:
        query = session.query(VulnProduct).first()
    return json(query)


@app.exception(NotFound)
async def ignore_404s(request, exception):
    return text("", status=404)
