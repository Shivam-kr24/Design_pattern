# Thread Safety: Singleton implementation should handle multi-threading scenarios.
#  example of a thread-safe Singleton ResourceManager using locks:
import threading

class ResourceManager:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

# Usage
resource_manager1 = ResourceManager()
resource_manager2 = ResourceManager()

print(resource_manager1 is resource_manager2)  # Outputs: True
