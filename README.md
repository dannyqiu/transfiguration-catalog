Transfiguration Library Catalog
-------------------------------

This web application was created for the Transfiguration School library as a means for teachers to search, borrow, and return books.

The library originally used a old system of recording all books on an Excel spreadsheet on one computer until Stuyvesant Key Club came in and helped re-catalog the library because of the inconsistency between the physical books and the record. We decided to go with a collaborative, available-anywhere catalog on [Google Spreadsheets](http://spreadsheets.google.com). This application serves as an easier way to interact with the data on the spreadsheet.

## Features

- Searching for books
- Use of Google accounts for:
    - Borrowing books
    - Returning books
- Viewing all books that are cataloged

## Setup

1. Install dependencies using pip: `pip install -r requirements.txt -t lib`
2. Download credentials for a service account and move the json data to the root of this repository. Rename it to `client_secrets.json`
3. Deploy to Google App Engine

## Requirements

- [oauth2client](https://github.com/google/oauth2client)
- [gspread](https://github.com/burnash/gspread)
