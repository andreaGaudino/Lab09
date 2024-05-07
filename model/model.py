from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self.voli = []
        self.grafo = nx.Graph()
    def loadVoli(self, distance):
        self.voli = []
        self.grafo = nx.Graph()
        self.voli = DAO.getAllFlights()
        self.loadAirports()
        allVoli = {}
        #print(len(self.voli))
        # for volo in self.voli:
        #     self.grafo.add_edge(volo.origin_airport_id, volo.destination_airport_id, distanza=volo.distance)
        for volo in self.voli:
            if (volo.origin_airport_id, volo.destination_airport_id) in allVoli:
                #lista = allVoli[(volo.origin_airport_id, volo.destination_airport_id)]
                allVoli[(volo.origin_airport_id, volo.destination_airport_id)].append(volo.distance)
            elif (volo.destination_airport_id, volo.origin_airport_id) in allVoli:
                allVoli[(volo.destination_airport_id, volo.origin_airport_id)].append(volo.distance)
            else:
                allVoli[(volo.origin_airport_id, volo.destination_airport_id)] = [volo.distance]
        for elem in allVoli:
            media =  sum(allVoli[elem])/len(allVoli[elem])
            if sum(allVoli[elem])/len(allVoli[elem]) >= distance:
                self.grafo.add_edge(elem[0], elem[1], media = media)





    def loadAirports(self):
        listaAirports = DAO.getAllAirports()
        for i in listaAirports:
            self.grafo.add_node(i._id)