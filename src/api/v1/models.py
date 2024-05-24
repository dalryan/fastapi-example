"""Response models for API V1 endpoints"""

from pydantic import BaseModel


class Health(BaseModel):
    """API Health status"""

    status: str = "ok"
