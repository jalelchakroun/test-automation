# -*- coding: utf-8 -*-
from src.services.user_fetcher_service import UserFetcherService
from src.services.user_service import UserService

import collections

def test_list_user_service_ids(monkeypatch):
    # we define a function that will replace the existing function
    # instead of calling the mocked server, we use a controlled dataset
    def mock_get_user(*args):
        return [
            {'id': 'aaa-001', 'email': 'toto@gmail.com'},
            {'id': 'aaa-002', 'email': 'TATA@gmail.com'},
        ]

    monkeypatch.setattr(UserFetcherService, 'get_users', mock_get_user)

    user_service = UserService(user_fetcher_service=UserFetcherService())
    users = user_service.list_users()

    assert users ==  [
            {'id': 'aaa-001', 'email': 'toto@gmail.com'},
            {'id': 'aaa-002', 'email': 'tato@gmail.com'},
        ]

