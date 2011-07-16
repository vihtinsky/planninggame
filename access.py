from functools import wraps
import hashlib
from users import User
from flask import session, redirect, url_for, request

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user") is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


def check_auth(username, password):
    ph = hashlib.md5(password).hexdigest()
    user = User(username, ph)
    return user.login()

