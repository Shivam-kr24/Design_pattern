#Singleton allows access to its instance globally. Here's an example of a Singleton Logger that provides centralized logging:
class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def log(self, message):
        print(f"Logging: {message}")

# Usage
logger = Logger()
logger.log("An important event occurred")

