
import datetime as dt
import pandas
import random
import smtplib

my_email = "**email**"
password = "**password**"

now = dt.datetime.now()
today = (now.month, now.day)
# print(today)

data = pandas.read_csv("birthdays.csv")
# print(data)

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
# print(birthdays_dict)

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter:
        context = letter.read()
        person = context.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{person}"
        )







