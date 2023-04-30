from check.common import validation_check_methods
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView


class Validation(APIView):
    @swagger_auto_schema(operation_id='validate_input', request_body=openapi.Schema(
        type='object',
        properties={
            'Name': openapi.Schema(type='string', example='John Doe'),
            'Age': openapi.Schema(type='string', example='30'),
            'Phone': openapi.Schema(type='string', example='+91 1234567890'),
            'Email': openapi.Schema(type='string', example='johndoe@example.com'),
            'Pincode': openapi.Schema(type='string', example='400001')
        }
    ), responses={200: openapi.Schema(
        type='object',
        properties={
            'Name': openapi.Schema(type='string', example='Valid'),
            'Age': openapi.Schema(type='string', example='Invalid'),
            'Phone': openapi.Schema(type='string', example='Valid'),
            'Email': openapi.Schema(type='string', example='Valid'),
            'Pincode': openapi.Schema(type='string', example='Valid')
        }
    )})

    def post(self, request):
        response = {}
        if 'Name' in request.data:
            name = str(request.data['Name'])
            Name = validation_check_methods.name_check(name)
            response['Name'] = Name
        if 'Age' in request.data:
            age = request.data['Age']
            Age = validation_check_methods.age_check(age)
            response['Age'] = Age
        if 'Phone' in request.data:
            phone = str(request.data['Phone'])
            Phone = validation_check_methods.phone_check(phone)
            response['Phone'] = Phone
        if 'Email' in request.data:
            email =str(request.data['Email'])
            Email = validation_check_methods.email_check(email)
            response['Email'] = Email
        if 'Pincode' in request.data:
            pincode = str(request.data['Pincode'])
            Pincode = validation_check_methods.pincode_check(pincode)
            response['Pincode'] = Pincode
        return Response(response)
