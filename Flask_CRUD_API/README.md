# Flask Laptop API - Testing with Postman
This Flask Laptop API provides a set of endpoints to efficiently manage laptop records. You can add new laptops, retrieve all laptops, search for laptops by name or number, update laptop details, and delete laptops—all through simple HTTP requests. Below are the step-by-step instructions for testing these API endpoints using Postman.

![alt text](image-2.png)

* Running the Flask Application
To get started, launch the Flask application by running the server. Once the server is live, you can begin making requests to the API endpoints.

Setting Up Postman for Testing
Postman is a popular tool for testing APIs by sending HTTP requests and analyzing responses. Below are the specific endpoints you can test:

1. POST /laptops/add
This endpoint allows you to add a new laptop to the system. Send a POST request with the laptop’s details in JSON format. If successful, the API will return a confirmation message. If any required data is missing or incorrect, the system will respond with an error.

2. GET /laptops
Use this endpoint to retrieve a list of all laptops stored in the database. The response will be in JSON format, containing the details of each laptop.

3. GET /laptops/name/<name>
This endpoint allows you to search for a laptop by its name. If the laptop is found, it will return its details in JSON format. If the laptop does not exist, an error message will indicate that the search returned no results.

4. PUT /laptops/update/<laptop_number>
To update an existing laptop’s details, send a PUT request with the new information in JSON format. If the laptop number is found in the system, the record will be updated, and the API will return a success message. If the laptop number does not exist, you will receive an error response.

5. DELETE /laptops/delete/<laptop_number>
This endpoint allows you to delete a laptop by its number. If the laptop is successfully deleted, the API will return a confirmation message. If the laptop number is not found, an error will be returned.

Conclusion
This API simplifies the process of managing laptop records, offering clear and straightforward endpoints for adding, retrieving, updating, and deleting laptops. It handles common errors like missing data or non-existent records with appropriate HTTP status codes and error messages.

By using Postman, you can easily test these endpoints by providing the correct JSON payloads for POST and PUT requests, and using the appropriate URLs for GET, PUT, and DELETE operations.

Following this guide, you will be able to effectively manage your laptop records through the API.

## Author
Abdul-Majeed Saidatu

## Tech Stack
* Backend Framework: Flask (Python)
* Database: SQL
* API Testing Tool: Postman
* Version Control: Git, hosted on GitHub
* Data Format: JSON
* Development Environment: Local development with Node.js

## Installation Instructions
```bash
First, fork this repository, then clone it locally:
git clone https://github.com/Majeedsaida/Tech4Girls_Backend.git

````

 