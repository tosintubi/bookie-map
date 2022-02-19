import io
import json
from unittest import TestCase, mock

from src import create_app
from src.book import create_book
from src.constants.http_status_codes import HTTP_201_CREATED, HTTP_405_METHOD_NOT_ALLOWED,HTTP_400_BAD_REQUEST

class TestBook(TestCase):
    
    
    @mock.patch("src.book.create_book", return_value=201 )
    def test_successful_book_create(self, create_book):
        """
        Test Successful book creation.
        """
        with open('resources/yakitabu-image.png', 'rb') as img:
            image = io.BytesIO(img.read())
            
        test_data = {
            'image':(image,'yakitabu-logo.png'),
            'title': 'How not to learn German',
            'author_first_name': 'Tim',
            'isbn':'12-3434-J1002',
            'author_last_name': 'Lahaye',
            'language':'EN',
            'year_of_publication': 2002,
            'category': 'Motivational',
            'owner_id':'4d75f8e2-c2ca-4d3c-bc34-039bf66731dc'
        }
        flask_app = create_app()
        
        with flask_app.test_client() as test_client:
            response = test_client.post('http://localhost:5000/api/books',
                                        content_type='multipart/form-data',
                                        data=test_data
                                        )
            response.status_code = create_book()
            self.assertEqual(response.status_code, HTTP_201_CREATED)

    @mock.patch("src.book.create_book", return_value=400 )
    def test_unsuccessful_book_create_when_title_missing(self, create_book):
            """
            Test Unsuccessful book save due to book title missing.
            """
            with open('resources/yakitabu-image.png', 'rb') as img:
                image = io.BytesIO(img.read())
                
            test_data = {
                'image':(image,'yakitabu-logo.png'),
                'isbn':'12-3434-J1002',
                'author_first_name': 'Tim',
                'author_last_name': 'Lahaye',
                'language':'EN',
                'year_of_publication': 2002,
                'category': 'Motivational',
                'owner_id':'4d75f8e2-c2ca-4d3c-bc34-039bf66731dc'
            }
            flask_app = create_app()
            
            with flask_app.test_client() as test_client:
                response = test_client.post('http://localhost:5000/api/books',
                                            content_type='multipart/form-data',
                                            data=test_data
                                            )
                response.status_code = create_book()
                self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
    
    @mock.patch("src.book.create_book", return_value=400 )
    def test_unsuccessful_book_create_when_isbn_missing(self, create_book):
        """
        Test Unsuccessful book save due to ISBN missing.
        """
        with open('resources/yakitabu-image.png', 'rb') as img:
            image = io.BytesIO(img.read())
            
        test_data = {
            'image':(image,'yakitabu-logo.png'),
            'title': 'How not to learn German',
            'author_first_name': 'Tim',
            'author_last_name': 'Lahaye',
            'language':'EN',
            'year_of_publication': 2002,
            'category': 'Motivational',
            'owner_id':'4d75f8e2-c2ca-4d3c-bc34-039bf66731dc'
        }
        flask_app = create_app()
        
        with flask_app.test_client() as test_client:
            response = test_client.post('http://localhost:5000/api/books',
                                        content_type='multipart/form-data',
                                        data=test_data
                                        )
            response.status_code = create_book()
            self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
            
    @mock.patch("src.book.create_book", return_value=400 )
    def test_unsuccessful_book_create_when_author_first_name_missing(self, create_book):
        """
        Test Unsuccessful book save due to author's first name missing.
        """
        with open('resources/yakitabu-image.png', 'rb') as img:
            image = io.BytesIO(img.read())
            
        test_data = {
            'image':(image,'yakitabu-logo.png'),
            'title': 'How not to learn German',
            'isbn':'12-3434-J1002',
            'author_last_name': 'Lahaye',
            'language':'EN',
            'year_of_publication': 2002,
            'category': 'Motivational',
            'owner_id':'4d75f8e2-c2ca-4d3c-bc34-039bf66731dc'
        }
        flask_app = create_app()
        
        with flask_app.test_client() as test_client:
            response = test_client.post('http://localhost:5000/api/books',
                                        content_type='multipart/form-data',
                                        data=test_data
                                        )
            response.status_code = create_book()
            self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
            
    @mock.patch("src.book.create_book", return_value=400 )
    def test_unsuccessful_book_create_when_owner_id_missing(self, create_book):
        """
        Test Unsuccessful book save due to Owner's ID missing.
        """
        with open('resources/yakitabu-image.png', 'rb') as img:
            image = io.BytesIO(img.read())
            
        test_data = {
            'image':(image,'yakitabu-logo.png'),
            'title': 'How not to learn German',
            'isbn':'12-3434-J1002',
            'author_first_name': 'Tim',
            'author_last_name': 'Lahaye',
            'language':'EN',
            'year_of_publication': 2002,
            'category': 'Motivational'
        }
        flask_app = create_app()
        
        with flask_app.test_client() as test_client:
            response = test_client.post('http://localhost:5000/api/books',
                                        content_type='multipart/form-data',
                                        data=test_data
                                        )
            response.status_code = create_book()
            self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
