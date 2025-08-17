# OURL - A Full-Stack URL Shortener

A complete URL shortener web application built with Python and Django. This project provides a simple, clean interface to convert long, unwieldy URLs into short, memorable links. It was developed and deployed on a cloud server, and includes a full architectural design for scaling to a distributed, global-level service.

**Live Demo:** [https://ourl.app](https://ourl.app)

## Features ✨

  * **Shorten URLs**: Convert any valid URL into a short link.
  * **Custom Short Codes**: Users can provide their own custom, memorable codes.
  * **De-duplication**: Prevents creating multiple short links for the same destination URL, ensuring consistency.
  * **Fast Redirection**: Efficiently redirects short links to their original destination.
  * **Secure**: Deployed with a Let's Encrypt SSL certificate to enable HTTPS.

-----

## System Architecture

The application was deployed using a robust, single-server architecture. Additionally, a complete design for a highly scalable, distributed system was architected to handle enterprise-level traffic.

  * **Deployed Architecture**: A monolithic Django application running on an Ubuntu cloud VM, served by Gunicorn and proxied by Nginx.
  * **Scalable Architecture Design**: A distributed system incorporating a load balancer, multiple stateless web servers, a NoSQL database (e.g., DynamoDB), a Redis caching layer, and a dedicated unique ID generation service to ensure high availability and low latency.

-----

## Tech Stack

  * **Backend**: Python, Django
  * **Database**: PostgreSQL
  * **Deployment**: Nginx, Gunicorn, Systemd, Ubuntu Server
  * **Security**: Let's Encrypt (Certbot) for SSL/HTTPS

-----

## Local Setup and Installation

To run this project on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run database migrations:**
    ```bash
    python manage.py migrate
    ```
5.  **Create a superuser for admin access:**
    ```bash
    python manage.py createsuperuser
    ```
6.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000`.
