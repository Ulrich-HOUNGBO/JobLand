# JobLand

JobLand is a Django-based web application. This document provides instructions on how to set up and run the project.

## Prerequisites

- Python 3.8 or higher
- pip

## Installation

1. Clone the repository:
    
    ```bash
    git clone https://github.com/Ulrich-HOUNGBO/JobLand.git
    ```
2. Create a virtual environment and activate it:
    
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install the dependencies:
    
    ```bash
    pip install -r requirements.txt
    ```
4. Create a `.env` file in the root directory of the project and add the following environment variables:
    
    ```bash
    SECRET_KEY=your_secret_key
    DEBUG=True
    ```
5. Run the migrations:
    
    ```bash
    python manage.py migrate
    ```
6. Create a superuser:
    
    ```bash
    python manage.py createsuperuser
    ```
7. Run the development server:
    
    ```bash
    python manage.py runserver
    ```
8. Open your browser and go to http://
9. To access the admin interface, go to http://localhost:8000/admin/ and log in with the superuser credentials you created in step 6.
