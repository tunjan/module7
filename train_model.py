import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score


def train_model(input_path, metrics_path):
    df = pd.read_csv(input_path)

    X = df.drop(columns=["survived"])

    y = df["survived"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1
    )

    scaler = StandardScaler()
    X_train[["fare", "age"]] = scaler.fit_transform(X_train[["fare", "age"]])
    X_test[["fare", "age"]] = scaler.transform(X_test[["fare", "age"]])

    model = LogisticRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    with open(metrics_path, "w") as f:
        f.write(f"accuracy: {accuracy}\n")


if __name__ == "__main__":
    import sys

    train_model(sys.argv[1], sys.argv[2])
