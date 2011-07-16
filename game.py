from flask import session, request, redirect, url_for, Flask, render_template, flash

from users import User
from access import *

app = Flask(__name__)
app.config.from_object('settings')

@app.route('/')
@login_required
def index():
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if not session.get("next"):
        session["next"] = request.args.get("next","/")
    if request.method == 'POST':
        form = request.form
        auth = check_auth(form['username'],form['password'])
        if auth:
            session["user"], session["is_admin"] = auth
            return redirect(session["next"])
        else:
            flash("Wrong Password")
    return render_template("login.html")


@app.route('/logout')
def logout():
    session.pop("user", None)
    session.pop("is_admin", None)
    return redirect("/")

if __name__ == '__main__':
    app.run()

