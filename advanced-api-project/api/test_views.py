from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Book
from django.contrib.auth.models import User


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client = APIClient()
        self.client.login(username="testuser", password="testpass")  # Authenticate the client

        # Create test data
        self.book1 = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
        self.book2 = Book.objects.create(title="Brave New World", author="Aldous Huxley", publication_year=1932)


    def test_get_book_list(self):
        response = self.client.get("/api/books_all/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_book_detail(self):
        response = self.client.get(f"/api/books_all/{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "1984")
    

    def test_create_book(self):
        data = {"title": "Fahrenheit 451", "author": "Ray Bradbury", "publication_year": 1953}
        response = self.client.post("/api/books_all/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, "Fahrenheit 451")


    def test_update_book(self):
        data = {"title": "1984 (Updated)", "author": "George Orwell", "publication_year": 1949}
        response = self.client.put(f"/api/books_all/{self.book1.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "1984 (Updated)")


    def test_delete_book(self):
        response = self.client.delete(f"/api/books_all/{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)


        
    
    

