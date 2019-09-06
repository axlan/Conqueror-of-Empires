from pydantic import BaseModel
from typing import List


class TileIdx(BaseModel):
    x: int
    y: int

class BriefPage(BaseModel):
    speaker: str
    dialogue: str

class ShopItem(BaseModel):
    name: str
    cost: int
    description: str

class LevelData(BaseModel):
    brief_setting: str
    brief_pages: List[BriefPage]
    shop_items: List[ShopItem]
    camera_center: TileIdx
    spawn_points: List[TileIdx]
    map_name: str
