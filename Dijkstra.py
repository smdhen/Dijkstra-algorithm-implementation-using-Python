# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 22:00:35 2022

@author: HENNANI
"""
import math

# Data Representation:
# J'ai utilisé la matrice d'adjacence d'un graphe. Tous les poids doivent être >= 0.

# math.inf:
# Si on n'a pas d'arc entre deux sommets d'un graphe.

# 0:
# La distance entre un sommet et lui-même est de 0.

# Poids > 0 et différent de l'infini: (un poid >0 et != inf )
# Le poids de l'arc reliant deux sommets.

# graph={'A':[0,3,5,math.inf,math.inf,math.inf],
#        'B':[math.inf,0,1,10,math.inf,math.inf],
#        'C':[math.inf,math.inf,0,math.inf,3,math.inf],
#        'D':[math.inf,math.inf,math.inf,0,math.inf,4],
#        'E1':[math.inf,math.inf,math.inf,math.inf,0,2],
#        'f':[math.inf,math.inf,math.inf,math.inf,math.inf,0]}

graph={ 'S':[0,5,math.inf,1,math.inf,math.inf],
        'A':[math.inf,0,1,math.inf,2,math.inf],
        'B':[math.inf,math.inf,0,math.inf,1,4],
        'C':[math.inf,2,2,0,5,math.inf],
        'D':[math.inf,math.inf,math.inf,math.inf,0,2],
        'E':[math.inf,math.inf,math.inf,math.inf,math.inf,0]}



sommets_examines = []  # les sommets déjà examinés
pred = {}  # la trace pour garder le prédécesseur de chaque sommet examiné
séquence = []  # dans ce tableau va contenir le chemin optimal à la fin
distances_min = []  # les distances minimales entre les sommets du graphe
#**********************************************************************************


def min(distances_min_,sommets_examines_):
    m=math.inf
    h=0
    for i in range(1,len(distances_min_)):
        if distances_min_[i]> 0 and  m>distances_min_[i]  :
            if i not in sommets_examines_:
                m=distances_min_[i]
                h=i       
    return m,h


    # current_vertex_index : Il représente l'indice du sommet actuel avec lequel on travaille dans l'algorithme Dijkstra.

    # cumulative_cost : C'est le coût cumulé pour atteindre un sommet spécifique à partir du sommet initial en passant par d'autres sommets. Il est mis à jour si un chemin plus court est trouvé via un sommet courant.

    # current_vertex_id : C'est l'identifiant du sommet actuel avec lequel on travaille dans l'algorithme. Il est utilisé pour accéder aux informations de distance depuis ce sommet.


#**********************************************************************************
def dijkstra():# la fonction principal 
    global distances_min

    distances_min=graph[list(graph.keys())[0]]
  
    pred[list(graph.keys())[min(distances_min,sommets_examines)[1]]]=[list(graph.keys())[0]]
    
    print(distances_min)
    
    lenght_=len(graph)-1 
    
    for i in range(1,lenght_):
    
        current_vertex_index=min(distances_min,sommets_examines)[1]
      
        sommets_examines.append(current_vertex_index)
     
        current_vertex_id=list(graph.keys())[current_vertex_index]
    
        for j in range(lenght_+1):
          
            if graph[current_vertex_id][j]>0 and graph[current_vertex_id][j]!=math.inf :  
            
                cumulative_cost=graph[current_vertex_id][j]+distances_min[current_vertex_index]
             
                if cumulative_cost<distances_min[j]:
                
                    distances_min[j]=cumulative_cost
                    
                    pred[list(graph.keys())[j]]=[list(graph.keys())[current_vertex_index]]
        
        print(distances_min)

#*******************************recuperer la séquence de chemin opti******************************
#séquence
    séquence=[list(pred.keys())[-1],pred[list(pred.keys())[-1]][0]]
    
    for i in range(2,len(pred)):
    
        séquence.append(pred[séquence[i-1]][0])  # recuperer le chemin optimale 
        
    print('la lamgeur de plus cours chemin est :',distances_min[-1])
    
    for i in range(len(séquence),0,-1):# affichage 
    
        print('->',end="")
        
        print(séquence[i-1],end="")
        
#******************************************************************************

        
dijkstra()
