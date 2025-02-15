# Issue Tracker Application

## Introduction

The Issue Tracker Application is a simple yet efficient issue management system built using the Zango framework. It allows users to create, update, assign, and track issues seamlessly.

## Features

### Core Features

- **User Authentication**
  - User registration and login.
  - Utilizes Zango's built-in authentication system.
- **Issue Management**
  - Create issues with a title, description, status, and assignee.
  - Status options: `Open`, `In Progress`, and `Resolved`.
  - Users can update issue statuses.
  - Timestamp tracking for creation and updates.
  - Assign issues to specific users.

## Installation & Setup

### Prerequisites

Ensure you have the following installed:

- **Python 3.8+**
- **PostgreSQL**
- **Docker & Docker Compose** (for containerization)

### Clone the Repository

```bash
git clone https://github.com/Raju1422/Zango_Issue_Tracker_Application---Assignment.git
cd Zango_Issue_Tracker_Application---Assignment
```

### Setting Up a Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### Install Zango

```bash
pip install Zango
```

### PostgreSQL Database Setup

- **Pull the Postgres Docker Image:**

  ```bash
  docker pull postgres
  ```

- **Create a Docker Volume:**

  ```bash
  docker volume create postgres_data
  ```

- **Run the Postgres Docker Container:**

  ```bash
  docker run --name postgres_container -e POSTGRES_PASSWORD=mypassword -d -p 5432:5432 -v postgres_data:/var/lib/postgresql/data postgres
  ```

### Redis setup

Redis is used as a broker by Celery workers. Use the steps below to run Redis on your local machine:

- **Start Redis inside a Docker container on port 6379:**

  ```bash
  docker run --name zango_redis -d -p 6379:6379 redis
  ```

### Starting the Celery Worker and Celery Beat

- **To start the Celery worker:**

  ```bash
  celery -A IssueTrackerApplication worker -l INFO
  ```

- **To start Celery Beat:**

  ```bash
  celery -A IssueTrackerApplication beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
  ```

### Running the Development Server

1. **Navigate to your project directory:**

   ```bash
   cd IssueTrackerApplication
   ```

2. **Start the development server:**

   ```bash
   python manage.py runserver
   ```

   This command will start the development server, and you'll see output indicating that the server is running. By default, the server will be available at [http://localhost:8000/](http://localhost:8000/).

### Access Your Project's App Panel

To access the app panel, go to [http://localhost:8000/platform](http://localhost:8000/platform) and enter the platform username and password that you entered while creating the project.

```bash
username: santosh@gmail.com
password: Sanju@169
```

### Setting App Domain

1. **Open a new terminal window.**
2. **Run the below command to open `/etc/hosts` file on macOS or Linux:**

   ```bash
   sudo nano /etc/hosts
   ```

3. **Paste the following line in the file:**

   ```bash
   0.0.0.0  issuemanagement.com
   ```

4. **Save and exit the editor.**

### Creating a User

- Navigate to `apps/IssueManagement/user_management` and click on `New User` to create a new user.

### Accessing IssueManagement App

- **Enter the following URL in your browser:**

  ```bash
  http://issuemanagement.com:8000/issues/all/
  ```

- **Enter your credentials that you created in user management.**
- **Perform actions like creating an issue and updating the status of an issue, etc.**

### NOTE

- The application has been **Dockerized**, but currently, the **Celery container is throwing an error**.
### Complete working of IssueTrackerApplication 
https://github.com/user-attachments/assets/2a99318e-0be1-47e7-a7fd-d7555d5b801b
