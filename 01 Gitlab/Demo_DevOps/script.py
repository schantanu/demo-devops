import socket
import pandas as pd


def get_ip_address(df):

    df["ip"] = df["website"].apply(lambda row: socket.gethostbyname(row))
    return df


if __name__ == "__main__":

    # Website dictionary
    data = {"website": ["www.google.com"]}

    # Convert to Pandas dataframe
    df = pd.DataFrame(data)

    # Get ip addresses
    df = get_ip_address(df)

    # Print dataframe
    print(df)
