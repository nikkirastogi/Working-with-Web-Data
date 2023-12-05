import requests
import pandas as pd

class APIDataFetch:
    """
    A class for fetching data from an API using the requests library and converting it to a Pandas DataFrame.
    """
    def __init__(self, base_url):
        """
        Create an object by passing in a `url and api key` for data.
        
        """
        # Reading the API key
        api_key = 'pub_331919af4c2a25bb759ef095c96b1f3706e05'
        
        self.base_url = base_url

    def make_request(self):
        """
        Sends a GET request to the API using the provided base URL.

        Returns:
        - If the request is successful (status code 200), returns the JSON content of the response.
        - If the request is unsuccessful, prints an error message with the status code and response text,
          and returns None.
        """
        response = requests.get(self.base_url)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error {response.status_code}: {response.text}")
            return None

    def fetch_data(self):
        """
        Fetches data from the API using make_request() and converts it to a Pandas DataFrame.

        Returns:
        - If data is successfully retrieved and converted to a DataFrame, returns the DataFrame.
        - If there is an issue with the API request or the data cannot be converted, returns None.

        """
        data = self.make_request()

        if data:
            df = pd.DataFrame(data['results'])
            # Clean and process the DataFrame if needed
            return df
        else:
            return None
