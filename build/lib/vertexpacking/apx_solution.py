import gurobipy as gp
import networkx as nx

def solve_model(graph):
    #modello pli per rilassamento lagrangiamo 
    model = gp.Model()

    #Imposta il parametro OutputFlag a 0 per sopprimere l'output
    model.setParam('OutputFlag', 0)
 
    #matrice di incidenza A
    A = nx.incidence_matrix(graph, oriented=False).toarray()
    #print(A)
  
    #numero di archi e nodi
    E = graph.number_of_edges()
    V = graph.number_of_nodes()
    
    #aggiungiamo le variabili
    x = model.addVars(E, lb=0.0, ub=float('inf'), obj=1, vtype=gp.GRB.CONTINUOUS, name="x")
    
    #aggiungiamo i vincoli
    for i in range(V):
        model.addConstr((gp.quicksum(x[j]*A[i][j] for j in range(E)) >= 1), name="vincolo_{i}")

    #risoluzione del modello
    model.optimize()

    #stampa della soluzione ottima
    #print("soluzione approssimata: " + str(x))

    # Scrittura del modello su un file .lp
    #model.write("lag_model.lp")

    #restituiamo valore ottimo
    return model.ObjVal

