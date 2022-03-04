from typing import Any

class Singleton(type):
    _intances = {}
    def __call__(self, cls: Any, *args: Any, **kwds: Any) -> Any:
        if cls not in cls._intances:
            cls._intances[cls] = super(Singleton, cls).__call__(*args, **kwds)
        return cls._intances[cls]
