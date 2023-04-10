from utils.file_utils import is_allowed_format
from models.file import File


async def get_files_by_category(category: str, user_id: str):
    files = []
    async for file in File.find({
        "user_id": user_id
    }):
        if is_allowed_format(file.name.split('.')[1], category):
            file_dict = {
                "file_id": str(file.id),
                "name": file.name,
                "size": file.size,
                "content_type": category,
                "is_favorite": file.metadata["is_favorite"],
                "is_deleted": file.metadata["is_deleted"],
                "created_at": file.metadata["created_at"],
            }
            files.append(file_dict)
    return files
