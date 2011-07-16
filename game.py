from flask import session, request, redirect, url_for, Flask, render_template, flash

from users import User
from teams import Team
from access import *

app = Flask(__name__)
app.config.from_object('settings')

@app.route('/')
@login_required
def index():
    user = get_user()
    teams = user.get_teams()
    return render_template(
        "index.html",
        teams=teams
    )

@app.route('/team/<team>', methods=['GET', 'POST'])
@login_required
def team(team=None):
    team = Team(team)
    estimate = team.get_estimate()
    cards = app.config['CARDS']
    return render_template(
       "team.html", team=team, estimate=estimate,
       cards = cards
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    username = ""
    next = request.args.get("next",None)
    if next:
        session["next"] = next
    elif not session.get('next', False):
        session["next"] = '/'
    if request.method == 'POST':
        form = request.form
        username = form['username']
        auth = check_auth(form['username'],form['password'])
        if auth:
            session["user"], session["is_admin"] = auth
            next = session["next"]
            del(session["next"])
            return redirect(next)
        else:
            flash("Wrong Password")
    return render_template("login.html", username=username)


@app.route('/logout')
def logout():
    session.pop("user", None)
    session.pop("is_admin", None)
    return redirect("/")

if __name__ == '__main__':
    app.run()

