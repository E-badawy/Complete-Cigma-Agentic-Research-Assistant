from fastapi import APIRouter

from app.models.library_models import CreateLibraryRequest
from app.services.library_service import LibraryService
from fastapi import UploadFile, File, Form
from typing import List

router = APIRouter(
    prefix="/libraries",
    tags=["Libraries"]
)

service = LibraryService()


@router.post("")
def create_library(request: CreateLibraryRequest):
    return service.create_library(
        request.name,
        request.folder_path
    )


@router.get("")
def list_libraries():
    return service.list_libraries()


@router.delete("/{library_name}")
def delete_library(library_name: str):
    return service.delete_library(library_name)

@router.post("/upload")
async def upload_library(
    name: str = Form(...),
    files: List[UploadFile] = File(...)
    ):
    return await service.create_library_from_upload(
        name=name,
        files=files
    )