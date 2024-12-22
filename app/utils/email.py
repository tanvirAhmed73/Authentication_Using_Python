def send_reset_email(email:str, reset_token:str):
    #send the password reset token to the user email
    reset_url = f"http://localhost:8000/auth/resetPassword?token={reset_token}"
    print(reset_url)