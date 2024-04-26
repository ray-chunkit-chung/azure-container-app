import os
import requests

# from fastapi.encoders import jsonable_encoder

BACKEND_URL = os.environ.get('BACKEND_URL', 'localhost')
PORT = os.environ.get('BACKEND_URL', 8000)


def test_true_1():
    """
    Always passes
    """
    assert True


# def test_endpoint_alive():
#     """
#     Happy path: Expect 200
#     """
#     headers = {'accept': 'application/json'}
#     response = requests.get(f'{BACKEND_URL}/:{PORT}', headers=headers)
#     content = jsonable_encoder(response.content)

#     assert response.status_code == 200
#     assert 'Nginx' in content
