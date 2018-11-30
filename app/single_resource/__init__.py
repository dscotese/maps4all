from flask import Blueprint, g

single_resource = Blueprint('single_resource', __name__, url_prefix='/<tlf>/single_resource')

@single_resource.url_defaults
def add_locale(endpoint, values):
    values.setdefault('tlf',g.tlf)

@single_resource.url_value_preprocessor
def pull_locale(endpoint, values):
    g.tlf = values.pop('tlf')

from . import views  # noqa
