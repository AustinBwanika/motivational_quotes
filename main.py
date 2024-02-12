# import smtplib
#
# my_email = "kasetunes@gmail.com"
# password = "nzqubvfhaptabwek"
#
# # Makes connection secure
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="austinbwanika@gmail.com", msg="Subject:Hello Mate\n\n This is the "                                                        "body of my email" )
#     connection.close()

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.weekday()
#
# date_of_birth = dt.datetime(year=2004, month=2, day=20)
# print(now.year)

import datetime as dt
import smtplib as mail
import random

now = dt.datetime.now()
day = now.weekday()

quotes = []
with open("quotes.txt", "r") as file:
    for line in file:
        quotes.append(line.strip())

rand_num = random.randint(0, len(quotes))
message = quotes[rand_num]
print(now.weekday())

my_email = "example@gmail.com"
password = "example password"

# Makes connection secure
if day == 0:
    with mail.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject: Monday Motivation \n\n{message}")