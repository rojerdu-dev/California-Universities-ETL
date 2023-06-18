import sqlite3
from typing import Dict

import pandas as pd
import requests


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
    conn = sqlite3.connect("my_db.db")
    cursor = conn.cursor()

    create_table_query = """ 
        CREATE TABLE IF NOT EXISTS california_universities ( 
            domains TEXT, 
            country TEXT,
            web_pages TEXT,
            name TEXT
    )
    """
    cursor.execute(create_table_query)

    insert_query = "INSERT INTO california_universities \
    (domains, country, web_pages, name) VALUES(?, ?, ?, ?)"
    values = data_frame.values.tolist()

    cursor.executemany(insert_query, values)

    conn.commit()
    conn.close()


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
