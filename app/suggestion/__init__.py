from flask import Blueprint, g

suggestion = Blueprint('suggestion', __name__, url_prefix='/<tlf>/suggestion')

@suggestion.url_defaults
def add_locale(endpoint, values):
    values.setdefault('tlf',g.tlf)

@suggestion.url_value_preprocessor
def pull_locale(endpoint, values):
    g.tlf = values.pop('tlf')

from . import views  # noqa
