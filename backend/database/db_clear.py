import sys
sys.path.insert(0, '..')

from app import app, db, models

def clear_db():
    with app.app_context():
        # Drop all tables
        db.drop_all()

        # Commit the changes
        db.session.commit()

    print("Database cleared!")

if __name__ == "__main__":
    clear_db()
