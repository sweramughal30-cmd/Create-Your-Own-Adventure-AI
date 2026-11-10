from typing import Optional
from pydantic import BaseModel
from datetime import datetime



# base
class StoryJobBase(BaseModel):
    theme:str


# res
class StoryJobResponse(BaseModel):
    job_id:str
    status:str
    created_at:datetime
    story_id:Optional[int] =None
    completed_at: Optional[datetime] = None
    error: Optional[str]  = None
    # session_id: Optional[str] = None

    class Config:
        from_attributes = True

# req
class StoryJobCreate(StoryJobBase):
    pass

