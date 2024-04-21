#!/usr/bin/python3
"""FLASK APP"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Closes the db session"""
    storage.close()


@app.route("/states", strict_slashes=False)
def state_list():
    return render_template("7-states_list.html",
                           states=storage.all(State))


@app.route("/states/<id>", strict_slashes=False)
def state_by_id(id):
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html",
                                   states=state)
    return render_template("9-states.html", states=None)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
