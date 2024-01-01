'''
https://myaccount.google.com/apppasswords

*App passwords: used for applications or devices that don't support Google's usual login method with a username and password, but require access to your Google Account. This is often the case with third-party applications, devices, or services that need to access your Gmail, Calendar, Contacts, or other Google services.

When you generate an App Password, it's a unique, application-specific password that you use instead of your regular Google Account password. This helps enhance security by providing a dedicated password for that particular application or device, without exposing your main Google Account credentials.

If you create an App Password for a specific application or device, you typically do not need to regenerate your main Google Account password. The App Password is specific to the application or device for which it was generated.


'''
# Import the smtplib module
import smtplib

# Define a function named 'send_mail'
def send_mail():
    try:
        # Create an SMTP server object for Gmail on port 587
        server = smtplib.SMTP('smtp.gmail.com', 587)

        # Perform the SMTP 'ehlo' handshake
        server.ehlo()

        # Start a secure TLS connection
        server.starttls()

        # Perform the SMTP 'ehlo' handshake again after starting TLS
        server.ehlo()

        # Open the 'password.txt' file in read mode to get the email password
        with open('EMAIL_SENDER/password.txt', 'r') as x:
            password = x.read()

        # Log in to the SMTP server using the Gmail email address and password
        server.login('xxx@gmail.com', password)

        # Specify the email subject
        subject = "Good morning!"

        # Open the 'body.txt' file in read mode to get the email body content
        with open('EMAIL_SENDER/body.txt', 'r', encoding='utf-8') as n:
            body = n.read()

        # Construct the email message with the specified subject and body
        msg = f"Subject: {subject}\n\n\n {body}"

        # Send the email from 'xxx@gmail.com' to 'yyy@naver.com'
        # Encode the message using utf-8
        server.sendmail(
            'xxx@gmail.com',
            'yyy@naver.com',
            msg.encode('utf-8')
        )

        # Print a success message if the email is sent successfully
        print('Message is sent successfully!')
    except Exception as e:
        # Print an error message if an exception occurs during the process
        print(f"An error occurred: {e}")

# Check if the script is run as the main module
if __name__ == "__main__":
    # Call the 'send_mail' function if the script is run as the main module
    send_mail()