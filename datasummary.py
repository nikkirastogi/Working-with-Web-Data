class summary:
    def __init__(self, df):
        """Create a object by passing in a `pandas.DataFrame` of data."""
        self.data = df
        
    # Show first 5 rows of dataframe
    def show(self):
        return self.data.head()
    
    #Check the shape of the dataframe
    def shape(self):
        return self.data.shape
    
    # Calculate the number of use cases
    def usecase(self):
        """
            Number of Use Cases: To determine the number of use cases (rows) in the dataset
        """
        return "Number of Use Cases: " , self.data.shape[0]
    

    def num_attributes(self):
        """
            Number of Attributes: To calculate the number of attributes (columns) in the dataset
        """
        return "Number of Attributes: " , self.data.shape[1]
    
    
    def data_types(self):
        """
            Data Types for Each Attribute: To display the data types of each attribute in our dataset.
        """
        print("Data Types for Each Attribute:")
        return self.data.dtypes
    
    # Check the number of null values in the columns
    def check_null(self):
        """Missing values in Dataset"""    
        return self.data.isnull().sum()