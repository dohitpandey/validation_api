This is the source code for a Lead Generation Validation API that is used to validate user data such as name, age, email, phone number, and pin code at the backend. The API has separate functions defined for performing checks, which can be found in the validation_check_methods.py file located at validation_api/validation_check/check/common/validation_check_methods.py.

If you wish to add a new check feature to the API, you can fork the project and add your validation check method at the end of the validation_check_methods.py file. When defining a function, it must follow a specific naming convention, with the function name being in the format "inputdata_check". Additionally, the function must accept one parameter, which is the input data, and after checking the validity of the input data, it should return either "Valid" or "Invalid".

Once you have defined your new validation check method, you will need to add an if block inside post method of views.py file, which can be found at validation_api/validation_check/check/views.py, and call the method you defined earlier within this if block.

If you are confident about the logic and code you have written, you can then make a pull request to have your changes reviewed and potentially added to the Lead Generation Validation API.

The project is hosted, and you can access the API documentation by visiting the following URL: https://lead-gen-validation-service.onrender.com/swagger/