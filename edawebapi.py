import pandas as pd
import matplotlib.pyplot as plt

class EDAWebAPI:
    """
    A class for performing exploratory data analysis on a DataFrame using pandas and matplotlib.
    """

    def __init__(self, df):
        """
        Initialize the EDAWebAPI object with a DataFrame.

        Parameters:
        - df (pd.DataFrame): The DataFrame for analysis.
        """
        self.df = df

    def data_info(self):
        """
        Display information about the DataFrame.

        Returns:
        - None
        """
        return self.df.info()

    def creator_count(self):
        """
        Count the occurrences of each creator in the DataFrame.

        Returns:
        - A Series with creator counts.
        """
        return self.df["creator"].value_counts()

    def creator_bargraph(self):
        """
        Plot a bar graph of creator counts in the DataFrame.

        Returns:
        - The bar graph of creator counts.
        """
        return self.df["creator"].value_counts().plot.bar(title="creators")

    def source_count(self):
        """
        Count the occurrences of each source_id in the DataFrame.

        Returns:
        - A Series with source_id counts.
        """
        return self.df["source_id"].value_counts()

    def source_bargraph(self):
        """
        Plot a bar graph of source_id counts in the DataFrame.

        Returns:
        -The bar graph of source_id counts.
        """
        return self.df["source_id"].value_counts().plot.bar(title="source_id")
