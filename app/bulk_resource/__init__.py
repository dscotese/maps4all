from flask import Blueprint, g

bulk_resource = Blueprint('bulk_resource', __name__, url_prefix='/<tlf>/bulk-resource')

@bulk_resource.url_defaults
def add_locale(endpoint, values):
    values.setdefault('tlf',g.tlf)

@bulk_resource.url_value_preprocessor
def pull_locale(endpoint, values):
    g.tlf = values.pop('tlf')

from . import views  # noqa
