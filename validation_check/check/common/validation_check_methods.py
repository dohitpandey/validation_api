import json
import re
import requests
import phonenumbers


def name_check(n):
    if re.search("^(?!\s)[^0-9!@#$%^&*()_+\-=\[\]{}\"\';:?/><.,`~|\n]{2,50}$", n):
        name = "Valid"
    else:
        name = "Invalid"
    return name


def age_check(a):
    try:
        if 0 < int(a) < 120:
            age = "Valid"
        else:
            age = "Invalid"
    except:
        age = "Invalid"
    return age


def phone_check(p):
    p1 = p.replace("-", "")
    p2 = p1.replace(" ", "")
    ph = p2[-10:]

    try:
        phone_number = phonenumbers.parse(f"+91{ph}")
        valid = phonenumbers.is_valid_number(phone_number)
        if valid == True:
            phone = "Valid"
        else:
            phone = "Invalid"
    except:
        phone = "Invalid"
    return phone


def email_check(e):
    if re.search("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]{2,}@[a-zA-Z0-9-]{2,}(?:\.[a-zA-Z0-9-]{2,})+$", e):
        if ".@" not in e and e[0] != ".":
            email = "Valid"
        else:
            email = "Invalid"
    else:
        email = "Invalid"
    return email


def pincode_check(pc):
    pin = pc.replace(" ", "")
    url = f"https://api.postalpincode.in/pincode/{pin}"
    response = requests.request("GET", url)
    data = json.loads(response.text)
    if data[0].get("Status") == "Success":
        pincode = "Valid"
    else:
        pincode = "Invalid"
    return pincode
