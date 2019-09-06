from pydantic import BaseModel
from typing import List


class TileIdx(BaseModel):
    x: int
    y: int

    def add(self, other):
        return TileIdx.parse_obj({'x': self.x + other.x, 'y': self.y + other.y})

class BriefPage(BaseModel):
    speaker: str
    dialogue: str

class ShopItem(BaseModel):
    name: str
    cost: int
    description: str

class UnitStart(BaseModel):
    unit_type: str
    relative_position: TileIdx

class Formation(BaseModel):
    spawn_points: List[TileIdx]
    units: List[UnitStart]

class LevelData(BaseModel):
    brief_setting: str
    brief_pages: List[BriefPage]
    shop_items: List[ShopItem]
    camera_center: TileIdx
    player_spawn_points: List[TileIdx]
    enemy_formations: List[Formation]
    map_name: str
