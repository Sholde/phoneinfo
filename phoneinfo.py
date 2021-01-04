#!/usr/bin/python3

import sys

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

if len(sys.argv) != 2:
    print("Usage: phoneinfo.py [PHONE NUMBER]")
    exit(1)

number = str(sys.argv[1])

parsing = phonenumbers.parse(number, "EN")
print("Country  :", geocoder.description_for_number(parsing, "en"))
print("Carier   :", carrier.name_for_number(parsing, "en"))
print("Timezone :", timezone.time_zones_for_number(parsing))
