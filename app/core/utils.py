from typing import Type, TypeVar

from pydantic import BaseModel
from sqlmodel import SQLModel

T = TypeVar("T", bound=BaseModel)
M = TypeVar("M", bound=SQLModel)


def convert_to_schema(db_model: M, schema_class: Type[T]) -> T:
    """
    Convert a SQLModel instance to a Pydantic schema.
    
    Args:
        db_model: The SQLModel instance to convert
        schema_class: The Pydantic schema class to convert to
        
    Returns:
        An instance of the specified schema class
    """
    return schema_class.model_validate(db_model.model_dump())


def convert_list_to_schema(db_models: list[M], schema_class: Type[T]) -> list[T]:
    """
    Convert a list of SQLModel instances to a list of Pydantic schemas.
    
    Args:
        db_models: List of SQLModel instances to convert
        schema_class: The Pydantic schema class to convert to
        
    Returns:
        A list of instances of the specified schema class
    """
    return [convert_to_schema(model, schema_class) for model in db_models] 