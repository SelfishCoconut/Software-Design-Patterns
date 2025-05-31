# lock_singleton.py
import threading

class LockSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance.lock = threading.Lock()
        return cls._instance

# Access the global lock like this:
def get_global_lock():
    return LockSingleton().lock
