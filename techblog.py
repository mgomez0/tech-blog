from app import app, db
from app.models import Entry, User, FTSEntry


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Entry': Entry, 'FTSEntry': FTSEntry}

