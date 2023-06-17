from typing import Dict

import pandas as pd
import requests
from sqlalchemy import create_engine


def extract(url: str) -> Dict:
    """
    Extract data from specified URL
    :param url: the URL from where data is extracted
    :return: the extracted data as a dictionary
    """
    data = requests.get(url).json()
    return data


def transform(data: Dict) -> pd.DataFrame:
    """
    Transform data into desired structure & format

    :param data: input data to be transformed
    :return: transformed data as a pandas DataFrame
    """
    df = pd.DataFrame(data)
    print(f"Total Number of Universities in API: {len(data)}")
    df = df[df["name"].str.contains("California")]
    print(f"Number of Universities in California: {len(df)}")
    df["domains"] = [",".join(map(str, item)) for item in df["domains"]]
    df["web_pages"] = [",".join(map(str, item)) for item in df["web_pages"]]
    df = df.reset_index(drop=True)
    return df[["domains", "country", "web_pages", "name"]]


def load(data_frame: pd.DataFrame) -> None:
    """
    Load transformed data into a SQLite database

    :param data_frame: the transformed data to be loaded
    """
    disk_engine = create_engine("sqlite:///my_sqlite.db")
    data_frame.to_sql("california_universities", disk_engine, if_exists=True)


def main() -> None:
    """
    The main function to orchestrate the ETL process
    """
    API = "http://universities.hipolabs.com/search?country=United+States"
    data = extract(API)
    transformed_data = transform(data)
    load(transformed_data)


if __name__ == "__main__":
    main()
