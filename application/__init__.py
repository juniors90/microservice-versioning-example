import os

from application.core.database import db

import connexion

from flask import jsonify

from flask_cors import CORS, cross_origin

from flask_marshmallow import Marshmallow

from flask_migrate import Migrate

from config import app_config

basedir = os.path.abspath(".")

ma = Marshmallow()
migrate = Migrate()
cors = CORS()


def create_app(config_name):
    server_args = {"instance_relative_config": True}
    connex_app = connexion.App(
        __name__, specification_dir=basedir, server_args=server_args
    )
    # register api endpoints
    connex_app.add_api(
        os.path.join(basedir, "application", "api", "v1", "swagger.yml")
    )
    connex_app.add_api(
        os.path.join(basedir, "application", "api", "v2", "swagger.yml")
    )
    app = connex_app.app

    app.config.from_object(app_config[config_name])

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(
        app, resources={r"/api/*": {"origins": os.getenv("APIREST_ORIGINS")}}
    )

    @app.route("/healthcheck", methods=["GET"])
    @cross_origin()
    def healthcheck():
        return jsonify({"msg": "ok"}), 200

    return app
