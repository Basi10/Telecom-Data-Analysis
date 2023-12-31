import psycopg2


class Database:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None

    def connect(self):
        self.connection = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        

    def execute_query(self, query):
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        return result

    def close_connection(self):
        if self.connection:
            self.connection.close()
            self.connection = None


