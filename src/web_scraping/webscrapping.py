import urllib.request as req
from bs4 import BeautifulSoup

class WebScrape:
    """
    A class for scraping the word of the day from dictionary.com.
    """

    def __init__(self, url):
        """
        Initialize the WebScrape object with the provided URL.

        Parameters:
        - url (str): The URL of the dictionary.com page.
        """
        self.url = url
        self.soup = None

    def get_soup(self):
        """
        Fetch the HTML content from the URL and parse it using BeautifulSoup.

        Returns:
        - BeautifulSoup: The parsed HTML content.
        """
        response = req.urlopen(self.url)
        self.soup = BeautifulSoup(response.read(), "html.parser")
        return self.soup

    def TodaysDate(self):
        """
        Extract the date of the word of the day.

        Returns:
        - dict: A dictionary containing the today's date.
        """
        date_element = self.soup.find("div", {'class': 'otd-item-headword__date'})
        todaysdate = date_element.find('time').get_text()
        return {
            "Today's Date": todaysdate
        }

    def WordOfTheDay(self):
        """
        Extract the word of the day.

        Returns:
        - dict: A dictionary containing the word of the day.
        """
        word_element = self.soup.find("div", {'class': 'otd-item-headword__word'})
        word_of_the_day = word_element.find('h1').get_text()
        return {
            "Word of the Day": word_of_the_day
        }

    def PronunciationWord(self):
        """
        Extract the pronunciation of the word.

        Returns:
        - dict: A dictionary containing the pronunciation of the word.
        """
        pronunciation_element = self.soup.find("span", {'class': 'otd-item-headword__pronunciation__text'})
        pronunciation_word = pronunciation_element.get_text(strip=True)
        return {
            "Pronunciation": pronunciation_word
        }

    def WordTypeAndMeaning(self):
        """
        Extract the part of speech and meaning of the today's word.

        Returns:
        - dict: A dictionary containing the part of speech and meaning.
        """
        pos_span = self.soup.find("span", {'class': 'luna-pos'})
        word_type = pos_span.get_text(strip=True) if pos_span else None

        word_element = self.soup.find('div', class_='otd-item-headword__pos-blocks')
        definition = None
        if word_element:
            pos_block = word_element.find("div", {"class": "otd-item-headword__pos"})
            if pos_block:
                paragraph_list = [paragraph.text for paragraph in pos_block.find_all('p')]
                definition = paragraph_list[1] if len(paragraph_list) > 1 else None

        return {
            "Parts Of Speech": word_type,
            "Word Meaning": definition
        }

    def MoreWordInfo(self):
        """
        Extract additional information about the today's word.

        Returns:
        - dict: A dictionary containing additional information about the word.
        """
        more_info = {}

        word_element = self.soup.find('div', class_='wotd-item-origin__content-full')
        if word_element:
            more_info['word'] = word_element.find('h2').get_text(strip=True)

            origin_list = word_element.find('ul')
            if origin_list:
                more_info['origin'] = [li.get_text(strip=True) for li in origin_list.find_all('li')]

        return more_info

    def ExamplesWord(self):
        """
        Extract examples of the today's word.

        Returns:
        - dict: A dictionary containing examples of the word.
        """
        examples_list = []

        word_element = self.soup.find('div', class_='wotd-item-origin__content-full')
        for ul in word_element.find_all('ul'):
            for li in ul.find_all('li'):
                examples_list.append(li.get_text(strip=True))

        return {
            "Examples": examples_list[3:]
        }
