from __future__ import print_function
import pickle
import os.path

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


class Gmail:
    def __init__(self, ns, config_dir):
        self.ns = ns
        self.badge = 0

        self.ns.register('gmail', self.badge)

        creds_file_loc = os.path.join(config_dir, 'credentials.json')
        pickle_file_loc = os.path.join(config_dir, 'token.pickle')

        """Shows basic usage of the Gmail API.
        Lists the user's Gmail labels.
        """
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(pickle_file_loc):
            with open(pickle_file_loc, 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    creds_file_loc, SCOPES)
                creds = flow.run_local_server()
            # Save the credentials for the next run
            with open(pickle_file_loc, 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('gmail', 'v1', credentials=creds)

    def refresh(self):
        # pylint: disable=no-member
        results2 = self.service.users().labels().get(userId="me", id="INBOX").execute()
        unread = results2.get("messagesUnread")

        if unread or unread == 0:
            self.badge = unread
        self.ns.update('gmail', self.badge)
