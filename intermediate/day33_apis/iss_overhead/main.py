import requests
import smtplib
import datetime as dt
import time
import sched

# If the ISS is overhead
# And it's nighttime (dark outside, past sunset)
# Then email me to tell me to look up
# BONUS: Run the code every 60 seconds

PIT_LAT = 40.440624
PIT_LONG = -79.995888
PIT_LOC = (PIT_LAT, PIT_LONG)

EMAIL = "dev.testing.5878@gmail.com"
PASSWORD = "chhtiosxcnzezios"


def is_time_between(start_time, end_time, check_time):
    """
  Check if a time is between two other times.
  Times must be in datetime.time() format.
  Returns:
    True if the check_time is between the start_time and end_time, False otherwise.
  """

    # Check if the check_time is between the start_time and end_time.
    return start_time <= check_time <= end_time


def is_above():
    # Get ISS location data
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    iss_data = response.json()
    longitude = float(iss_data["iss_position"]["longitude"])
    latitude = float(iss_data["iss_position"]["latitude"])

    iss_pos = (longitude, latitude)
    current_pos = PIT_LOC

    iss_lat = iss_pos[0]
    current_lat = current_pos[0]
    iss_long = iss_pos[1]
    current_long = current_pos[1]
    if (current_lat - 5 <= iss_lat <= current_lat + 5) and (current_long - 5 <= iss_long <= current_long + 5):
        return True
    else:
        return False


def main():
    print("running...")
    # Figure out if it's dark or not
    daylight_parameters = {
        "lat": PIT_LAT,
        "lng": PIT_LONG,
        "formatted": 0
    }

    daylight_data = requests.get("https://api.sunrise-sunset.org/json", params=daylight_parameters).json()

    sunrise_hour = int(daylight_data["results"]["sunrise"].split("T")[1].split("+")[0].split(":")[0])
    sunrise_minute = int(daylight_data["results"]["sunrise"].split("T")[1].split("+")[0].split(":")[1])
    sunset_hour = int(daylight_data["results"]["sunset"].split("T")[1].split("+")[0].split(":")[0])
    sunset_minute = int(daylight_data["results"]["sunset"].split("T")[1].split("+")[0].split(":")[1])

    sunrise_time = dt.time(sunrise_hour, sunrise_minute)
    sunset_time = dt.time(sunset_hour, sunset_minute)
    now_time = dt.datetime.now().time()

    # if iss_position == PIT_LOC and is_time_between(sunset_time, sunrise_time, now_time):
    if is_above() and is_time_between(sunset_time, sunrise_time, now_time):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs="matthew.defusco@gmail.com",
                msg="Subject: The ISS is above you!\n\nIt's dark outside and you've got a chance of seeing the ISS!")
            connection.close()
    else:
        print("Nope, it's not above you.")

    print("finished running...")


main()
while True:
    s = sched.scheduler(time.time, time.sleep)
    s.enter(5, 1, main)
    s.run()
