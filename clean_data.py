import pandas as pd
import sys


def clean_data(input_path, output_path):
    df = pd.read_csv(input_path)
    df.columns = df.columns.str.lower()
    df = df.drop(columns=[col for col in ["cabin", "ticket", "name", "passengerid"]])
    df["age"] = df["age"].fillna(df["age"].median())
    df["sex"] = pd.Categorical(
        df["sex"], categories=["male", "female"], ordered=True
    ).codes
    df = pd.get_dummies(df, columns=["embarked"], prefix="embarked", drop_first=True)
    df = df.dropna()
    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input_path output_path")
        sys.exit(1)
    input_path, output_path = sys.argv[1], sys.argv[2]
    clean_data(input_path, output_path)
