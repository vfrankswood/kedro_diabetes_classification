"""
This is a boilerplate pipeline 'inference'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import preprocess_inference_data
from .nodes import make_predictions

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess_inference_data,
                inputs=["inference_data", 'age_scaler', "params:model_options"],
                outputs="preprocessed_inference_data",
                name="preprocess_inference_data_node",
            ),

            node(
                func=make_predictions,
                inputs=["model", 'preprocessed_inference_data'],
                outputs="predictions",
                name="make_predictions",
            )
        ]
    )
