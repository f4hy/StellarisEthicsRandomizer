from collections import defaultdict
import uuid
import json
from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
from wtforms import StringField
from wtforms.fields import SelectMultipleField, FieldList, FormField
from wtforms.widgets import CheckboxInput  # RangeInput
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from stellarisrandomizer.auth import login_required
from stellarisrandomizer.db import get_db
from stellarisrandomizer.ranges import get_ranges
from stellarisrandomizer.agg import game_vote_aggregator

bp = Blueprint("game", __name__)


@bp.route("/")
def index():
    db = get_db()
    games = db.execute(
        "SELECT p.id, gameid, created, steamid, votes"
        " FROM game p JOIN user u ON p.author_id = u.id"
        " ORDER BY created DESC"
    ).fetchall()
    return render_template("game/index.html", games=games)


class VoteItemForm(FlaskForm):
    select = SelectMultipleField(choices=[], validators=[DataRequired()])


class VotingForm(FlaskForm):
    gameid = StringField("gameid", validators=[DataRequired()])
    select_entries = FieldList(FormField(VoteItemForm))


def get_vote_entries():
    ranges = get_ranges("medium")
    entries = []

    def tupulize(lst):
        return [(i, i) for i in lst]

    for name, choices in ranges.items():
        select_entry = VoteItemForm()
        select_entry.select.label = name
        select_entry.select.id = name
        select_entry.select.name = name
        select_entry.id = uuid.uuid1()
        select_entry.name = name
        select_entry.select.choices = tupulize(choices)
        select_entry.size = len(choices)
        entries.append(select_entry)
    return entries


@bp.route("/create", methods=("GET", "POST"))
@login_required
def create():
    form = VotingForm()
    form.select_entries = get_vote_entries()
    if request.method == "POST" and form.validate_on_submit():
        gameid = request.form["gameid"]
        votes = {}
        for k, v in request.form.lists():
            votes[k] = v
        error = None

        if not gameid:
            error = "gameid is required"

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "INSERT INTO game (gameid, author_id, votes)" " VALUES (?, ?, ?)",
                (gameid, g.user["id"], json.dumps(votes)),
            )
            db.commit()
            return redirect(url_for("game.index"))
    return render_template("game/vote.html", form=form)


def get_games(gameid, check_author=True):

    games = (
        get_db()
        .execute(
            "SELECT p.gameid, created, author_id, steamid, votes"
            " FROM game p JOIN user u ON p.author_id = u.id"
            " WHERE p.gameid = ?",
            (gameid,),
        )
        .fetchall()
    )

    if not games:
        abort(404, "Game id {0} doesn't exist.".format(id))

    return games


@bp.route("/<id>/tally", methods=("GET", "POST"))
@login_required
def tally(id):
    print("tally")
    games = get_games(id)
    jsons = [json.loads(game["votes"]) for game in games]
    agged = game_vote_aggregator(jsons)
    for j, g in zip(jsons, games):
        del j["csrf_token"]
        j["steamid"] = g["steamid"]
    print("got", games)
    return render_template("game/tally.html", votes=agged, raw=jsons, gameid=id)
