from typing import List, Optional

from app.models.common import DateTimeModelMixin, IDModelMixin
from app.models.domain.profiles import Profile
from app.models.domain.rwmodel import RWModel
from pydantic import validator

class Item(IDModelMixin, DateTimeModelMixin, RWModel):
    slug: str
    title: str
    description: str
    tags: List[str]
    seller: Profile
    favorited: bool
    favorites_count: int
    image: Optional[str]
    body: Optional[str]

    class Config:
        validate_assignment = True

    @validator('image')
    def set_image(cls, image):
        return image or '/placeholder.png'