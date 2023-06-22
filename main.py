from http.client import HTTPException
from model_2 import project
from fastapi import FastAPI, Query, HTTPException
from typing import Union, Optional
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import json, requests

import clickup


app = FastAPI()


origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from database import (
    fetch_all_projects,
    fetch_project_by_name,
    fetch_all_projects_by_type,
    fetch_all_industry_types,
    fetch_all_client_alias,
    create_new_project,
    update_project,
    delete_project,
    fetch_projects,
    fetch_types
)

@app.get("/favicon.ico")
def get_favicon():
    return FileResponse("./favicon.ico")

@app.get("/")
async def get_projects():

    response = await fetch_all_projects()
    return response

@app.get("/api/Industry_Types/")
async def get_all_Industry_Types():

    response = await fetch_all_industry_types()
    return response

@app.get("/api/Client_Aliases/")
async def get_all_Client_Aliases():

    response = await fetch_all_client_alias()
    return response

@app.get("/api/ProjectList/{Industry_Type}")
async def get_projects(Industry_Type):

    response = await fetch_all_projects_by_type(Industry_Type)
    return response

@app.get("/api/ProjectList/Type/{Type}")
async def get_types(Type):
    response = await fetch_types(Type)
    return response

@app.get("/api/ProjectList")
async def get_projects(
    Client_Alias: Optional[str] = Query(None),
    Industry: Optional[str] = Query(None),
    Project_Name: Optional[str] = Query(None),
    Platform: Optional[str] = Query(None),
    Tool_Type: Optional[str] = Query(None),
    PDR: Optional[int] = Query(None),
    Project_Type: Optional[str] = Query(None),
    Action_Items: Optional[str] = Query(None),
    QA_Check_Points: Optional[str] = Query(None),
    Obj_Benchmark: Optional[str] = Query(None),
    Img_Benchmark: Optional[str] = Query(None),
    Tagging_Benchmark: Optional[Union[int, str]] = Query(None),
    Deletion: Optional[Union[int, str]] = Query(None),
    Skip_Image: Optional[Union[int, str]] = Query(None),
    Update: Optional[Union[int, str]] = Query(None),
    Image_Loading: Optional[Union[int, str]] = Query(None),
    Object_Saving_Time: Optional[Union[int, str]] = Query(None),
    Video_Watch_Time: Optional[Union[int, str]] = Query(None),
    Judgement_Time: Optional[Union[int, str]] = Query(None),
    QA_Benchmark: Optional[Union[int, str]] = Query(None),
    Annotation: Optional[str] = Query(None),
    QA: Optional[str] = Query(None),
    Remarks: Optional[str] = Query(None),
):
    filters = {}
    if Client_Alias is not None:
        filters["Client_Alias"] = Client_Alias
    if Industry is not None:
        filters["Industry"] = Industry
    if Project_Name is not None:
        filters["Project_Name"] = Project_Name
    if Platform is not None:
        filters["Platform"] = Platform
    if Tool_Type is not None:
        filters["Tool_Type"] = Tool_Type
    if PDR is not None:
        filters["PDR"] = PDR
    if Project_Type is not None:
        filters["Project_Type"] = Project_Type
    if Action_Items is not None:
        filters["Action_Items"] = Action_Items
    if QA_Check_Points is not None:
        filters["QA_Check_Points"] = QA_Check_Points
    if Obj_Benchmark is not None:
        filters["Obj_Benchmark"] = Obj_Benchmark
    if Img_Benchmark is not None:
        filters["Img_Benchmark"] = Img_Benchmark
    if Tagging_Benchmark is not None:
        filters["Tagging_Benchmark"] = Tagging_Benchmark
    if Deletion is not None:
        filters["Deletion"] = Deletion
    if Skip_Image is not None:
        filters["Skip_Image"] = Skip_Image
    if Update is not None:
        filters["Update"] = Update
    if Image_Loading is not None:
        filters["Image_Loading"] = Image_Loading
    if Object_Saving_Time is not None:
        filters["Object_Saving_Time"] = Object_Saving_Time
    if Video_Watch_Time is not None:
        filters["Video_Watch_Time"] = Video_Watch_Time
    if Judgement_Time is not None:
        filters["Judgement_Time"] = Judgement_Time
    if QA_Benchmark is not None:
        filters["QA_Benchmark"] = QA_Benchmark
    if Annotation is not None:
        filters["Annotation"] = Annotation
    if QA is not None:
        filters["QA"] = QA
    if Remarks is not None:
        filters["Remarks"] = Remarks

    projects = await fetch_projects(filters)
    return projects
