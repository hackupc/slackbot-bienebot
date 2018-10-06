import requests
import time

from hackupc.bienebot.util import log


def execute(method, url, headers=None, params=None, data=None, allowed_statuses=None):
    """
    Execute request giving some parameters
    :param method: method to request
    :param url: url to request
    :param headers: request headers
    :param params: parameters
    :param data: request body
    :param allowed_statuses: allowed HTTP status response for avoiding retry
    :return: json response
    """
    if allowed_statuses is None:
        allowed_statuses = {}

    # Check method
    if method not in ('GET', 'POST', 'PUT', 'PATCH', 'DELETE'):
        log.error('Indicated method must be GET, POST, PUT, PATCH or DELETE')
        return None

    # Iterate until six times
    for it in range(1, 6):
        try:
            response = requests.request(method=method, url=url, headers=headers, params=params, data=data, timeout=15)
            if response is not None and (response.ok or response.status_code in allowed_statuses):
                return response.json()
            else:
                log.warn('Problem requesting URL [{url}] getting [{code}] status code. Number of tries: {i}'.format(
                    url=url,
                    code=None if response is None else response.status_code,
                    i=it))
                time.sleep(it)
        except Exception as e:
            log.exception(e)
            log.error('Could not request URL [{}]. Number of tries: {}'.format(url, it))
            time.sleep(it)
            continue
