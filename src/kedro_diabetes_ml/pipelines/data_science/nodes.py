"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.1
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from typing import Dict, Tuple
import tensorflow as tf

def split_data(data: pd.DataFrame, parameters: Dict) -> Tuple:
    X = data[parameters["features"]]
    y = data['class']

    X_train, X_temp, y_train, y_temp = train_test_split(
        X, y, test_size=parameters["test_size"]+parameters["val_size"],
        random_state=parameters["random_state"]
    )

    X_valid, X_test, y_valid, y_test = train_test_split(
        X_temp, y_temp, test_size=parameters["test_size"]/(parameters["test_size"]+parameters["val_size"]),
        random_state=parameters["random_state"])

    return X_train, X_valid, X_test, y_train, y_valid, y_test

def train_val_model(X_train, X_valid, y_train, y_valid, parameters):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(parameters["n_neurons"], activation=parameters["hidden_activation_f"]),
        tf.keras.layers.Dense(parameters["n_neurons"], activation=parameters["hidden_activation_f"]),
        tf.keras.layers.Dense(1, activation=parameters["output_activation_f"])
    ])

    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=parameters["learning_rate"]),
                  loss=tf.keras.losses.BinaryCrossentropy(),
                  metrics=parameters["metrics"])


    model.fit(X_train, y_train, batch_size=parameters["batch_size"], epochs=parameters["epochs"],
              validation_data=(X_valid, y_valid))
    return model

def test_model(model, X_test, y_test):
    test_metrics = model.evaluate(X_test, y_test)
    return test_metrics
