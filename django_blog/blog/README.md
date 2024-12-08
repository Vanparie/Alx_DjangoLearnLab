# Django Blog Authentication System

## Features
1. **User Registration**:
   - Users can register with a username and password.
   - Implemented using Django’s `UserCreationForm`.

2. **Login & Logout**:
   - Built-in Django authentication views are used for secure login and logout.

3. **Profile Management**:
   - Authenticated users can view their profile details.
   - Access is restricted to logged-in users.

## URLs
- `/login/`: Login page.
- `/logout/`: Logout page.
- `/register/`: User registration page.
- `/profile/`: User profile page (requires login).

## Setup Instructions
1. Add `blog` to `INSTALLED_APPS` in `settings.py`.
2. Configure URLs as shown in `urls.py`.
3. Run the development server:
   ```bash
   python manage.py runserver
