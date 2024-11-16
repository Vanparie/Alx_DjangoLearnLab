# Project Title

## Description
A brief description of the project.

# Permission and Group Setup in Django

## Custom Permissions
We added four custom permissions to the `Book` model in the `bookshelf` app:
- `can_view`: Allows users to view books.
- `can_create`: Allows users to create new books.
- `can_edit`: Allows users to edit existing books.
- `can_delete`: Allows users to delete books.

These permissions are defined in the `Meta` class of the `Book` model.

## Groups and Permissions
We created three groups with the following permissions:
- **Viewers**: Assigned the `can_view` permission.
- **Editors**: Assigned the `can_create` and `can_edit` permissions.
- **Admins**: Assigned all permissions (`can_view`, `can_create`, `can_edit`, `can_delete`).

## Views and Permissions
In the views, we use the `@permission_required` decorator to enforce these permissions:
- View book: `@permission_required('bookshelf.can_view')`
- Create book: `@permission_required('bookshelf.can_create')`
- Edit book: `@permission_required('bookshelf.can_edit')`
- Delete book: `@permission_required('bookshelf.can_delete')`

## Testing
Test the permissions by logging in as users in different groups and verifying that the permissions are correctly enforced.

## Example Setup:
1. Create and assign groups through the Django admin interface.
2. Test user access based on their group and assigned permissions.


## Security Measures Implemented

- **CSRF Protection**: All forms include `{% csrf_token %}` to prevent CSRF attacks.
- **SQL Injection Prevention**: All database queries use Django's ORM, preventing SQL injection.
- **Content Security Policy (CSP)**: CSP headers are set to limit the sources from which content can be loaded.
- **HTTPS-Only Cookies**: `CSRF_COOKIE_SECURE` and `SESSION_COOKIE_SECURE` are set to `True` to ensure cookies are sent only over HTTPS.
- **Security Headers**: The app uses security headers like `SECURE_BROWSER_XSS_FILTER`, `X_FRAME_OPTIONS`, and `SECURE_CONTENT_TYPE_NOSNIFF`.
