# -*- coding: utf-8 -*-
from src.services.book_fetcher_service import BookFetcherService
from src.services.book_service import BookService

import collections

def test_list_authors(monkeypatch):
    def mock_get_books(*args):
        return [
            { 'id': 'aaa-001', 'name': 'Origine', 'author': { 'firstname':'Dan', 'lastname': 'Brown' }},
            { 'id': 'aaa-002', 'name': 'Anges & démons', 'author': { 'firstname': 'Dan', 'lastname': 'Brown' }},
            { 'id': 'aaa-002', 'name': 'Anges & démons', 'author': { 'firstname': 'Dann', 'lastname': 'Boy' }},
        ]

    monkeypatch.setattr(BookFetcherService, 'get_books', mock_get_books)

    book_service = BookService(book_fetcher_service=BookFetcherService())
    authors = book_service.list_books_authors()

    assert collections.Counter(authors) == collections.Counter(['Brown Dan', 'Boy Dann'])
