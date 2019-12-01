import mysql.connector

class UseDatabase():
    def __init__(self, config: dict)-> None:
        self.configuration = config

    def __enter__(self)->"cursor":
        self.connection = mysql.connector.connect(**self.configuration)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, exc_trace)-> None:
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
