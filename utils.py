import csv
import json

import datetime
import yagmail
from getpass import getpass

import pandas as pd


import re

regex = r"^[a-z0-9]+[\.]?[a-z0-9]+[@]\w+[.]\w{2,3}$"


def check_email_format(email):
    if re.fullmatch(regex, email):
        return True
    return False


def add_errors(customers, path, csv_header):
    if not customers:
        return None
    with open(path, "+a") as file:
        write = csv.writer(file)
        if file.tell() == 0:
            write.writerow(csv_header)
            write.writerows(customers)
        else:
            write.writerows(customers)


def add_success(customers, path):
    if not customers:
        return None
    with open(path, "+w") as data:
        json.dump(customers, data, indent=1)


def apply_detail_to_template(template, customer):
    today = datetime.date.today().strftime("%d %b %G")

    body = (
        template["body"]
        .format()
        .format(
            TITLE=customer["TITLE"],
            FIRST_NAME=customer["FIRST_NAME"],
            LAST_NAME=customer["LAST_NAME"],
            TODAY=today,
        )
    )

    return {
        "from": template["from"],
        "to": customer["EMAIL"],
        "subject": template["subject"],
        "mimeType": template["mimeType"],
        "body": body,
    }
