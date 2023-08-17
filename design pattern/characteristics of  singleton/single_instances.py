class DatabaseConnection:    #Single Instance:-The Singleton pattern ensures that only one instance of the class is created.
                             #  example of a Singleton implementation of a DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.initialize()  # Simulate database connection setup
        return cls._instance

    def initialize(self):
        print("Initializing database connection")

# Usage
db_conn1 = DatabaseConnection()
db_conn2 = DatabaseConnection()

print(db_conn1 is db_conn2)  # Outputs: True
