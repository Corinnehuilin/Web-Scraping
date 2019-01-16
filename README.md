# Web Scraping

This program will text a phone number (through [Twilio](https://www.twilio.com)) if a website that you have chosen to monitor has changed. All you need to do is enter the website URL, the number you want the text from, and the number you want the text to go to. This is done through scrapingvariables.py.

## To Begin
- You will need to import requests.
```
pip install requests
```
- You will also need a [Twilio](https://www.twilio.com) account.

## scrapingvariables.py
You will need to create a file called "scrapingvariables.py" with the following variables:
```
url = "THE WEBSITE YOU WANT TO MONITER"
account_sid = "YOUR ACCOUNT SID FROM TWILIO"
auth_token = "YOUR AUTH TOKEN FROM TWILIO"
twilio_phone_number = "+1THE NUMBER YOU WANT THE TEXT TO COME FROM (FROM TWILIO)"
my_phone_number = "+1THE NUMBER YOU WANT THE TEXT TO SEND TO (YOUR PHONE NUMBER)"
```
Don't forget the +1 before the phone numbers!

### gitscraping.py
This is where all of the magic happens! There are comments in the gitscraping.py file if some of the code is confusing.

You can customize the message that sends in line 51 through 
```
send_message("The website changed!")
```
This code automatically checks a website every 5 seconds, but how long the program waits (in seconds) may be changed in line 19 through
```
default = 5
```

### index.html
This is a test file used to make testing easier.

###### As a general courtesy, please respect a website's terms of use and don't overload their servers!
