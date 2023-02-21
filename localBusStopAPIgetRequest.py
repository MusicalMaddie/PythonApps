import requests
import datetime

# Define the API endpoint
endpoint = "https://api-v3.mbta.com/predictions"
filter = "?filter[stop]=17094"
endpoint = (f"{endpoint}{filter}")

# Instantiate Global variables
arrivalTime = ""
soonestTime = ""

print(endpoint)

# Define the API parameters
params = {
    "filter[stop]": "17094",
    "filter[route]": "57",
    "sort": "arrival_time",
    "api_key": "110adb3ad66e4f27be542ffeaeacbee3"
}

# Send a GET request to the API endpoint with the parameters
response = requests.get(endpoint)

#print(requests.get(endpoint).json())

# Check if the response was successful (HTTP status code 200)
if response.status_code == 200:
    # Parse the JSON data from the response
    data = response.json()

    if response.status_code == 200:
        # Parse the JSON data from the response
        data = response.json()
        print(data)

    #if data returned, loop through and find all times
    if "data" in data:
        for item in data["data"]:
            attributes = item.get("attributes")
            if attributes is not None:
                arrival_time_str = attributes.get("arrival_time")
                if arrival_time_str is not None:
                    arrival_time = datetime.datetime.fromisoformat(arrival_time_str[:-6])
                    arrival_time_formatted = arrival_time.strftime("%H:%M")
                    print(arrival_time_formatted)
                    if soonestTime == "" :
                        soonestTime = arrival_time_formatted

        next_arrival = data["data"][0]["attributes"]["arrival_time"]
        print(f"The next arrival time for Bus 57 at Linden Street is {soonestTime}.")
    else:
        print("No predictions were found.")
else:
    print(f"Request failed with status code {response.status_code}.")