# import network request library
import requests

# allow the user to enter a location
location: str = str(input("Enter a location: "))
print("Getting the weather . . .")
try:
    # reqest to the website
    res = requests.get(f"https://wttr.in/{location}?format=3")
    # print out the response text
    print(res.text)
except Exception as err:
    # if the place does not exist
    print(err)
