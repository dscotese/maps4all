from flask import Blueprint, g

contact = Blueprint('contact', __name__, url_prefix='/<tlf>/contact')

@contact.url_defaults
def add_locale(endpoint, values):
    values.setdefault('tlf',g.tlf)

@contact.url_value_preprocessor
def pull_locale(endpoint, values):
    g.tlf = values.pop('tlf')

from . import views
