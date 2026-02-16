from __init__ import create_app, db  # import your Flask app factory and db
import students  # import your students model

app = create_app()

# <-- HERE is the critical part
with app.app_context():
    db.create_all()  # this will create db.sqlite
    print("Database created successfully!")
    student = students.Students(name="John", subject="Math", marks=85)
    student1 = students.Students(name="Johny", subject="Science", marks=80)
    db.session.add(student)
    db.session.add(student1)
    db.session.commit()
    print("Student added!")