import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "9zNsb3LmgWHeky7R9kBnHQpLkJGF1g9e"

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key":key,"from":orig,"to":dest})
    json_data = requests.get(url).json()

    print("URL:" + (url))
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API status:" + str(json_status) + " = Successful route call. \n")
        print("Directions from: " + (orig) + "to: " + (dest))
        print("Trip duration " + (json_data["route"]["formattedTime"]))
        print("Miles " + str(json_data["route"]["distance"]))
        print("Kilometers " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))

        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " Km)"))
    elif json_status == 402:
        print("API status:" + str(json_status) + " = Invalid user input. \n")
    elif json_status == 611:
        print("API status:" + str(json_status) + " = Missing entry. \n")
    else:
        print("API status:" + str(json_status) + " = Error. \n")