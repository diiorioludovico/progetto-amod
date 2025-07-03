import networkx as nx
import matplotlib.pyplot as plt

def make_graph(v, e):
    # Crea un grafo casuale con v vertici e e archi
    G = nx.gnm_random_graph(v, e)

    # Matrice di incidenza: righe=node, colonne=archi
    #M = nx.incidence_matrix(G, oriented=False).toarray()
    #print(M)
    
    # Visualizzazione del grafo
    #nx.draw(G, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=15)
    #plt.show()

    #se il grafo non è connesso, ne generiamo un altro finchè non è connesso
    while not nx.is_connected(G):
        G = nx.gnm_random_graph(v, e)
    
    return G

# Esempio di utilizzo
#v = 5  # Numero di vertici
#e = 4  # Numero di archi
#grafo_casuale = make_graph(v, e)
