from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self.voli = []
        self.grafo = nx.DiGraph()
    def loadVoli(self, distance):
        self.voli = DAO.getAllFlights(distance)
        #print(self.voli)

    def loadAirports(self):
        listaAirports = DAO.getAllAirports()
        self.grafo.add_nodes_from(listaAirports)