from dataclasses import dataclass, asdict
from enum import Enum
from typing import Optional

# class FileType(Enum):
#     CSV = "csv"
#     TXT = "txt"
#     XLSX = "xlsx"


@dataclass
class FileExport:
    """Single model for file export configuration"""
    filename: str
    filetype: str
    sql_query: str
    # db_host: str
    # db_name: str
    # db_user: str
    # db_password: str
    # db_port: int = 5432
    # query_params: Optional[dict] = None
    # overwrite_existing: bool = False

    @property
    def full_filename(self) -> str:
        """Returns filename with proper extension"""
        return f"{self.filename}.{self.filetype.value}"

    @property
    def as_json(self) -> dict:
        return asdict(self)
