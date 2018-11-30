from flask import Blueprint, g

account = Blueprint('account', __name__, url_prefix='/<tlf>/account')

@account.url_defaults
def add_locale(endpoint, values):
    values.setdefault('tlf',g.tlf)

@account.url_value_preprocessor
def pull_locale(endpoint, values):
    g.tlf = values.pop('tlf')

from . import views  # noqa
