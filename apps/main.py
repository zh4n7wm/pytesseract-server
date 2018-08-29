# -*- coding: utf-8 -*-
import importlib
import logging
import os

from flask import Flask, render_template

from apps.config import conf
from apps.view.api import api_bp
from apps.view.page import page_bp


def app_factory(config=None):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    app = Flask(
        __name__,
        static_folder=os.path.join(root_dir, 'static'),
        template_folder=os.path.join(root_dir, 'templates')
    )

    config_app(app, config or conf)
    config_logger(app)
    config_blueprints(app)
    config_extensions(app)
    config_request_hooks(app)
    configure_error_handlers(app)
    get_url_map(app)
    # pylint: disable=no-member
    app.logger.info("app started...")
    return app


def get_url_map(app):
    for url in app.url_map.iter_rules():
        print(url)


def config_logger(app, force=False):
    if force or not app.debug:
        stream_format = logging.Formatter(
            '%(asctime)s %(name)s %(levelname)s: %(message)s'
            '[in %(pathname)s:%(lineno)d]'
        )
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(stream_format)
        stream_handler.setLevel(logging.INFO)
        app.logger.addHandler(stream_handler)
        app.logger.setLevel(logging.INFO)


def config_app(app, config):
    if isinstance(config, str):
        config = importlib.import_module('apps.config.%s' % config)
    app.config.from_object(config)


def config_extensions(app):
    pass


def config_blueprints(app):
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(page_bp, url_prefix='/')


def config_request_hooks(app):
    @app.before_request
    def before_request_handler():
        pass


def configure_error_handlers(app):
    @app.errorhandler(403)
    # pylint: disable=unused-argument, unused-variable
    def forbidden_page(error):
        return render_template("error/access_forbidden.html"), 403

    @app.errorhandler(404)
    # pylint: disable=unused-argument, unused-variable
    def page_not_found(error):
        return render_template("error/page_not_found.html"), 404

    @app.errorhandler(405)
    # pylint: disable=unused-argument, unused-variable
    def method_not_allowed_page(error):  # pylint: disable=unused-argument
        return render_template("error/method_not_allowed.html"), 405

    @app.errorhandler(500)
    # pylint: disable=unused-argument, unused-variable
    def server_error_page(error):  # pylint: disable=unused-argument
        return render_template("error/server_error.html"), 500

    @app.errorhandler(410)
    # pylint: disable=unused-argument, unused-variable
    def page_gone(error):  # pylint: disable=unused-argument
        return render_template("error/page_gone.html"), 410
