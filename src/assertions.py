from requests import Response
import json
class Assertions:
    def assert_status_code(self, response: Response, expected_status_code):
        actual_status_code = response.status_code
        assert response.status_code == expected_status_code, \
            f'Unexpected status code. Expected {expected_status_code}. Actual: {actual_status_code}'

    def assert_response_is_json(self, response: Response):
        assert 'application/json' in response.headers.get('Content-Type', ''), \
            'Error: Response is not in JSON format'

    def assert_json_has_keys(self, response: Response, names: list):
        try:
            response_json = response.json()
        except json.JSONDecodeError:
            assert False, f"""Response is not JSON format. Response text is '{response.text}'"""
        for name in names:
            assert name in response_json, f"""response JSON does not have key '{name}'"""

