import gspread
import datetime
import sys
from oauth2client.service_account import ServiceAccountCredentials

if __name__ == '__main__':
    queries = sys.argv[1]
    email = "priyaverma@gmail.com"
    timestamp = str(datetime.datetime.now())

    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("/Users/macair/Desktop/Siddharth/Final year project/GSOC/engine/creds.json", scope)

    client = gspread.authorize(creds)

    sheet = client.open("User Queries").sheet1

    data = sheet.get_all_records()

    insertData = [email, queries, timestamp]

    sheet.insert_row(insertData, 2)
