

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        
        return False
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except:
                pass

            return True
        
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            for v in self.adj_list[vertex]:
                self.adj_list[v].remove(vertex)

            del self.adj_list[vertex]
            return True
        
        return False



    def print_graph(self):
        for v in self.adj_list:
            print(v, ":", self.adj_lsit[v])
        