#     Sl_No: Optional[Union[int, str]] = Query(None),
#     Project_Timeline: Optional[str] = Query(None),
#     Client_Name: Optional[str] = Query(None),
#     Client_Alias: Optional[str] = Query(None),
#     Project_Name: Optional[str] = Query(None),
#     Industry_Type: Optional[str] = Query(None),
#     Use_Case: Optional[str] = Query(None),
#     Guideline: Optional[str] = Query(None),
#     Edge_Case: Optional[str] = Query(None),
#     Annotation_Type: Optional[str] = Query(None),
#     Data_Type: Optional[str] = Query(None),
#     Benchmark: Optional[str] = Query(None),
#     PDR: Optional[str] = Query(None),
#     Project_Charter: Optional[str] = Query(None),
#     Remarks: Optional[str] = Query(None),
# ):
#     filters = {}
#     if Sl_No is not None:
#         filters["Sl_No"] = Sl_No
#     if Project_Timeline is not None:
#         filters["Project_Timeline"] = Project_Timeline
#     if Client_Name is not None:
#         filters["Client_Name"] = Client_Name
#     if Client_Alias is not None:
#         filters["Client_Alias"] = Client_Alias
#     if Project_Name is not None:
#         filters["Project_Name"] = Project_Name
#     if Industry_Type is not None:
#         filters["Industry_Type"] = Industry_Type
#     if Use_Case is not None:
#         filters["Use_Case"] = Use_Case
#     if Guideline is not None:
#         filters["Guideline"] = Guideline
#     if Edge_Case is not None:
#         filters["Edge_Case"] = Edge_Case
#     if Annotation_Type is not None:
#         filters["Annotation_Type"] = Annotation_Type
#     if Data_Type is not None:
#         filters["Data_Type"] = Data_Type
#     if Benchmark is not None:
#         filters["Benchmark"] = Benchmark
#     if PDR is not None:
#         filters["PDR"] = PDR
#     if Project_Charter is not None:
#         filters["Project_Charter"] = Project_Charter
#     if Remarks is not None:
#         filters["Remarks"] = Remarks
#     projects = await fetch_projects(filters)
#     return projects

@app.get("/api/ProjectList{Project_Name}", response_model= project)
async def get_project_by_name(Project_Name):
    response = await fetch_project_by_name(Project_Name)
    if response:
        return response
    raise HTTPException(404, "There is no Project")


@app.post("/api/ProjectList/", response_model = project)
async def post_project(Project: project):
    response = await create_new_project(Project.dict())
    if response:
        return response
    raise HTTPException(404, "Something went wrong")


# async def put_project(Project_Name: str, data: project):
#     updated_data = data.dict(exclude_unset=True)
#     response = await update_project(Project_Name, updated_data)
#     if response:
#         return response
#     raise HTTPException(404, "Something went wrong")

@app.put("/api/ProjectList/{id}/update", response_model= project)
async def put_project(id, data: project):
    print(data)
    # Check if the project exists in the database
    # if not await project_exists(Project_Name):
    #     raise HTTPException(status_code=404, detail="Project not found")

    # Update the project
    updated_data = data.dict()

    print(updated_data)
    success = await update_project(id, updated_data)

    if success:
        # Return the updated project
        return data
    else:
        # Return an error response if the update fails
        raise HTTPException(status_code=500, detail="Failed to update the project")


@app.delete("/api/ProjectList/remove")
async def delete_project_by_name(id):
    response = await delete_project(id)
    if response:
        return response
    raise HTTPException(404, "There is no Project")

@app.post("api/ProjectList/Sync")
async def project_sync():
    list_id = None
    url = f"https://api.clickup.com/api/v2/list/{list_id}/task"
    API_KEY = clickup.API_KEY

    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Authorization': API_KEY
    }

    response = requests.request("GET", url, headers=headers, data=payload)


    existing_projects = fetch_types("Project_Name")