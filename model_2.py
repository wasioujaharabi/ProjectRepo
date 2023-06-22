from pydantic import BaseModel, validator, PyObject, Field
from datetime import datetime
from typing import Union
from bson import ObjectId
class project(BaseModel):
    id: object = Field(default_factory=ObjectId, alias="_id")
    Client_Alias: str
    Industry: str
    Project_Name: str
    Platform: str
    Tool_Type: str
    PDR: int
    Project_Type: str
    Action_Items: str
    QA_Check_Points: str
    Obj_Benchmark: str
    Img_Benchmark: str
    Tagging_Benchmark: Union[int, str]
    Deletion: Union[int, str]
    Skip_Image: Union[int, str]
    Update: Union[int, str]
    Image_Loading: Union[int, str]
    Object_Saving_Time: Union[int, str]
    Video_Watch_Time: Union[int, str]
    Judgement_Time: Union[int, str]
    QA_Benchmark: Union[int, str]
    Annotation: str
    QA: str
    Remarks: str

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}
        arbitrary_types_allowed = True

@validator('Sl_No', pre=True)
def allow_none(cls, v):
    if v is None:
        return None
    else:
        return v
