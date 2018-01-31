import aiopg

from sanic import Sanic

from patton_server.service.end_points_api_v1 import *
from patton_server.service.end_points_api_v2 import *
from patton_server.service.end_points_home import *


def make_app(config_file: dict) -> Sanic:
    class _fake:
        pass

    _A = _fake()
    _A.__dict__.update(config_file)

    app = Sanic(__name__)
    app.config.from_object(_A)
    app.blueprint(end_points_home)
    app.blueprint(end_points_api_v1)
    app.blueprint(end_points_api_v2)

    @app.listener('before_server_start')
    async def register_db(app, loop):
        app.pool = await aiopg.create_pool(dsn=app.config["PATTON_DB_URL"],
                                           loop=loop,
                                           maxsize=100)

    return app


__all__ = ("make_app", )