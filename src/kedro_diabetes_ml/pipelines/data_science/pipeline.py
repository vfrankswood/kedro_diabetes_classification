"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import split_data
from .nodes import train_val_model
from .nodes import test_model

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=split_data,
                inputs=["preprocessed_diabetes_data", "params:model_options"],
                outputs=["X_train", "X_valid", "X_test", "y_train", "y_valid", "y_test"],
                name="split_data_node",
            ),

            node(
                func=train_val_model,
                inputs=["X_train", "X_valid", "y_train", "y_valid", "params:model_options"],
                outputs="model",
                name="train_val_model_node",
            ),

            node(
                func=test_model,
                inputs=["model", "X_test", "y_test"],
                outputs="test_metrics",
                name="test_model_node",
            ),

        ]
    )
