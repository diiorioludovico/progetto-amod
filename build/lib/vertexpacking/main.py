import graph_creation  as gc
import apx_solution as aps
import pandas as pd
import opt_solution as ops
import time
import sys

V_min = 40 # min numero di nodi
V_max = 40 # max numero di nodi

V_lim = 63 # numer di nodi massimo con tutti i possibili grafi

opt_analysis = True # abilita analisi dell'ottimo del problema primale

apx_analysis = True # abilita analisi del rilassamento lagrangiano

def main():
    #inizializzazione del dizionario in cui salvare le informazioni
    dict = {'Nodes': [], 'Edges': [], 'OptSolution': [], 'ApxSolution': [], 'OptTime': [] ,'ApxTime': []}

    #calcolo del numero di iterazioni
    iterazioni = 0
    for i in range(V_min, V_max+1):
        iterazioni = iterazioni + (i*(i-1)/2)-(i-1)
    
    solved = 0

    # variazione dei valori dei nodi
    for v in range(V_min, V_max+1):
        if (v > V_lim):
            e_max = 2001
        else:
            e_max = int(v*(v-1)/2)
        #variazione dei valori degli archi
        for e in range(v-1, e_max):
            #creazione del grafo connesso
            G = gc.make_graph(v, e)
            
            if opt_analysis:
                start_time = time.perf_counter()
                #risoluzione del problema primale
                z = ops.solve_model(G)
                end_time = time.perf_counter()
                execution_opt_time = end_time - start_time
                dict['OptSolution'].append(z)
                dict['OptTime'].append(execution_opt_time)
            else: 
                dict['OptSolution'].append(0)
                dict['OptTime'].append(0)
            
            if apx_analysis:
                start_time = time.perf_counter()
                #risoluzione del problema approssimato
                L = aps.solve_model(G)
                end_time = time.perf_counter()
                execution_apt_time = end_time - start_time
                dict['ApxSolution'].append(L)           
                dict['ApxTime'].append(execution_apt_time)
            else:
                dict['ApxSolution'].append(0)           
                dict['ApxTime'].append(0)

            #aggiunta della nuova riga con le info relative al problema appena risolto
            dict['Nodes'].append(v)
            dict['Edges'].append(e)    
            
            solved = solved + 1
            percentuale = (solved / iterazioni) * 100
            sys.stdout.write(f"\rCompletamento: {solved}/{iterazioni} --> {percentuale:.2f}%")
            sys.stdout.flush()

    df = pd.DataFrame(dict)
    #print(df)

    #esportiamo i dati su un file excel
    df.to_excel('vertexpacking.xlsx')

main()