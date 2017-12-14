from sanic import Sanic
from sanic.response import text, json
from sanic.exceptions import NotFound

from . import config
from . import __version__

from .dal.managers import batch_query_cpe, query_cpe

app = Sanic(__name__)
app.config.from_object(config)


@app.route('/', methods=['GET'])
async def hello_world(*args, **kwargs):
    return text(f'Welcome to patton! {__version__}')


@app.route('/<package>/<version>', methods=['GET'])
def package_search(request, package, version, *args, **kwargs):
    return json(query_cpe(package, version))


@app.route('/batch/', methods=['POST'])
def batch_package_search(request, *args, **kwargs):
    return json(batch_query_cpe(request.json))


@app.exception(NotFound)
async def ignore_404s(request, exception):
    return text("", status=404)
