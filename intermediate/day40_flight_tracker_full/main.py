from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

SHEET_URL = "https://api.sheety.co/3609f29ae6976a55f6868df66df56155/flightDeals/prices"

dataManager = DataManager(SHEET_URL)
flightSearch = FlightSearch()
notificationManager = NotificationManager()

sheet_data = dataManager.get_records().json()

for row in sheet_data["prices"]:
    city = row["city"]
    print(row)
    # Check if there's an IATA code in the spreadsheet, and populate it if not.
    if row["iataCode"] == "":
        iataCode = flightSearch.get_iata_code(city)
        row["iataCode"] = iataCode
        data_to_update = {
        "price": {
            "iataCode": row["iataCode"]
            }
        }

        dataManager.update_record(row["id"], data=data_to_update)

    flight_info = flightSearch.search_flights_from_PIT(row["iataCode"])
    if flight_info and flight_info.price <= row["lowestPrice"]:
        notificationManager.notify(flight_info)
    else:
        pass
