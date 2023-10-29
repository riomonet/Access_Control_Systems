from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db
from flaskr.modules.open_gate import open

bp = Blueprint('access', __name__)

@bp.route('/access')
@login_required
def access():
    return render_template('access.html')

@bp.route('/open_gate')
def open_gate():
    res = open()
    if res == 1:
        result = 'succses'
    else:
        result = 'fail'
    return {'result': result};
