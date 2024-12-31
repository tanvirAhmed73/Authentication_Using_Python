import smtplib
from email.mime.text import MIMEText
from email_validator import validate_email, EmailNotValidError


# check if the email is valid or not
def validationEmail(email:str)->bool:
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False




# send the reset token to the user email
def send_reset_email(email:str, reset_token:str):
    #send the password reset token to the user email
    reset_url = f"http://localhost:8000/auth/setNewPasswrod?token={reset_token}"
    msg = MIMEText(f"Click the following link to reset your password: {reset_url}")
    msg['Subject'] = "Password Reset"
    msg['From'] = "tanvir.073.ahmed@gmail.com"
    msg['To'] = "tanvir734215@gmail.com"
    
     # Gmail SMTP settings
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "tanvir.073.ahmed@gmail.com"
    sender_password = "qpwi kzei axhr cmaw" 

    try:
        # Connect to Gmail SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Start TLS encryption
            server.login(sender_email, sender_password)  # Login to your email account
            server.sendmail(msg["From"], [msg["To"]], msg.as_string())  # Send the email
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")