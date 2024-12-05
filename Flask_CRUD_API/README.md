# Flask Laptop API - Testing with Postman
This API offers various endpoints to manage laptops, including adding a new laptop, retrieving all laptops, searching for a laptop by its name or number, updating a laptop by its number, and deleting a laptop by its number. Below are step-by-step instructions for testing these API endpoints using Postman.

## Start the Flask Application
To begin, run the Flask application to get the server up and running. Once the server is active, you will be able to make requests to it.

## Set Up Postman
Testing the API Endpoints
POST /laptops/add: Use this endpoint to add a new laptop to the system. You will need to send a POST request with the laptop’s details in JSON format. A successful request will return a confirmation message, while an error response will indicate missing or incorrect data.

GET /laptops: This endpoint allows you to retrieve a list of all laptops in the database. It returns the laptop records in JSON format.

GET /laptops/name/<name>: Use this endpoint to search for a laptop by its name. If the laptop exists, you will receive its details; if not, an error message will be returned indicating that the laptop was not found.

PUT /laptops/update/<laptop_number>: To update the details of an existing laptop, send a PUT request with the new data in JSON format. If the laptop number is found, the system will update the record and return a success message; otherwise, an error will be returned.

DELETE /laptops/delete/<laptop_number>: This endpoint allows you to delete a laptop by its number. A successful deletion will return a confirmation message.

Conclusion
This API simplifies laptop management by providing clear endpoints for adding, retrieving, updating, and deleting laptop records. It handles common issues such as missing fields or non-existent laptops with appropriate HTTP status codes and error messages.

By using Postman, you can easily test each endpoint. Just ensure that you provide the correct JSON payloads for POST and PUT requests, and use the appropriate URLs for GET, PUT, and DELETE operations.

By following this guide, you will be able to efficiently manage your laptop records through the API.

This version keeps the focus on the process and instructions for testing the API without the detailed examples. Let me know if you need further adjustments!

## Author
* Abdul-Majeed Saidatu

## Installation
```bash
  first, fork this repository and
  git clone https://github.com/Majeedsaida/Tech4Girls_Backend.git

  ```

## Tech Stack
* Powered by Flask (Python)
* Database: SQL
* API Testing: Postman
* Version Control: Managed with Git and hosted on GitHub
* Data Format: JSON
* Environment: Local development with Node.js 




