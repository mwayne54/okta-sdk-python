import aiohttp
import asyncio
import json
from okta.errors.http_error import HTTPError
from okta.errors.okta_api_error import OktaAPIError


class HTTPClient:
    """
    This class is the basic HTTPClient for the Okta Client.
    Custom HTTP clients should inherit from this class.
    """

    def __init__(self, http_config={}):
        # Get headers from Request Executor
        self._default_headers = http_config["headers"]
        # Setup oauth if available
        self._oauth = None if "oauth" not in http_config \
            else http_config["oauth"]
        # Create timeout for all HTTP requests
        self._timeout = aiohttp.ClientTimeout(
            total=http_config["requestTimeout"]
        )

    async def send_request(self, request):
        """
        This method fires HTTP requests

        Arguments:
            request {dict} -- This dictionary contains all information needed
            for the request.
            - HTTP method (as str)
            - Headers (as dict)
            - Request body (as dict)

        Returns:
            Tuple(aiohttp.RequestInfo, aiohttp.ClientResponse, JSON object)
            -- A tuple containing the request and response of the HTTP call
        """
        try:
            # Set headers
            self._default_headers.update(request["headers"])
            # Fire request
            async with aiohttp.request(
                method=request["method"],
                url=request["url"],
                headers=self._default_headers,
                data={} if "data" not in request else request["data"],
                timeout=self._timeout
            ) as response:
                return (response.request_info,
                        response,
                        await response.json(), None)
        except (aiohttp.ClientError, asyncio.exceptions.TimeoutError) as error:
            # Return error if arises
            return (None, None, None, error)

    @staticmethod
    def check_response_for_error(url, response_details, response_body):
        dict_resp = json.loads(json.dumps(response_body))
        status_code = response_details.status

        # error check
        if 200 <= status_code <= 300:
            return dict_resp, None
        else:
            # create errors
            try:
                error = OktaAPIError(url, response_details, dict_resp)
            except Exception:
                error = HTTPError(url, response_details, dict_resp)
            return None, error
