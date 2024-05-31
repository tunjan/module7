# Titanic Survival Prediction using DVC

## File Descriptions

### 1. dvc.yaml

Defines the stages of the machine learning pipeline, specifying dependencies and outputs for each stage. It ensures reproducibility and version control for data and models.

### 2. titanic.csv.dvc

This DVC file links to the actual Titanic dataset, tracking its version and storage location. It ensures the correct version of the dataset is used for training and evaluation. In this case it is stored in an AWS S3 bucket.

### 3. clean_data.py

Removes some of the columns, fills NaN values, and changes categorical columns to numerical. 

### 3. train_model.py

Trains a logistic regression model on the Titanic dataset. It includes the following key steps:

- Loading the dataset.
- Splitting the data into training and testing sets.
- Standardizing numerical features.
- Training a logistic regression model.
- Evaluating the model's accuracy.

The script takes two arguments:
- `input_path`: Path to the input CSV file containing the Titanic dataset.
- `metrics_path`: Path to the output file where the model's accuracy will be saved.

#### Usage

Create a virtual environment and install dependencies:

```sh
python3 -m venv dvc-env
source dvc-env/bin/activate
pip install -r requirements.txt
```

Download the dataset and run the pipeline:

```sh
dvc pull
dvc repro
```
