import sys
from functools import wraps

from flask import abort
from flask.ext.login import current_user
from .models import Permission
from .utils import tlf
from flask import Request


def permission_required(permission):
    """Restrict a view to users with the given permission."""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def admin_required(f):
    return permission_required(Permission.ADMINISTER)(f)


def handle_locale(f):
    def hl(*args, **kwargs):
        path = flask.request.path
        print("Found the path", path)
        sys.stdout.flush()
    print ("Locale decorator added.")
    sys.stdout.flush()
