
# Email Marketing Project

This Django-based Email Marketing project allows users to manage email campaigns, including sender management, recipient categorization, and email template creation. The project integrates with REST Framework for API functionalities and uses Knox for token-based authentication.

## Features

- **Sender Management**: Create, update, retrieve, and delete sender information.
- **Receiver Management**: Manage recipients, including creating categories for efficient targeting.
- **Email Templates**: Design and store email templates for various campaigns.
- **History Tracking**: Keep a record of sent emails for future reference.
- **Bulk Email Sending**: Send emails to multiple recipients in a single request.
- **Search Functionality**: Search for categories and manage data effectively.

## Technologies Used

- **Backend**: Django 4.2.7
- **REST API**: Django REST Framework
- **Authentication**: Django Knox
- **Database**: SQLite (for development)
- **Message Broker**: RabbitMQ (for Celery tasks)

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd email_marketing_project
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:

   ```bash
   python manage.py migrate
   ```

4. Create a superuser to access the admin interface:

   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Sender Endpoints

- `GET /sender-list/`: Retrieve all senders.
- `GET /sender-detail/<int:pk>/`: Retrieve details of a specific sender.
- `POST /sender-create/`: Create a new sender.
- `PUT /sender-update/<int:pk>/`: Update an existing sender.
- `DELETE /sender-delete/<int:pk>/`: Delete a sender.

### Receiver Endpoints

- `GET /receiver-list/`: Retrieve all receivers.
- `GET /receiver-detail/<int:pk>/`: Retrieve details of a specific receiver.
- `POST /receiver-create/`: Create a new receiver.
- `PUT /receiver-update/<int:pk>/`: Update an existing receiver.
- `DELETE /receiver-delete/<int:pk>/`: Delete a receiver.

### Template Endpoints

- `GET /templete-list/`: Retrieve all templates.
- `GET /templete-detail/<int:pk>/`: Retrieve details of a specific template.
- `POST /templete-create/`: Create a new template.
- `PUT /templete-update/<int:pk>/`: Update an existing template.
- `DELETE /templete-delete/<int:pk>/`: Delete a template.

### History Endpoints

- `GET /history-list/`: Retrieve all email sending history.
- `GET /History-detail/<int:pk>/`: Retrieve details of a specific history entry.
- `POST /History-create/`: Create a new history entry.
- `PUT /History-update/<int:pk>/`: Update an existing history entry.
- `DELETE /History-delete/<int:pk>/`: Delete a history entry.

## Celery Configuration

This project uses Celery for handling asynchronous tasks. Make sure to configure your message broker (e.g., RabbitMQ) before running the worker.

## Email Configuration

To configure email settings, you can uncomment and set up the Mailtrap or Gmail configurations in the `settings.py` file:

```python
# Example Mailtrap Configuration
EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = 'your_mailtrap_user'
EMAIL_HOST_PASSWORD = 'your_mailtrap_password'
EMAIL_PORT = '2525'

# Example Gmail Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_email_password'
```

## License

This project is licensed under the MIT License.
