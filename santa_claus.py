#Travail fait par Jérémias Sherwin et Dubord Ruben. BUT INFO 1, Boréas.


from time import time
from math import *
from numpy import *
from random import *


##############
# SAE S01.01 #
##############

def nb_villes(villes):
    """Retourne le nombre de villes"""
    return len(villes)//3


def noms_villes(villes):
    """Retourne un tableau contenant le nom des villes"""
    noms_v = []
    i = 0
    while 3*i < len(villes):
        noms_v.append(villes[3*i])
        i += 1
    return noms_v


def d2r(nb):
    return nb*pi/180


def distance(long1, lat1, long2, lat2):
    """retourne la distance entre les points (long1, lat1) et (long2, lat2)"""
    lat1 = d2r(lat1)
    long1 = d2r(long1)
    lat2 = d2r(lat2)
    long2 = d2r(long2)
    R = 6370.7
    d = R*arccos(sin(lat1)*sin(lat2)+cos(lat1)*cos(lat2)*cos(long2-long1))
    return d


def indexCity(ville, villes):
    """Retourne l'indice dans le tableau villes de la ville de nom ville,
       et -1 si elle n'existe pas
    """
    res = -1
    i = 0
    while 3*i < len(villes) and villes[3*i] != ville:
        i += 1
    if 3*i < len(villes):
        res = 3*i
    return res


def distance_noms(nom1, nom2, villes):
    """Retourne la distance entre les villes nom1 et nom2 
       en fonction de la structure de données villes
    """
    index1 = indexCity(nom1, villes)
    index2 = indexCity(nom2, villes)

    if index1 == -1 or index2 == -1:
        d = -1
    else:
        d = distance(villes[index1+1], villes[index1+2],
                     villes[index2+1], villes[index2+2])
    return d


def lecture_villes(path):
    """Retourne la structure de données villes en fonction des données du fichier path"""
    f_in = open(path, encoding='utf-8', mode='r')
    villes = []
    li = f_in.readline()
    li = li.strip()
    while li != '':
        tab_li = li.split(';')
        villes.append(tab_li[0])
        villes.append(float(tab_li[1]))
        villes.append(float(tab_li[2]))
        li = f_in.readline()
        li = li.strip()
    f_in.close()
    return villes


def long_tour(villes, tournee):
    """Retourne la longueur d'une tournée en fonction de la structure de données villes"""
    long = 0
    i = 0
    while i+1 < len(tournee):
        long += distance_noms(tournee[i], tournee[i+1], villes)
        i += 1
    long += distance_noms(tournee[i], tournee[0], villes)
    return long

##############
# SAE S01.02 #
##############


#Question 1
def dictionary_cities(villes):
    """
    Fonction prenant en paramètre un tableau villes comme définie dans la partie 1,
    et retournant un dictionnaire de distances contenant les distances entre les villes du tableau passé en paramètre.
    """
    dico = {}
    for v in range(0,len(villes),3):
        dico[villes[v]] = {}
        for i in range(0,len(villes),3):
            if villes[i] != villes[v]:
                dico[villes[v]][villes[i]] = distance_noms(villes[v],villes[i],villes)
    return dico


#Question 2
def distance_cities(name1, name2, d_cities):
    """
    Fonction prenant en paramètre deux noms de villes et un dictionnaire de distances,
    et retournant la distance entre les deux villes passées en paramètre si cette valeur est stockée dans le dictionnaire de villes, et -1 sinon.
    """
    if name1 not in d_cities.keys() or name2 not in d_cities[name1].keys(): #si les deux villes ne sont pas dans le dictionnaire
        return -1
    else:
        return d_cities[name1][name2]


#Question 3
def tour_length(tour, d_villes):
    """
    Calcule la longueur d'un tour en utilisant un dictionnaire de distances.
    
    Paramètres:
    - tour (list): Une liste représentant l'ordre du tour.
    - d_villes (dict): Un dictionnaire contenant les distances entre les villes.

    Retourne:
    - float: La longueur totale du tour.
    """
    total_length = 0
    for i in range(len(tour) - 1):
        current_city = tour[i]
        next_city = tour[i + 1]
        total_length += d_villes[current_city][next_city] #additionne la distance totale avec celle de la ville suivante

    total_length += d_villes[tour[-1]][tour[0]]
    return total_length


#Question 5
def closest_city(city, cities, d_cities):
    """
    Retourne l'indice de la ville de cities la plus proche de city.

    Paramètres:
    - city (str): Le nom de la ville de référence.
    - cities (list): Un tableau de noms de villes.
    - d_cities (dict): Un dictionnaire de distances entre les villes.

    Retourne:
    - int: L'indice de la ville la plus proche dans le tableau cities.
    """
    id_min_dist = 0
    min_dist = d_cities[city][cities[0]]

    for c in range(1, len(cities)):
        if min_dist > d_cities[city][cities[c]]: #si la distance minimale est plus grande que celle de la ville c
            min_dist = d_cities[city][cities[c]] #alors elle devient celle de la ville c
            id_min_dist = c

    return id_min_dist


