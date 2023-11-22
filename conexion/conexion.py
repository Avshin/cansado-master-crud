import psycopg2
class Conexion:
    def __init__(self):
        self.__con = psycopg2.connect('dbname=Sirh_prueba user=postgres host=localhost password=a')
    def getConexion(self):
        return self.__con