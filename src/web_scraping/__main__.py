from datacleaning import DataCleaning
from datasummary import DataSummary
import pandas as pd

def main():
    # Assume you have a DataFrame df that you want to clean and summarize
    df = pd.read_csv('your_dataset.csv')  # Replace 'your_dataset.csv' with your actual dataset file

    # Data Cleaning
    cleaner = DataCleaning(df)
    cleaned_df = cleaner.feild_drop()

    # Data Summary
    summary = DataSummary(cleaned_df)

    # Display summary information
    print("Original DataFrame:")
    print(df.head())

    print("\nCleaned DataFrame:")
    print(cleaned_df.head())

    print("\nSummary:")
    print(summary.show())
    print(summary.shape())
    print(summary.usecase())
    print(summary.num_attributes())
    print(summary.data_types())
    print(summary.check_null())

if __name__ == "__main__":
    main()
