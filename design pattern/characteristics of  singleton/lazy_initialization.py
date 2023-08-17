# Lazy Initialization:Singleton instances are created only when they are needed.
# Here's an example of a Singleton Configuration that loads configuration settings lazily:
class Configuration:
    _instance = None
    loaded = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def load(self):
        if not self.loaded:
            print("Loading configuration settings")
            self.loaded = True

# Usage
config = Configuration()
config.load()  # Configuration settings are loaded
config.load()  # Configuration settings are not reloaded
