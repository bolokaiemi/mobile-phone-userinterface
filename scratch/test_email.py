import app
import os

def test_email():
    print("=== TESTING EMAIL NOTIFICATION ===")
    print(f"SMTP Server: {os.environ.get('SMTP_SERVER')}")
    print(f"SMTP Email/Sender: {os.environ.get('SMTP_EMAIL')}")
    
    # Establish app context
    with app.app.app_context():
        print("Sending test email alert...")
        app.send_notification_email(
            subject="[EbiUI Test] SMTP Integration Check",
            body="Hello,\n\nThis is a test email confirming that Flask-Mail has been integrated successfully into EbiUI!\n\nBest regards,\nEbiUI Development Team"
        )
        print("Test email function finished executing! Check the console output for SMTP errors.")

if __name__ == "__main__":
    test_email()
