from http.client import HTTPException
from model import project
from fastapi import FastAPI

app = FastAPI()

from database import (
    fetch_all_projects,
    fetch_project_by_name,
    fetch_all_projects_by_type,
    fetch_all_industry_types,
    fetch_all_client_alias,
    create_new_project,
    update_project,
    delete_project
)

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

@app.put("/api/ProjectList{Project_Name}/update", response_model= project)
async def put_project(Project_Name: str, data:dict):
    response = await update_project(Project_Name,data)
    if response:
        return response
    raise HTTPException(404, "Something went wrong")

@app.delete("/api/ProjectList{Project_Name}/remove")
async def delete_project_by_name(Project_Name):
    response = await delete_project(Project_Name)
    if response:
        return "Successfully Deleted Project"
    raise HTTPException(404, "There is no Project")