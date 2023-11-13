from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db
from flaskr.open_gate import open,open_pedestrian

bp = Blueprint('access', __name__)

@bp.route('/access')
@login_required
def access():
    return render_template('access.html')

@bp.route('/open_gate')
def open_gate():
    res = open()
    return res

@bp.route('/open_pedestrian_gate')
def open_pedestrian_gate():
    res = open_pedestrian()
    return res

