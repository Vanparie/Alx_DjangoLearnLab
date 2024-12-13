# Social Media API

This project is a Social Media API built using Django and Django REST Framework. It provides user authentication, including registration and login functionality, with a custom user model.

---

## Setup Process

Follow these steps to set up and run the project locally:

### Prerequisites
- Python 3.8 or later
- Pip (Python package manager)
- Virtual environment tool (optional but recommended)

### Installation Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/Alx_DjangoLearnLab.git
   cd Alx_DjangoLearnLab/social_media_api


Register a User
URL: /accounts/register/
Method: POST
Request Body:
{
    "username": "testuser",
    "password": "password123",
    "email": "test@example.com",
    "bio": "Hello, world!"
}

Response:
{
    "id": 1,
    "username": "testuser",
    "email": "test@example.com",
    "bio": "Hello, world!",
    "profile_picture": null
}

Login a User
URL: /accounts/login/

Method: POST

Request Body:
{
    "username": "testuser",
    "password": "password123"
}

Response:
{
    "token": "abc123def456gh789ijk"
}


Usage: Include the token in the Authorization header for authenticated requests:
Authorization: Token abc123def456gh789ijk


Overview of the User Model
The user model is a custom implementation of Django’s AbstractUser and includes additional fields:

Username: Unique identifier for the user.
Password: Secured using Django’s built-in hashing mechanism.
Email: User's email address.
Bio: A short description or biography of the user.
Profile Picture: Optional image upload for the user's profile picture.
Followers: A many-to-many relationship allowing users to follow others.
This model is extensible and suitable for building a robust social media platform.

Author
Created by Your Name.

---

### Instructions:
1. Save this content as `README.md` in the root directory of your project.
2. Replace the placeholders:
   - `your-username` with your GitHub username.
   - `[Your Name]` with your actual name.
3. Modify or expand on sections if needed to match your specific project setup.
