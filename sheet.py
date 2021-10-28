# Library imports
from typing import Any
from uuid import uuid4

# Project imports
from database import Database


class Sheet:

    _SHEET_PATH_FMT = "json//sheets//{}.json"

    def __init__(self, sheet_id: str):
        self.id = sheet_id
        self.db = Database(self._SHEET_PATH_FMT.format(sheet_id))

    @classmethod
    def new(cls) -> 'Sheet':
        sheet_id = str(uuid4())
        Database.new(cls._SHEET_PATH_FMT.format(sheet_id))
        return Sheet(sheet_id)

    def __hash__(self):
        return self.id

    def __eq__(self, other):
        if isinstance(other, Sheet):
            return other.id == self.id
        else:
            return False

    def __getitem__(self, item) -> Any:
        if item in self.db:
            return self.db[item]
        else:
            return None

    def __setitem__(self, key, value) -> None:
        self.db[key] = value

    def __contains__(self, item) -> bool:
        return item in self.db




if __name__ == "__main__":

    sheet = Sheet(0, "char100")

    pass