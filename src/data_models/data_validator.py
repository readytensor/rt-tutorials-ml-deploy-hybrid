import pandas as pd
from pydantic import BaseModel, validator
from schema.data_schema import BinaryClassificationSchema


def get_data_validator(schema: BinaryClassificationSchema, is_train: bool) -> BaseModel:
    """
    Returns a dynamic Pydantic data validator class based on the provided schema.

    Args:
        schema (BinaryClassificationSchema): An instance of BinaryClassificationSchema.

    Returns:
        BaseModel: A dynamic Pydantic BaseModel class for data validation.
    """

    class DataValidator(BaseModel):
        data: pd.DataFrame

        class Config:
            arbitrary_types_allowed = True

        @validator('data', allow_reuse=True)
        def validate_dataframe(cls, data):

            if schema.id not in data.columns:
                raise ValueError(f"ID field '{schema.id}' is not present in the given data")

            if is_train and schema.target not in data.columns:
                raise ValueError(f"Target field '{schema.target}' is not present in the given data")

            for feature in schema.features:
                if feature not in data.columns:
                    raise ValueError(f"Feature '{feature}' is not present in the given data")

            return data

    return DataValidator



def validate_data(data: pd.DataFrame, data_schema: BinaryClassificationSchema, is_train: bool) -> pd.DataFrame:
    """
    Validates the data using the provided schema.

    Args:
        data (pd.DataFrame): The data to validate.
        data_schema (BinaryClassificationSchema): An instance of BinaryClassificationSchema.
        is_train (bool): Whether the data is for training or not.

    Returns:
        pd.DataFrame: The validated data.
    """
    DataValidator = get_data_validator(data_schema, is_train)
    DataValidator(data=data)
    return data