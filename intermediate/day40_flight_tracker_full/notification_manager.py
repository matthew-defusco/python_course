from datetime import datetime, timedelta
import os
import smtplib
from email.mime.text import MIMEText

from flight_data import FlightData

class NotificationManager:
    def __init__(self):
        self.from_email = "dev.testing.5878@gmail.com"

    def notify(self, flight: FlightData):
        arrival_string = flight.arrival_date.split()[0]
        year = int(arrival_string.split("-")[0])
        month = int(arrival_string.split("-")[1])
        day = int(arrival_string.split("-")[2])

        arrival_date = datetime(year, month, day)
        # print(arrival_date.date())


        text_to_send = f"""
        There's a great flight that was found!
        Price: {flight.price}
        Departure City/Airport: {flight.origin_city}/{flight.origin_airport}
        Arrival City/Airport: {flight.destination_city}/{flight.destination_airport}
        Departure Date: {flight.departure_date}
        Arrival Date: {flight.arrival_date}
        # of Nights: {flight.nights}
        Return Date: {(arrival_date + timedelta(days=flight.nights)).date()}
        """

        send_string = MIMEText(text_to_send.encode("utf-8"), _charset="utf-8")
        send_string["Subject"] = "Subject: There's a great flight deal ✈️"
        send_string["From"] = self.from_email
        send_string["To"] = "dev.testing5878@yahoo.com"

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(
                user="dev.testing.5878@gmail.com",
                password=os.environ["EMAIL_PASSWORD"]
                )
            connection.send_message(send_string)
            connection.close()
