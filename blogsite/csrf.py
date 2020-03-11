# CSRF related methods
from typing import Optional, Any

from . import app, sanitise, routes
from . import db

from flask import redirect, url_for, session, flash

from datetime import datetime, timedelta
import time
import random
import string


def create_token(the_user):
    values = [csrf_token(), datetime.utcnow(), the_user.id]
    raw_sql = 'INSERT INTO csrf_token (token, valid_from, user_id) VALUES({})'.format(
        ', '.join('"{}"'.format(str(v)) for v in values)
    )
    # flash(raw_sql)
    db.session.execute(raw_sql)
    db.session.commit()
    session['user_csrf'] = values[0]
    return


def delete_token():
    session_user = session.get('user_id')
    raw_sql = 'SELECT * FROM csrf_token WHERE user_id="{}"'.format(session_user)
    # flash(raw_sql)
    results = db.session.execute(raw_sql)
    values = results.fetchall()
    for v in values:
        raw_sql = 'DELETE FROM csrf_token WHERE token="{}" AND user_id="{}"'.format(v[0], v[2])
        # flash(raw_sql)
        db.session.execute(raw_sql)
        db.session.commit()


def csrf_token():
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(25))


# validates if the session is still within the specified time period. Returns true if valid, else false.
def validate_session():
    session_user = session.get('user_id')

    raw_sql = 'SELECT * FROM csrf_token WHERE user_id="{}"'.format(session_user)
    # flash(raw_sql)
    results = db.session.execute(raw_sql)
    values = results.first()
    # In production, validity period would be set to 20 minutes as per OWASP recommendation.
    valid_period = datetime.strptime(values[1], '%Y-%m-%d %H:%M:%S.%f') + timedelta(minutes=10)

    if compare_time(valid_period):
        if check_csrf(values[0]):
            token = csrf_token()
            raw_sql = 'UPDATE csrf_token SET token="{}", valid_from="{}" WHERE user_id="{}";'.format(
                 token, datetime.utcnow(), session_user)
            # flash(raw_sql)
            db.session.execute(raw_sql)
            db.session.commit()
            session['user_csrf'] = token
            return True
    else:
        flash('Session expired, please login again.')
        routes.logout()
        return redirect(url_for('logout'))


# If the current time is less than than the time passed, return true. Else return false.
def compare_time(comparison_time):
    now = datetime.utcnow()
    if now < comparison_time:
        return True
    else:
        return False


# Checks the CSRFToken held in the session matches that of the CSRFToken in the DB
def check_csrf(db_token):
    session_token = session.get('user_csrf')
    if session_token == db_token:
        return True
    return False

