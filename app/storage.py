from threading import Lock

class MemoryStorage:
    def __init__(self):
        self._data = {}
        self._lock = Lock()

    def set(self, key: str, value: str):
        with self._lock:
            self._data[key] = value

    def get(self, key: str):
        with self._lock:
            return self._data.get(key)
