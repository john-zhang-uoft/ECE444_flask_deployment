# create_db.py


from project.app import app, db
from project.models import Post

def create_db():
    with app.app_context():
        # create the database and the db table
        db.create_all()

        # commit the changes
        db.session.commit()
    
if __name__ == "__main__":
    create_db()
