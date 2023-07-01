# HR Connect

HR Connect is a comprehensive employee management system developed using Django ORM, Django REST Framework, and PostgreSQL. It provides a user-friendly interface and API endpoints for managing employee data, conducting advanced queries, and integrating with third-party APIs. This documentation provides an overview of the project, installation instructions, usage guidelines, and other relevant information.

## Features

- Intuitive web-based interface for managing employee records
- RESTful API endpoints for CRUD operations on employee data
- Advanced queries for data analysis and reporting
- Integration with third-party APIs for additional functionality
- Swagger API documentation for easy understanding and interaction with the endpoints

## Installation

1. Clone the repository:
* git clone https://github.com/pratikranaa/HRConnect.git
2. Navigate to the project directory:
* cd hr-connect
3. Create and activate a virtual environment:
* virtualenv venv
* source venv/bin/activate
4. Install the project dependencies:
* pip3 install -r requirements.txt
5. Set up the PostgreSQL database and update the database configuration in settings.py.
6. Apply database migrations:
* python manage.py migrate
7. Start the development server:
* python manage.py runserver

## Usage

* Access the web application by visiting the provided URL, for example: `http://localhost:8000`.
* Use the provided API endpoints for performing CRUD operations on employee data.
* Refer to the Swagger API documentation for details on the available endpoints and their usage.

## Resources
1. Django Documentation
https://docs.djangoproject.com/

2. Django REST Framework Documentation
https://www.django-rest-framework.org/

3. PostgreSQL Documentation
https://www.postgresql.org/docs/

4. Swagger API Documentation
https://swagger.io/docs/


