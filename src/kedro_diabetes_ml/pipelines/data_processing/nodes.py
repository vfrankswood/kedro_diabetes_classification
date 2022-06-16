"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.1
"""

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def get_age_scaler(diabetes_data):
    scaler = MinMaxScaler()
    scaler = scaler.fit(np.array(diabetes_data['age']).reshape((-1, 1)))
    return scaler

def preprocess_diabetes_data(diabetes_data: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses the data.

    Args:
        diabetes: Raw data.
    Returns:
        Preprocessed data, ready for split.
    """
    diabetes_data['gender'] = diabetes_data['gender'].apply(lambda x: 1 if x=='Female' else 0)
    scaler = get_age_scaler(diabetes_data)
    diabetes_data['age'] = scaler.transform(np.array(diabetes_data['age']).reshape((-1, 1)))

    return diabetes_data
