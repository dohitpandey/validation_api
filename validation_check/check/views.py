from rest_framework.views import APIView
from rest_framework.response import Response
import re
import phonenumbers
import json
import requests

class validation(APIView):

    def post(self,request):
        Name=None
        Age=None
        Phone=None
        Email=None
        Pincode=None

        def name_check(n):
            if re.search("^(?!\s)[^0-9!@#$%^&*()_+\-=\[\]{}\"\';:?/><.,`~|\n]{2,50}$", n):
                NAME="Valid"
            else:
                NAME="Invalid"
            return NAME

        def age_check(a):
            try:
                if 0 < int(a) < 120:
                    AGE = "Valid"
                else:
                    AGE = "Invalid"
            except:
                AGE = "Invalid"
            return AGE

        def phone_check(p):
            p1=p.replace("-","")
            p2=p1.replace(" ","")
            ph = p2[-10:]
            try:
                phone_number = phonenumbers.parse(f"+91{ph}")
                valid = phonenumbers.is_valid_number(phone_number)
                if valid == True:
                    PHONE = "Valid"
                else:
                    PHONE = "Invalid"
            except:
                PHONE = "Invalid"
            return PHONE

        def email_check(e):
            if re.search("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]{2,}@[a-zA-Z0-9-]{2,}(?:\.[a-zA-Z0-9-]{2,})+$", e):
                if ".@" not in e and e[0]!=".":
                    EMAIL="Valid"
                else:
                    EMAIL = "Invalid"
            else:
                EMAIL="Invalid"
            return  EMAIL

        def pincode_check(pc):
            pin=pc.replace(" ","")
            url = f"https://api.postalpincode.in/pincode/{pin}"
            response = requests.request("GET", url)
            data = json.loads(response.text)
            if data[0].get("Status")=="Success":
                PINCODE="Valid"
            else:
                PINCODE="Invalid"
            return PINCODE

        if 'name' in request.data:
            name=request.data['name']
            Name=name_check(name)
        if 'age' in request.data:
            age=request.data['age']
            Age=age_check(age)
        if 'phone' in request.data:
            phone=request.data['phone']
            Phone=phone_check(phone)
        if 'email' in request.data:
            email=request.data['email']
            Email=email_check(email)
        if 'pincode' in request.data:
            pincode=request.data['pincode']
            Pincode=pincode_check(pincode)

        return Response({
            'Name':Name,
            'Age':Age,
            'Phone':Phone,
            'Email':Email,
            'Pincode':Pincode
        })
