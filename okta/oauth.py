from urllib.parse import urlencode, quote
from okta.jwt import JWT
import json


class OAuth:
    """
    This class contains the OAuth actions for the Okta Client.
    """
    OAUTH_ENDPOINT = "/oauth2/v1/token"

    def __init__(self, request_executor, config):
        self._request_executor = request_executor
        self._config = config
        self._access_token = None

    def getJwt(self):
        org_url = self._config["client"]["orgUrl"]
        client_id = self._config["client"]["clientId"]
        private_key = self._config["client"]["privateKey"]

        return JWT.create_token(org_url, client_id, private_key)

    def get_access_token(self):
        if self._access_token:
            return self._access_token

        jwt = self.getJwt()
        parameters = {
            'grant_type': 'client_credentials',
            'scope': ' '.join(self._config["client"]["scopes"]),
            'client_assertion_type':
                'urn:ietf:params:oauth:client-assertion-type:jwt-bearer',
            'client_assertion': jwt
        }

        encoded_parameters = urlencode(parameters, quote_via=quote)
        url = f"{self._client.get_base_url()}{OAuth.OAUTH_ENDPOINT}?" + \
            encoded_parameters
        request = {
            'url': url,
            'method': "POST",
            'headers': {
                'Accept': "application/json",
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        }
        # Work on handling response
        # Make max 1 retry
        req, res_details, res_json, err = self._request_executor.fire_request(
            request)

        if err:
            return None, err

        parsed_response = self._parse_response(res_details, res_json)
        self._access_token = parsed_response["access_token"]
        return self._access_token

    def clear_access_token(self):
        self._access_token = None

    def _parse_response(self, res_details, json_resp):
        dict_resp = json.dumps(json_resp)
        status_code = res_details.status

        # error check
        if 200 <= status_code <= 300:
            return dict_resp
        else:
            # create errors
            pass
