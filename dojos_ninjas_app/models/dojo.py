from dojos_ninjas_app.config.mysqlconnection import MySQLConnection, connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL("dojos_to_ninjas").query_db(query)
        dojos = []

        for d in results:
            dojos.append( cls(d))
        return dojos
