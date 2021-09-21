# Send Email

This is a simple python application for sending Gmail emails.

## Features
- Log in your Gmail accounts.
- Send emails with applied template.
- Save errors and succesfully sent emails into files.

## Requirements
- In order to log-in your Gmail you must [Allow less secure App on](https://myaccount.google.com/intro/security).
- Python >= 3.6

## Installation
- Install all dependencies with 
```sh
pip3 install -r requirements.txt
```
## Running
```sh
python send_email.py --email=your_login_email --template=path/to/email_template.json --customer=path/to/customers.csv --output=path/to/output.json --errors=path/toerrors.csv
```
