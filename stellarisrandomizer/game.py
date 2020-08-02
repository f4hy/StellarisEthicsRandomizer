from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from stellarisrandomizer.auth import login_required
from stellarisrandomizer.db import get_db

bp = Blueprint("game", __name__)


@bp.route("/")
def index():
    db = get_db()
    games = db.execute(
        "SELECT p.id, title, body, created, author_id, steamid"
        " FROM game p JOIN user u ON p.author_id = u.id"
        " ORDER BY created DESC"
    ).fetchall()
    return render_template("game/index.html", games=games)


@bp.route("/create", methods=("GET", "POST"))
@login_required
def create():
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "INSERT INTO game (title, body, author_id)" " VALUES (?, ?, ?)",
                (title, body, g.user["id"]),
            )
            db.commit()
            return redirect(url_for("game.index"))

    return render_template("game/create.html")


def get_game(id, check_author=True):
    game = (
        get_db()
        .execute(
            "SELECT p.id, title, body, created, author_id, steamid"
            " FROM game p JOIN user u ON p.author_id = u.id"
            " WHERE p.id = ?",
            (id,),
        )
        .fetchone()
    )

    if game is None:
        abort(404, "Game id {0} doesn't exist.".format(id))

    if check_author and game["author_id"] != g.user["id"]:
        abort(403)

    return game


@bp.route("/<int:id>/update", methods=("GET", "POST"))
@login_required
def update(id):
    game = get_game(id)

    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "UPDATE game SET title = ?, body = ?" " WHERE id = ?", (title, body, id)
            )
            db.commit()
            return redirect(url_for("game.index"))

    return render_template("game/update.html", game=game)


@bp.route("/<int:id>/delete", methods=("POST",))
@login_required
def delete(id):
    get_game(id)
    db = get_db()
    db.execute("DELETE FROM game WHERE id = ?", (id,))
    db.commit()
    return redirect(url_for("game.index"))
