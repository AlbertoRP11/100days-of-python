import requests
from datetime import datetime
import smtplib
import time

MY_LAT = int("your latitude")
MY_LONG = int("your longitude")
MY_EMAIL = "your email"
PW = "your password"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if iss_latitude <= MY_LAT + 5 or iss_latitude >= MY_LAT - 5 and iss_longitude <= MY_LONG + 5 or iss_longitude >= MY_LONG - 5:
        iss_is_close = True

def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

# Send an email every minute to look up to see the ISS
while True:
    if is_iss_overhead() and is_dark():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PW)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:ISS in the Sky\n\nLook up!"
            )
        time.sleep(60)