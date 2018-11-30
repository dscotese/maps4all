from flask import Blueprint, g

descriptor = Blueprint('descriptor', __name__, url_prefix='/<tlf>/descriptor')

@descriptor.url_defaults
def add_locale(endpoint, values):
    values.setdefault('tlf',g.tlf)

@descriptor.url_value_preprocessor
def pull_locale(endpoint, values):
    g.tlf = values.pop('tlf')

from . import views  # noqa
