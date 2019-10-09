import requests
import time

from hackupc.bienebot.util import log


def execute(method, url, headers=None, params=None, data=None, allowed_statuses=None):
    """
    Execute request giving some parameters.
    :param method: Method to request.
    :param url: URL to request.
    :param headers: Request headers.
    :param params: Parameters.
    :param data: Request body.
    :param allowed_statuses: Allowed HTTP status response for avoiding retry.
    :return: JSON response.
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
                status_code = None if response is None else response.status_code,
                log.warn(f'Problem requesting URL [{url}] getting [{status_code}] status code. Number of tries: {it}')
                time.sleep(it)
        except Exception as e:
            log.exception(e)
            log.error(f'Could not request URL [{url}]. Number of tries: {it}')
            time.sleep(it)
            continue
