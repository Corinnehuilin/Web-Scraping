import argparse
import time
from urllib.request import urlopen

import requests
from twilio.rest import Client

import scrapingvariables

client = Client(scrapingvariables.account_sid, scrapingvariables.auth_token)

# Parse out the arguments (or parameters) from the terminal
def parse_args():
    parser = argparse.ArgumentParser(description = "Website monitoring and texting")
    parser.add_argument(
        "--url", help = "URL of the website to monitor", default=scrapingvariables.url
    )
    parser.add_argument(
        "--delay", help = "Time delay (in seconds) between scraping", default = 5
    )
    args = parser.parse_args()
    return args


# Get html from the url
def fetch_html(url):
    content = requests.get(url)
    return content.text


# Send an SMS using Twilio
def send_message(msg):
    _ = client.messages.create(
        body = msg,
        from_ = scrapingvariables.twilio_phone_number,
        to = scrapingvariables.my_phone_number,
    )


# Monitor the url for any changes
def monitor(url, delay):
    old_html = fetch_html(url)

    while True:
        time.sleep(delay)
        new_html = fetch_html(url)

        # If the HTML of the page is different than last time,
        # send a text message
        if new_html != old_html:
            send_message("The website changed!")
            old_html = new_html


# Get parameters
args = parse_args()

# Try to use URL, exit if the URL is invalid or if the program crashes
try:
    _ = fetch_html(args.url)
except (
    requests.exceptions.InvalidSchema,
    requests.exceptions.InvalidURL,
    requests.exceptions.MissingSchema,
) as _:
    print('The provided URL ("{}") is invalid.'.format(args.url))
    exit()
except:
    print("Error.")
    exit()

# Try to turn the delay into a number, and make sure it is greater than zero.
try:
    delay = float(args.delay)
    if delay <= 0.0:
        print("Please make sure the delay is greater than zero.")
        exit()
except ValueError:
    print("Please make sure the delay is a real number.")
    exit()

print(
    'Beginning monitoring of "{}".\npress Ctrl+C to exit.'.format(
        args.url
    )
)

# Start monitoring website, exit when user
# presses Ctrl+C (which sends a KeyboardInterrupt)

try:
    monitor(args.url, float(args.delay))
except KeyboardInterrupt:
    print("Ending monitoring...")
