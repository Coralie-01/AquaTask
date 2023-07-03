import sys
sys.path.insert(0, '..')

from app import app, db, models

def setup_db():
    with app.app_context():
        # Create all tables
        db.create_all()

        # Commit the changes
        db.session.commit()

    print("Database setup completed!")

if __name__ == "__main__":
    setup_db()
