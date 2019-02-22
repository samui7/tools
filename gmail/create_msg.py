from email.mime.text import MIMEText
import base64

def create_message(sender, to, subject, message_text):
	# Returns an object containing a base64url encoded email object

	message = MIMEText(message_text)
	message['to'] = to
	message['from'] = sender
	message['subject'] = subject
	return {'raw': base64.urlsafe_b64encode(message.as_string())}