"""
This is a boilerplate pipeline 'inference'
generated using Kedro 0.18.1
"""
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from typing import Dict
import json

def preprocess_inference_data(inference_data: pd.DataFrame, age_scaler, parameters: Dict) -> pd.DataFrame:
    """Preprocesses the data.

    Args:
        diabetes: Raw data.
    Returns:
        Preprocessed data, ready for split.
    """
    inference_data = inference_data[parameters['features']]
    inference_data['gender'] = inference_data['gender'].apply(lambda x: 1 if x=='Female' else 0)
    inference_data['age'] = age_scaler.transform(np.array(inference_data['age']).reshape((-1, 1)))
    prep_inference_data = inference_data
    return prep_inference_data

def make_predictions(model, preprocessed_inference_data):
    predictions = model.predict(preprocessed_inference_data)
    list_predictions = predictions.tolist()
    json_predictions = json.dumps(list_predictions)
    return json_predictions