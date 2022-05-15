from flask import abort

def handle_error_db(e, db):
    print(e)
    db.session.rollback()
    abort(500)

def handle_error(e):
    print(e)
    abort(500)