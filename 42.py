#Phone number analyzer

import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from tabulate import tabulate

def number_check(Phone_number):
    number = phonenumbers.parse(Phone_number)
    description = geocoder.description_for_number(number,"en")
    supplier = carrier.name_for_number(number,"en")
    info = [["country","supplier"],[description,supplier]]

    return tabulate(info, headers="firstrow",tablefmt="github")

if __name__  == "__main__":
    number = int(input("enter the phone number :"))
    print(number_check(number))