#Question 6
def tour_from_closest_city(start_city, d_cities):
    """
    Construit un petit tour passant par toutes les villes en partant d'une ville de départ.

    Paramètres:
    - start_city (str): Le nom de la ville de départ.
    - d_cities (dict): Un dictionnaire de distances entre les villes.

    Retourne:
    - list: Le tour obtenu en ajoutant à chaque fois la ville restante la plus proche de la dernière ville ajoutée.
    """
    tour = [start_city]
    remaining_cities = list(d_cities.keys())
    remaining_cities.remove(start_city)

    while remaining_cities: #tant qu'il reste des villes
        current_city = tour[-1]
        index_closest_city = closest_city(current_city, remaining_cities, d_cities)
        tour.append(remaining_cities[index_closest_city]) #on ajoute la ville la plus proche
        remaining_cities.remove(remaining_cities[index_closest_city]) #et on l'enlève des villes restantes

    return tour


#Question 7
def best_tour_from_closest_city(d_cities):
    """
    Retourne le meilleur tour parmi ceux obtenus avec l'algorithme précédent en prenant chaque ville comme ville de départ.

    Paramètres:
    - d_cities (dict): Un dictionnaire de distances entre les villes.

    Retourne:
    - list: Le meilleur tour parmi ceux obtenus.
    """
    cities = list(d_cities.keys())
    best_tour = tour_from_closest_city(cities[0], d_cities)
    min_tour_length = tour_length(best_tour, d_cities)

    for start_city in cities[1:]:
        tour = tour_from_closest_city(start_city, d_cities)
        tour_length_value = tour_length(tour, d_cities)

        if tour_length_value < min_tour_length:
            min_tour_length = tour_length_value #si la longueur du tour actuel est plus petite que celle du meilleur tour précédent, alors on la remplace
            best_tour = tour

    return best_tour


#Question 9
def reverse_part_tour(tour, ind_b, ind_e):
    """
    Inverse la partie du tableau tour entre les indices ind_b et ind_e inclus.

    Paramètres:
    - tour (list): Le tableau représentant le tour.
    - ind_b (int): L'indice de début de la partie à inverser.
    - ind_e (int): L'indice de fin de la partie à inverser.
    """
    if ind_b < 0 or ind_e >= len(tour) or ind_b >= ind_e:
        print("Indices invalides.")
        return
    
    while ind_b < ind_e:
        tour[ind_b], tour[ind_e] = tour[ind_e], tour[ind_b]
        ind_b += 1
        ind_e -= 1 #inversion des indices de fin et de début

reverse_part_tour(["Agen", "Belfort", "Cahors", "Dijon", "Épinay", "Fréjus", "Grenoble", "Hyères"],2,5)


#Question 10
def inversion_length_diff(tour, d_cities, ind_b, ind_e):
    """
    Retourne la différence entre la distance du tour et celui obtenu en inversant une partie du tour.

    Paramètres:
    - tour (list): Le tableau représentant le tour.
    - d_cities (dict): Un dictionnaire de distances entre les villes.
    - ind_b (int): L'indice de début de la partie à inverser.
    - ind_e (int): L'indice de fin de la partie à inverser.

    Retourne:
    - float: La différence de distance entre le tour initial et le tour inversé.
    """
    a = tour.copy() #on copie le tour en paramètre pour le conserver
    reverse_part_tour(a, ind_b, ind_e) #on inverse sa copie entre les indices ind_b et ind_e
    
    return tour_length(tour, d_cities) - tour_length(a, d_cities) #on renvoie la différence entre les deux longueurs


#Question 11
def better_inversion(tour, d_cities):
    """
    Améliore le tour en explorant toutes les inversions possibles et en appliquant l'inversion
    permettant d'obtenir le plus petit tour si cela l'améliore.

    Paramètres:
    - tour (list): Le tableau représentant le tour.
    - d_cities (dict): Un dictionnaire de distances entre les villes.

    Retourne:
    - bool: True si une inversion du tour a été faite, False sinon.
    """
    length_diff = inversion_length_diff(tour, d_cities, 0, 1)
    a = 0
    b = 1

    for i in range(len(tour) - 1): #on compare le premier élément du tour avec les suivants. 
        #si on prend le premier élément, on le compare au 2e,3e,4e.
        #si on prend le deuxième élément, on le compare au 3e et 4e.
        #si on prend le troisième élément, on le compare au 4e.
        for j in range(i + 1, len(tour)):
            if not(i == 0 and j == 1): #on ne prend pas en compte la partie avec le premier et le deuxième élément car elle est déjà affectée avant en tant que 'Length_diff' 
                new_length_diff = inversion_length_diff(tour, d_cities, i, j)
                if new_length_diff > length_diff: #on compare la nouvelle longueur avec celle d'avant
                    a = i
                    b = j

    improved_tour = tour.copy()
    reverse_part_tour(improved_tour, a, b)

    if tour_length(tour, d_cities) > tour_length(improved_tour, d_cities):
        reverse_part_tour(tour, a, b)
        return True
    else:
        return False


#Question 12
def best_obtained_with_inversions(tour, d_cities):
    """
    Améliore le tour successivement par des inversions jusqu'à ce qu'aucune inversion ne puisse améliorer le tour.

    Paramètres:
    - tour (list): Le tableau représentant le tour.
    - d_cities (dict): Un dictionnaire de distances entre les villes.

    Retourne:
    - int: Le nombre d'inversions effectuées.
    """
    num_inversions = 0
    improved = True

    while improved: #tant que l'on peut trouver une meilleure inversion
        improved = better_inversion(tour, d_cities) #on l'améliore
        if improved:
            num_inversions += 1 #on augmente le nombre d'améliorations effectuées
    
    return num_inversions


