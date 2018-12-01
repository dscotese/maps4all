from flask import Blueprint, g

main = Blueprint('main', __name__, url_prefix='/<tlf>')

@main.url_defaults
def add_locale(endpoint, values):
    values.setdefault('tlf',g.tlf)

@main.url_value_preprocessor
def pull_locale(endpoint, values):
    g.tlf = values.pop('tlf')

from . import views, errors  # noqa
