# Company Management System

This project is a **Company Management System** built with Django. It includes features to manage companies, departments, employees, and projects, with a focus on handling relationships between different entities. The project implements role-based access control, allows employees to be assigned to projects, and provides API endpoints for interacting with the data.

## Table of Contents
1. [Approach & Implementation](#approach--implementation)
2. [Setup & Running Instructions](#setup--running-instructions)
3. [Task Completion Checklist](#task-completion-checklist)
4. [Security Considerations](#security-considerations)
5. [API Documentation](#api-documentation)

---

## Approach & Implementation

The system is designed using Django, a high-level Python web framework, which provides flexibility for building dynamic websites and APIs. The key models include `Company`, `Department`, `Employee`, and `Project`. These models are related using foreign keys, and we used Django's `ManyToMany` relationship for employees working on multiple projects.

**Key Features Implemented:**
- **Company Management**: Ability to manage multiple companies with different departments.
- **Department Management**: Departments are linked to specific companies and contain employees.
- **Employee Management**: Employees are assigned to specific departments and can be linked to projects.
- **Project Management**: Projects are associated with companies, departments, and employees, with a start and end date.
- **API Endpoints**: Exposed API endpoints for interacting with the system.
- **Role-Based Access Control (RBAC)**: Access control is handled based on user roles.

### Considerations:
- **Data Relationships**: Proper relationships are set up between models to ensure data integrity.
- **Role-based Access Control**: Roles are defined to manage permissions based on the user's role in the system (e.g., admin, employee).
- **Testing**: Unit tests are written to validate the system's functionality, including the correctness of the business logic and model methods (e.g., number of employees, days employed).
- **Deployment**: Docker is used to containerize the application, making it easy to deploy in various environments.

---

## Setup & Running Instructions

### Prerequisites:
- Python 3.x or higher
- Django (version 4.0 or higher)
- Docker (optional, for deployment)

### Steps to Set Up Locally:
1. **Clone the repository**:
    ```bash
    git clone https://github.com/ahmed-new/company-management-system.git
    cd company-management-system
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Run the development server**:
    ```bash
    python manage.py runserver
    ```
    The application will be accessible at [http://localhost:8000](http://localhost:8000).

6. **Create a superuser for accessing the admin panel**:
    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to set up the superuser.

---

## Task Completion Checklist

- [x] **Set up models for `Company`, `Department`, `Employee`, and `Project`.**
- [x] **Implement relationships between models** using `ForeignKey` and `ManyToManyField`.
- [x] **Implement custom properties** for counting departments, employees, and projects.
- [x] **Create unit tests** for model methods and business logic.
- [x] **Test the system** to ensure the correctness of the functionality.
- [x] **Setup API endpoints** (if applicable).
- [x] **Dockerized the application** for deployment.
- [x] **Prepared the `README.md`** with setup instructions and documentation.

### Assumptions:
- The project is intended to manage companies, departments, employees, and projects in a way that facilitates easy management of these entities.
- The user roles and access control are implemented to allow proper access management (e.g., an admin has full control, while an employee has limited access).

---

## Security Considerations

1. **Role-Based Access Control (RBAC)**:
   - Roles are assigned to users based on their function in the organization (e.g., admin, manager, employee).
   - Access to sensitive data and actions is restricted based on roles. Admins can manage the entire system, while employees can only view or update their own data.

2. **Data Protection**:
   - Personal data such as employee email addresses and mobile numbers are protected through secure storage and appropriate access control.
   - Passwords are hashed and stored securely using Django's built-in password management system.

3. **CSRF Protection**:
   - CSRF protection is enabled by default in Django to protect against cross-site request forgery attacks.

4. **HTTPS**:
   - For production deployments, it's recommended to use HTTPS to encrypt the data transmitted between the client and server.

---

## API Documentation

This section provides documentation for the API endpoints. You can interact with the API through HTTP requests (GET, POST, PUT, DELETE).

### Base URL:

### Endpoints:
1. **GET /companies/**
   - Fetch all companies.
   - **Response**: A list of all companies with their details.

2. **POST /companies/**
   - Create a new company.
   - **Body**: JSON object with the company details.

3. **GET /companies/{id}/**
   - Fetch a single company by its ID.
   - **Response**: Details of the company.

4. **GET /departments/{company_id}/**
   - Fetch all departments for a given company.

5. **GET /employees/{department_id}/**
   - Fetch all employees in a specific department.

6. **POST /projects/**
   - Create a new project.
   - **Body**: JSON object with project details, including assigned employees.

---

### Accessing API Documentation Externally:
You can use tools like **Postman** or **Insomnia** to test the API endpoints and view responses. API documentation can also be auto-generated using tools like **Swagger** if required.

---

## Additional Information

- **Docker**: To deploy the project using Docker, you can build the Docker image and run the container with the following commands:
    ```bash
    docker build -t company-management .
    docker run -p 8000:8000 company-management
    ```

- **Deployment**: The project can be easily deployed to services like **Heroku**, **Render**, or **AWS**. Ensure that your environment variables, such as database credentials, are securely set.

---

For any additional information or questions, feel free to reach out!


