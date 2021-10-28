# Library imports
from typing import Dict, Any, List, Tuple
import json, time, os
from multiprocessing import Lock


class Database:

    REVISION = "__REVISION__"
    CREATED_DATE = "__CREATEDDATE__"

    def __init__(self, path):
        if not os.path.isfile(path):
            raise FileNotFoundError
        self.path = path
        self.lock = Lock()
        self._db = None
        self.reload()

    def __getitem__(self, item):
        return self._db[item]

    def __setitem__(self, key, value):
        self._db[key] = value

    def __contains__(self, x) -> bool:
        return x in self._db

    def items(self) -> List[Tuple[str, Any]]:
        return list(self._db.items())

    def values(self) -> List[Any]:
        return list(self._db.items())

    def reload(self):
        self._db = self._read()

    def commit(self):
        self._db[self.REVISION] += 1
        self._write(self._db)

    def as_dict(self) -> Dict:
        return self._db

    @classmethod
    def new(cls, path) -> 'Database':
        with open(path, "w+") as fp:
            json.dump({cls.REVISION: 1, cls.CREATED_DATE: int(time.time())}, fp=fp)
        return Database(path)

    def _read(self) -> Dict[str, Any]:
        with open(self.path, "r") as fp:
            return json.load(fp)

    def _write(self, data: Dict[str, Any]) -> None:
        self.lock.acquire(False)
        with open(self.path, "w+") as fp:
            json.dump(data, fp)
        self.lock.release()
