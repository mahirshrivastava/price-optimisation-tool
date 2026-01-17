# Price Optimization Application Setup

This `README.md` outlines the steps to set up a Python virtual environment, install Flask application dependencies, and run the application.

## 1. Virtual Environment Setup

A virtual environment isolates your project's dependencies, preventing conflicts with other Python projects.

1.  **Create a virtual environment:**
    ```bash
    python3 -m venv venv

## 2. Installing Dependencies

To install the dependecies you need to run the command:

    ```bash
    pip install -r price_optimization_tool/requirements.txt

## 3. Running the application

To run the application, use the command:

    ```bash ( open on the root directory)
    python3 main.py

## 4. Environment variables:

Need to add the environment variables in config.ini file:

- Mysql credentials

## 5. Database dependencies

We have some database dependencies in our code:

1. Once you start the application, it will automatically create the database in your mysql envrionment.
2. You need add the roles manually, direct support to add roles require admin credentials, which you need to make either registering yourself via default role as admin, or need to register manually in the database.
3. Once user and roles are created you can access the apis and create update products.
