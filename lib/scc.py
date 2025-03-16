from internal_scc import _SCC_graph as internal

class SCC_graph:
    def __init__(self, n):
        self._n = n
        self._scc_graph = internal(n)
    
    def add_edge(self, frm, to):
        assert 0 <= frm < self._n
        assert 0 <= to < self._n
        self._scc_graph.add_edge(frm, to)
    
    def scc(self):
        return self._scc_graph.scc()
