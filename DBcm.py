import mysql.connector


class ConnectionError(Exception):
    pass

class CredentialsError(Exception):
    pass

class SQLError(Exception):
    pass


class UseDatabase():
    def __init__(self, config: dict)-> None:
        self.configuration = config

    def __enter__(self)->"cursor":
        try:           
            self.connection = mysql.connector.connect(**self.configuration)
            self.cursor = self.connection.cursor()
            return self.cursor
        except mysql.connector.errors.InterfaceError as err:
            raise ConnectionError(err)
        except mysql.connector.errors.ProgrammingError as err:
            raise CredentialsError(err)

    def __exit__(self, exc_type, exc_value, exc_trace)-> None:
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
        if exc_type is mysql.connector.errors.ProgrammingError:
            raise SQLError(exc_value)
        elif exc_type:
            raise exc_type(exc_value)

