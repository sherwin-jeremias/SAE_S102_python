#Travail fait par Jérémias Sherwin et Dubord Ruben. BUT INFO 1, Boréas.


from santa_claus import *


d_villes = {
    'Paris': {
        'Lyon': 394.5056834297657, 
        'Marseille': 661.8616554466852, 
        'Lille': 203.67224282542662
    }, 
    'Lyon': {
        'Paris': 394.5056834297657, 
        'Marseille': 275.87965367431525, 
        'Lille': 558.5472363339435
    }, 
    'Marseille': {
        'Paris': 661.8616554466852, 
        'Lyon': 275.87965367431525, 
        'Lille': 834.0220261600157
    }, 
    'Lille': {
        'Paris': 203.67224282542662, 
        'Lyon': 558.5472363339435, 
        'Marseille': 834.0220261600157
    }
}


#Question 1
def test_dictionary_cities():
    
    assert dictionary_cities(["Paris",2.33, 48.86, "Lyon", 4.85, 45.75, "Marseille", 5.40, 43.30, "Lille", 3.06, 50.63]) == d_villes
    print('Test de test_dictionary_cities() est réussi')

test_dictionary_cities()


#Question 2
def test_distance_cities():
    
       assert distance_cities('Paris','Marseille',d_villes) == 661.8616554466852
       assert distance_cities('Lyon','Lille',d_villes) == 558.5472363339435
       print('Tous les cas de test_distance_cities sont réussis.')

test_distance_cities()


#Question 3
def test_tour_length():

    tour_1 = ["Paris", "Lyon", "Marseille", "Lille"]
    assert tour_length(tour_1, d_villes) == 1708.0796060895232

    tour_2 = ["Lyon", "Marseille", "Lille", "Paris"]
    assert tour_length(tour_2, d_villes) == 1708.0796060895232

    tour_3 = ["Marseille", "Paris", "Lyon", "Lille"]
    assert tour_length(tour_3, d_villes) == 2448.9366013704102

    print('Tous les cas de test_tour_length() sont réussis.')

test_tour_length()


#Question 5
def test_closest_city():
    
    city_1 = "Paris"
    cities_1 = ["Lyon", "Marseille", "Lille"]
    assert closest_city(city_1, cities_1, d_villes) == 2

    city_2 = "Lyon"
    cities_2 = ["Paris", "Marseille", "Lille"]
    assert closest_city(city_2, cities_2, d_villes) == 1

    city_3 = "Marseille"
    cities_3 = ["Paris", "Lyon", "Lille"]
    assert closest_city(city_3, cities_3, d_villes) == 1

    print('Tous les cas de test_closest_city() sont réussis.')

test_closest_city()


#Question 6
def test_tour_from_closest_city():
    
    start_city_1 = "Marseille"
    expected_tour_1 = ["Marseille", "Lyon", "Paris", "Lille"]
    assert tour_from_closest_city(start_city_1, d_villes) == expected_tour_1

    start_city_2 = "Paris"
    expected_tour_2 = ['Paris', 'Lille', 'Lyon', 'Marseille']
    assert tour_from_closest_city(start_city_2, d_villes) == expected_tour_2

    start_city_3 = "Lyon"
    expected_tour_3 = ['Lyon', 'Marseille', 'Paris', 'Lille']
    assert tour_from_closest_city(start_city_3, d_villes) == expected_tour_3

    print('Tous les cas de test_tour_from_closest_city() sont réussis.')

test_tour_from_closest_city()


#Question 7
def test_best_tour_from_closest_city():

    expected_best_tour_1 = ["Paris", "Lille", "Lyon", "Marseille"]  # ou ["Lyon", "Marseille", "Paris", "Lille"]
    assert best_tour_from_closest_city(d_villes) == expected_best_tour_1

    print('Tous les cas de test_best_tour_from_closest_city() sont réussis.')

test_best_tour_from_closest_city()


#Question 9
def test_reverse_part_tour():
    
    tour_1 = ["Agen", "Belfort", "Cahors", "Dijon", "Épinay", "Fréjus", "Grenoble", "Hyères"]
    ind_b_1, ind_e_1 = 2, 5
    expected_tour_1 = ["Agen", "Belfort", "Fréjus","Épinay", "Dijon", "Cahors", "Grenoble", "Hyères"]
    reverse_part_tour(tour_1, ind_b_1, ind_e_1)
    assert tour_1 == expected_tour_1

    print('Tous les cas de test_reverse_part_tour() sont réussis.')

test_reverse_part_tour()


#Question 10
def test_inversion_length_diff():
    
    tour_1 = ["Marseille", "Lyon", "Paris", "Lille"]
    ind_b_1, ind_e_1 = 1, 2
    expected_diff_1 = -740.8569952808871
    assert inversion_length_diff(tour_1, d_villes, ind_b_1, ind_e_1) == expected_diff_1

    print('Tous les cas de test_inversion_length_diff() sont réussis.')

test_inversion_length_diff()


#Question 11
def test_better_inversion():

    tour_1 = ["Marseille", "Paris", "Lyon", "Lille"]
    assert better_inversion(tour_1, d_villes) == True
    assert tour_1 == ["Paris", "Marseille", "Lyon", "Lille"]

    tour_2 = ["Marseille", "Lyon", "Lille", "Paris"]
    assert better_inversion(tour_2, d_villes) == False
    assert tour_2 == ["Marseille", "Lyon", "Lille", "Paris"]

    print('Tous les cas de test_better_inversion() sont réussis.')

test_better_inversion()


#Question 12
def test_best_obtained_with_inversions():

    tour_1 = ["Marseille", "Paris", "Lyon", "Lille"]
    assert best_obtained_with_inversions(tour_1, d_villes) == 1
    assert tour_1 == ["Paris", "Marseille", "Lyon", "Lille"]

    tour_2 = ["Marseille", "Lyon", "Lille", "Paris"]
    assert best_obtained_with_inversions(tour_2, d_villes) == 0
    assert tour_2 == ["Marseille", "Lyon", "Lille", "Paris"]

    print('Tous les cas de test_best_obtained_with_inversions() sont réussis.')

test_best_obtained_with_inversions

