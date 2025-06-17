from Modelos import *
'''
#Generar modelo Gn,m de Erdös y Rényi
g = grafo_ErdosRenyi(500,600)
g.mostrar_grafo()
g.exportar_a_gv("Erdos_500.gv")
#g.dijkstra(5)
#g.exportar_dijkstra_gv(5,'Erdos_Dijkstra_30.gv')
'''


#Generar modelo Gn,p de Gilbert
#g = grafo_Gilbert(50,5)
#g.mostrar_grafo()
#g.exportar_a_gv("Gilbert300.gv")



#Generar modelo Gn Dorogovtsev-Mendes
#g = grafo_DoroMendes(50)
#g.mostrar_grafo()
#g.exportar_a_gv("Grafo_DoroMendes_500.gv")



#Generar modelo Gm,n de malla
g = grafo_Malla(20,25)
#g.mostrar_grafo()
#g.exportar_a_gv("Grafo_Malla_25.gv")


#Generar variante del modelo Gn,d Barabási-Albert
#g = grafo_BarabasiAlbert(500,10)
g.mostrar_grafo()
#g.exportar_a_gv("Grafo_Barabasi_20.gv")

nodo_inicial = g.nodos[0]

# Ejecutar Dijkstra
arbol, dist, padres = g.dijkstra(nodo_inicial)

# Exportar el camino más corto de inicio a fin
g.exportar_dijkstra_gv("Dijkstra_Geografico_50.gv", nodo_inicial, padres)





#Generar modelo Gn,r geográfico simple
#g = grafo_Geografico(400,0.2)
#g.mostrar_grafo()
#g.exportar_a_gv("Grafo_Geografico_400.gv")
#
# g.BFS(10)
#g.exportar_a_gv_algoritmo("Grafo_Geografico_BFS_500.gv")
#arbol_dfs = g.DFS_recursiva(40)
#g.exportar_arbol_dfs_a_gv(arbol_dfs,"Geografico_dfsR_500.gv")
#arbol_dfs_i = g.DFS_iterativa(10)
#g.exportar_arbol_dfs_a_gv(arbol_dfs_i, "Geografico_DFS_I_500.gv")




