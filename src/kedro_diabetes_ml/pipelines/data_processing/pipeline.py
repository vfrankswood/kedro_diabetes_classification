"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import preprocess_diabetes_data

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess_diabetes_data,
                inputs="diabetes_data",
                outputs=["preprocessed_diabetes_data", 'age_scaler'],
                name="preprocess_diabetes_data_node",
            ),
        ]
    )
