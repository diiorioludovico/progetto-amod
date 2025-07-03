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
    x = model.addVars(V, lb=0.0, ub=1.0, obj=1, vtype=gp.GRB.BINARY, name="x")
    
    #aggiungiamo i vincoli
    for i in range(E):
        model.addConstr((gp.quicksum(x[j]*A[j][i] for j in range(V)) <= 1), name=f"vincolo_{i}")

    #definiamo PL di massimizzazione
    model.ModelSense = gp.GRB.MAXIMIZE

    #risoluzione del modello
    model.optimize()

    #stampa della soluzione ottima
    #print("soluzione ottima: " + str(x))

    # Scrittura del modello su un file .lp
    #model.write("primal_model.lp")

    #restituiamo valore ottimo
    return model.ObjVal

