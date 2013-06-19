#from SimPy.Simulation import *
from SimPy.SimulationTrace import *

# D(t) es la demanda durante el periodo t
# d(t) es la demanda satisfecha en el periodo t
# I(t) es el nivel de stock disponible al final del periodo t
# IP(t) es la posición del stock al fin del periodo t
# Q(t) es la cantidad demandada en el periodo t.


N = 20

class Stock(Level):
    pass


class Compra(Process):
    
    def go(self):
        yield put,self,'stock',1 

# sets the software clock to 0.0
initialize()

simulate(until=N)

