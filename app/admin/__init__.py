from flask import Blueprint, g

admin = Blueprint('admin', __name__, url_prefix='/<tlf>/admin')

@admin.url_defaults
def add_locale(endpoint, values):
    values.setdefault('tlf',g.tlf)

@admin.url_value_preprocessor
def pull_locale(endpoint, values):
    g.tlf = values.pop('tlf')

from . import views  # noqa
