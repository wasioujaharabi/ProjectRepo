from model import project
import motor.motor_asyncio
from typing import List

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://wasiou:4B7z22thbADwmCYP@centralprojectrepo.b47wjni.mongodb.net/CentralProjectRepo")

database = client.CentralProjectRepo
collection = database.ProjectList

# async def fetch_all_projects():
#     projects = []
#     cursor = collection.find({})
#     async for document in cursor:
#         projects.append(project(**document))
#     return projects
async def fetch_all_projects():
    projects = []
    try:
        cursor = collection.find({})
        async for document in cursor:
            projects.append(project(**document))
    except Exception as e:
        # Handle the specific exception or log the error
        print(f"An error occurred while fetching projects: {e}")
        # You can also raise or return the exception if needed
        # raise e
        # return []
    finally:
        return projects

async def fetch_all_industry_types():
    industry_types = []
    try:
        cursor = collection.find({})
        async for document in cursor:
            industry_type = document.get("Industry_Type")
            if industry_type not in industry_types:
                industry_types.append(industry_type)
    except Exception as e:
        # Handle the specific exception or log the error
        print(f"An error occurred while fetching projects: {e}")
        # You can also raise or return the exception if needed
        # raise e
        # return []
    finally:
        # print(projects)
        return industry_types

async def fetch_types(Type):
    types = []
    try:
        cursor = collection.find({})
        async for document in cursor:
            type = document.get(Type)
            if type not in types:
                types.append(type)
    except Exception as e:
        # Handle the specific exception or log the error
        print(f"An error occurred while fetching projects: {e}")
        # You can also raise or return the exception if needed
        # raise e
        # return []
    finally:
        # print(projects)
        return types


async def fetch_all_client_alias():
    client_aliases = []
    try:
        cursor = collection.find({})
        async for document in cursor:
            client_Alias = document.get("Client_Alias")
            if client_Alias not in client_aliases:
                client_aliases.append(client_Alias)
    except Exception as e:
        # Handle the specific exception or log the error
        print(f"An error occurred while fetching projects: {e}")
        # You can also raise or return the exception if needed
        # raise e
        # return []
    finally:
        # print(projects)
        return client_aliases

async def fetch_project_by_name(Project_Name):
    document = await collection.find_one({"Project_Name": Project_Name})
    return document

async def fetch_projects(filters: dict) -> List[project]:
    projects = []
    query = {}
    for key, value in filters.items():
        query[key] = value
    results = collection.find(query)
    async for result in results:
        projects.append(project(**result))
    return projects

async def fetch_all_projects_by_type(Industry_Type):
    projects = []
    try:
        cursor = collection.find({"Industry_Type": Industry_Type})
        async for document in cursor:
            projects.append(project(**document))
    except Exception as e:
        # Handle the specific exception or log the error
        print(f"An error occurred while fetching projects: {e}")
        # You can also raise or return the exception if needed
        # raise e
        # return []
    finally:
        # print(projects)
        return projects

async def create_new_project(project):
    document = project
    result = await collection.insert_one(document)
    return document

async def update_project(Project_Name, data:dict):
    await collection.update_one({"Project_Name": Project_Name},{"$set":data})
    document = await collection.find_one({"Project_Name":Project_Name})
    return document


async def delete_project(Project_Name):
    await collection.delete_one({"Project_Name": Project_Name})
    return True