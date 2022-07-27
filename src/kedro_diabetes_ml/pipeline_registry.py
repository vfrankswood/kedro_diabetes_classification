"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline

from kedro_diabetes_ml.pipelines import data_processing as dp
from kedro_diabetes_ml.pipelines import data_science as ds
from kedro_diabetes_ml.pipelines import inference as inf


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipeline.

    Returns:
    A mapping from a pipeline name to a ``Pipeline`` object.

    """
    data_processing_pipeline = dp.create_pipeline()
    data_science_pipeline = ds.create_pipeline()
    inference_pipeline = inf.create_pipeline()

    return {
        "__default__": data_processing_pipeline + data_science_pipeline,
        "dp": data_processing_pipeline,
        "ds": data_science_pipeline,
        'inference': inference_pipeline
    }
