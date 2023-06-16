from pydantic import BaseModel, validator, PyObject, Field
from datetime import datetime
from typing import Union
from bson import ObjectId
class project(BaseModel):
    id: object = Field(default_factory=ObjectId, alias="_id")
    Sl_No: Union[int,str]
    Project_Timeline: str
    Client_Name: str
    Client_Alias: str
    Project_Name: str
    Industry_Type: str
    Use_Case: str
    Guideline: str
    Edge_Case: str
    Annotation_Type: str
    Data_Type: str
    Benchmark:str
    PDR: str
    Project_Charter: str
    Remarks: str

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}

@validator('Sl_No', pre=True)
def allow_none(cls, v):
    if v is None:
        return None
    else:
        return v

class startup_log(BaseModel):
    hostname: str
    startTime: datetime
    startTimeLocal: str
    cmdLine: object
    pid: int
    buildinfo: object