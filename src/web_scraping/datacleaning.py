class DataCleaning:
    def __init__(self, df):
        self.df = df
    
    def feild_drop(self):
        return self.df.drop(['keywords','video_url','description'], axis=1)