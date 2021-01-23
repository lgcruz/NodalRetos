from __future__ import print_function
import pickle
import os.path

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1DRD97TAw2WIuTCG0Nh6BW-aVvDKAgY1wvJb38V-3vU8'
SAMPLE_RANGE_NAME = 'Reto1!A2:C'


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    requests = []
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Author, Sentiment:')
        #for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
        #    print('%s, %s, %s' % (row[0], row[1],row[2]))

    requests.append({
        'updateCells': {
            'rows': {
                'values': [
                    {
                        'pivotTable': {
                            'source': {
                                'sheetId': SAMPLE_SPREADSHEET_ID,
                                'startRowIndex': 1,
                                'startColumnIndex': 0,
                                'endRowIndex': 16,
                                'endColumnIndex': 4
                            },
                            "rows": [
                                {
                                    "sourceColumnOffset": 0,
                                    "showTotals": False,
                                    "sortOrder": "DESCENDING"
                                },
                                {
                                    "sourceColumnOffset": 1,
                                    "showTotals": False,
                                    "sortOrder": "DESCENDING",
                                },
                            ],
                            'columns': [
                                {
                                    'sourceColumnOffset': 2,
                                    'sortOrder': 'ASCENDING',
                                    'showTotals': False,

                                },
                                {
                                    'sourceColumnOffset': 3,
                                    'sortOrder': 'ASCENDING',
                                    'showTotals': False,

                                },
                            ],
                        }
                    }
                ]
            },
            'start': {
                'sheetId': '1gCO95HVQ2IkrcURptkxViNC2rWESPUadK_42oXKp4II',
                'rowIndex': 0,
                'columnIndex': 0
            },
            'fields': 'pivotTable'
        }
    })
    body = {
        'requests': requests
    }
    response = service.spreadsheets().batchUpdate(spreadsheetId='1gCO95HVQ2IkrcURptkxViNC2rWESPUadK_42oXKp4II', body=body).execute()

if __name__ == '__main__':
    main()