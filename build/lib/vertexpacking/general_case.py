import graph_creation 
import apx_solution
import opt_solution
import matplotlib.pyplot as plt
import networkx as nx
import time

V = 100
E = 99

def dual_bound():
    # creazione grafo
    graph = graph_creation.make_graph(V, E)

    # ricerca soluzione ideale
    start_time = time.perf_counter()
    z = opt_solution.solve_model(graph)
    end_time = time.perf_counter()
    execution_opt_time = end_time - start_time

    # ricerca bound duale
    start_time = time.perf_counter()
    l = apx_solution.solve_model(graph)
    end_time = time.perf_counter()
    execution_apx_time = end_time - start_time

    # stampa del grafo
    nx.draw(graph, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=15)
    plt.show()

    print("-------- VERTEX PACKING --------")
    print(f"| Grafo G=(V,E), |V|={V}, |E|={E}")
    print(f"| Soluzione ottima: {z}")
    print(f"| Tempo primale: {execution_opt_time}")
    print(f"| Soluzione approssimata: {l}")
    print(f"| Tempo approssimazione: {execution_apx_time}")

    # Matrice di incidenza: righe=node, colonne=archi
    #print(nx.incidence_matrix(graph, oriented=False).toarray())

dual_bound() 