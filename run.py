from app import app
from db import db

db.__init__(app)
# sqlAlchemy looks through impports to see what columns an tables to create
@app.before_first_request
def create_table():
    db.create_all()