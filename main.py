import requests

from data_structures.datacenter import Datacenter
from time import sleep

URL = "http://www.mocky.io/v2/5e539b332e00007c002dacbe"


def get_data(url, max_retries=5, delay_between_retries=1) -> dict:
    """
    Fetch the data from http://www.mocky.io/v2/5e539b332e00007c002dacbe
    and return it as a JSON object.

    Args:
        url (str): The url to be fetched.
        max_retries (int): Number of retries.
        delay_between_retries (int): Delay between retries in seconds.
    Returns:
        data (dict)
    """

    while max_retries:
        max_retries -= 1
        try:
            response = requests.get(url)
        except Exception as ex:
            continue

        if response.ok:
            return response.json()
        sleep(delay_between_retries)


def main():
    """
    Main entry to our program.
    """

    data = get_data(URL)
    if not data:
        raise ValueError('No data to process')

    datacenters = [
        Datacenter(key, value)
        for key, value in data.items()
    ]

    pass  # the rest of your logic here


if __name__ == '__main__':
    main()

