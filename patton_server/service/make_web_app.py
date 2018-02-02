import aiopg

from sanic import Sanic
from sanic_cors import CORS

from patton_server.service.end_points_api_v1 import *
from patton_server.service.end_points_api_v2 import *
from patton_server.service.end_points_home import *


def make_app(config_file: dict) -> Sanic:
    class _fake:
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k.upper(), v)

    _A = _fake(**config_file)

    app = Sanic(__name__)
    app.config.from_object(_A)
    app.blueprint(end_points_home)
    app.blueprint(end_points_api_v1)
    app.blueprint(end_points_api_v2)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.listener('before_server_start')
    async def register_db(app, loop):
        app.pool = await aiopg.create_pool(dsn=app.config["PATTON_DB_URL"],
                                           loop=loop,
                                           maxsize=100)

    return app


__all__ = ("make_app", )