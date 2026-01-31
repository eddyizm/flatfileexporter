from dataclasses import dataclass
from datetime import datetime


@dataclass
class VersionCheck:
    version: str
    date_updated: datetime
    url: str
