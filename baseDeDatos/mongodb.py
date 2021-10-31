import pymongo
from clases.cliente import *
from clases.restaurante import *
class MongoDB:
    def __init__(self):
        #si la ip no conecta, conectarse a localhost
        self.mongo_host = "localhost"
        self.mongo_puerto = "27017"
        self.mongo_fuera = 1000
        self.mongo_uri = "mongodb://"+self.mongo_host+":"+self.mongo_puerto+"/"
        self.mongo_basedatos = "Restaurantes"
        self.mongo_coleccion = "visitas"
        try:
            self.cliente = pymongo.MongoClient(self.mongo_uri,serverSelectionTimeoutMs=self.mongo_fuera)
            self.baseDatos = self.cliente[self.mongo_basedatos]
            self.coleccion = self.baseDatos[self.mongo_coleccion]
            print("conexion exitosa con mongo")
        except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
            print("Tiempo exedido " + errorTiempo)
        except pymongo.errors.ConnectionFailure as errorConexion:
            print("Fallo al conectarse a mongodb " + errorConexion)

    def guardar(self, cliente: 'Cliente',restaurante:'Restaurante'):
        restauranteDocumento = {
            "nombre":restaurante.nombre,
            "telefono":restaurante.telefono,
            "ubicacion":restaurante.ubicacion

        }
        clienteDocumento = {
          "nombre":cliente.nombre,
          "telefono":cliente.telefono,
          "comentario":cliente.comentario,
          "ubicacion":cliente.ubicacion,
          "calificacion":cliente.calificacion,
          "restaurante":restauranteDocumento

        }
        self.coleccion.insert(clienteDocumento)