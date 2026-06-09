import app
import sys

def test_db():
    print("Testing DB connection...")
    try:
        with app.app.app_context():
            print("1. Creating tables...")
            app.db.create_all()
            
            print("2. Counting comments...")
            cnt = app.Comment.query.count()
            print(f"Current comments count: {cnt}")
            
            print("3. Adding a test comment...")
            test_comment = app.Comment(guest_name="DB Tester", text="Test database comment", rating=5)
            app.db.session.add(test_comment)
            app.db.session.commit()
            print("Comment added successfully!")
            
            print("4. Querying all comments...")
            comments = app.Comment.query.all()
            for c in comments:
                print(f"Comment: {c.guest_name} - {c.text} ({c.created_at})")
                
            print("5. Deleting test comment...")
            app.db.session.delete(test_comment)
            app.db.session.commit()
            print("Test comment deleted!")
            
    except Exception as e:
        print(f"DB Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_db()
