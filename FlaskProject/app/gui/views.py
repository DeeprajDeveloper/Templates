import os
from datetime import datetime
from flask import Blueprint, request, render_template, abort, flash, redirect, url_for
from werkzeug.exceptions import HTTPException
from app.gui import functionality as gui_func
from app.constants import Information as Const

bp_gui = Blueprint(
    'bp_gui'
    , __name__
    , url_prefix='/gui'
    , template_folder='templates'
    , static_folder=os.path.join(os.path.dirname(__file__), 'static')
    , static_url_path='/bp_gui/static'
)
