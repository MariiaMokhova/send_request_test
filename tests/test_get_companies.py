import requests
import pytest
from data.urls import BaseUrl
from src.assertions import Assertions
from data.credentional import AllData

class TestGetCompanies:

    url = BaseUrl()
    assertions = Assertions()
    cred = AllData()
    urls = BaseUrl()

    @pytest.mark.parametrize('status', cred.company_status)
    def test_get_companies(self, status):
        url = f'api/companies?status={status}&limit=3&offset=0'
        response = requests.get(f'{self.urls.base_url}/{url}')
        self.assertions.assert_status_code(response, expected_status_code=200)

    @pytest.mark.parametrize('status', cred.company_status)
    def test_get_companies_is_json(self, status):
        url = f'api/companies?status={status}&limit=3&offset=0'
        response = requests.get(f'{self.urls.base_url}/{url}')
        self.assertions.assert_response_is_json(response)

    @pytest.mark.parametrize('status', cred.company_status)
    def test_get_companies_has_valid_keys(self, status):
        url = f'api/companies?status={status}&limit=3&offset=0'
        response = requests.get(f'{self.urls.base_url}/{url}')
        self.assertions.assert_json_has_keys(response, self.cred.names)

    # def test_get_closed_companies_has_valid_keys(self):
    #     response = requests.get(self.url.url_closed)
    #     self.assertions.assert_json_has_keys(response, self.cred.names)
    #
    # def test_get_bankrupt_companies_has_valid_keys(self):
    #     response = requests.get(self.url.url_bankrupt)
    #     self.assertions.assert_json_has_keys(response, self.cred.names)