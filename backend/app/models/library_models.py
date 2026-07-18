from pydantic import BaseModel


class CreateLibraryRequest(BaseModel):
    name: str
    folder_path: str