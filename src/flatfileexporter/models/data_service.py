from dataclasses import dataclass, asdict


@dataclass
class DatabaseConnectionTest:
    """Store database connection test response"""
    message: str
    success_response: bool

    @property
    def as_json(self) -> dict:
        return asdict(self)
