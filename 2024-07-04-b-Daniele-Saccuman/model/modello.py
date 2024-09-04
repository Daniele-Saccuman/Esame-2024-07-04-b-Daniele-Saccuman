from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._listYears = []
        self._listStates = []
        self._listSightings = []
        self._grafo = nx.Graph()
        self._idMap = {}
        self._listEdges = []


    def buildGraph(self, anno, stato):
        self._listSightings = DAO.get_all_sightings(anno, stato)

        for s in self._listSightings:
            self._idMap[s.id] = s

        self._grafo.add_nodes_from(self._listSightings)
        self._archi = DAO.getAllEdges(anno, stato)

        for e in self._archi:
            S1 = self._idMap[e[0]]
            S2 = self._idMap[e[3]]
            if S1.distance_HV(S2) <100:
                self._grafo.add_edge(S1, S2)

    def get_connected_components(self):
        # Ottiene le componenti debolmente connesse del grafo
        components = list(nx.connected_components(self._grafo))
        return components

    def getYears(self):
        self._listYears = DAO.getAllYears()
        return self._listYears

    def getState(self, anno):
        self._listState = DAO.getAllStates(anno)
        return self._listState

    def getNumNodi(self):
        return len(self._grafo.nodes)

    def getNumArchi(self):
        return len(self._grafo.edges)

    def getConnectedComponents(self):
        return nx.number_connected_components(self._grafo)