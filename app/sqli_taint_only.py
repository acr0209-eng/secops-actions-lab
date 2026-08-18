import flask
from flask import request

app = flask.Flask(__name__)


def search(cur):
    q = request.args.get("q")
    cur.execute(
        "SELECT * FROM users WHERE name LIKE ?",
        (f"%{q}%",),
    )
