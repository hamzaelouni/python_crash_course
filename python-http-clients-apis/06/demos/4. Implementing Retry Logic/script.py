import logging
import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import RetryError
from urllib3.util.retry import Retry

# Set the basic config for the logging
logging.basicConfig(level=logging.DEBUG)
requests_log = logging.getLogger("urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

# Create a session object
session = requests.Session()

# Set the retries for the session
# total: total number of retries
# backoff_factor: factor to multiply the backoff time
# status_forcelist: list of status codes to force a retry
# allowed_methods: list of methods to allow retries for
retries = Retry(total=3, backoff_factor=0.1, status_forcelist=[500], allowed_methods={"GET"})
session.mount("http://127.0.0.1", HTTPAdapter(max_retries=retries))

# Or you can just use an integer instead of the Retry object to set the total number of retries
# session.mount("http://127.0.0.1", HTTPAdapter(max_retries=3))

try:
    # Flaky endpoint is a route that randomly fails or succeeds
    response = session.get("http://127.0.0.1:8000/flaky")
    print("Final response status:", response.status_code)
except RetryError:
    print("Maximum retries exceeded. Server is not available.")