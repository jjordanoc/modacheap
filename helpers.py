from sys import exc_info

def handle_error_db(e, db):
    print("Exception:", e)
    print("Traceback:", exc_info())
    db.session.rollback()

def handle_error(e):
    print("Exception:", e)
    print("Traceback:", exc_info())