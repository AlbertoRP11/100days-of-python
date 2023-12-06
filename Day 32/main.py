import datetime as dt
import random
import pandas as pd
import smtplib

PLACEHOLDER = "[NAME]"
my_email = "your email"
password = "your password"

now = dt.datetime.now()
today = (now.day, now.month)

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(row.day, row.month): row for (index, row) in data.iterrows()}
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"./letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as file:
        content = file.read()
        birthday_msg = content.replace(PLACEHOLDER, birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{birthday_msg}"
        )
