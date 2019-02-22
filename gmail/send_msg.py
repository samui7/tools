import create_msg 
import create_msg_with_attachments
from httplib2 import Http
from googleapiclient.discovery import build
from apiclient import errors
from google.oauth2 import service_account
import base64
import sys

# currently only 1 attachment is supported

def send_message(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        print("Message Id: %s", message['id'])
        return message
    except errors.HttpError as error:
        print("An error occurred: %s", error)

def service_account_login():
    SCOPES = ['https://www.googleapis.com/auth/gmail.send']
    SERVICE_ACCOUNT_FILE = 'credentials.json'
    credentials = service_account.credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes = SCOPES)
    delegated_credentials = credentials.with_subject(EMAIL_FROM)
    service = build('gmail', 'v1', credentials = delegated_credentials)
    return service

def main(to, subject, txt_path, attachments):

    # modify EMAIL_FROM
    EMAIL_FROM = "EMAIL ADDRESS"
    EMAIL_TO = to
    EMAIL_SUBJECT = subject

    print("main(), opening txt")
    with open(txt_path, 'r') as txt:
        text = txt.read().replace('\n', '')
        EMAIL_CONTENT = text
    
    print("main(), creating msg")
    if len(attachments) > 0:
        message = create_msg_with_attachments.create_message_with_attachment(EMAIL_FROM, EMAIL_TO, 
                EMAIL_SUBJECT, EMAIL_CONTENT, attachments)
    else:
        message = create_msg.create_message(EMAIL_FROM, EMAIL_TO, 
                EMAIL_SUBJECT, EMAIL_CONTENT)
    
    print("main(), calling service and sending")
    service = service_account_login()
    sent = send_message(service, 'me', message)

if __name__=='__main__':

# to , subject, content txt, attachment
    print("start")
    to = sys.argv[1]
    subject = sys.argv[2]
    txt_path = sys.argv[3]
    attachment = ""
    if len(sys.argv) == 5:
        # one attachment
        attachment += sys.argv[4]
    print("calling ")
    main(to, subject, txt_path, attachment)
    







