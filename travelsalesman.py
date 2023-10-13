   
#Problem 2
#Given the following map of cities as a graph write a Python program using the Genetic Algorithm 
#to find the shortest possible route that visits every city exactly once and returns to the starting point.
import random

cities = {
    "A": {"A": 0, "B": 12, "C": 10, "D": 21, "E": 13, "F": 19, "G": 12},
    "B": {"A": 12, "B": 0, "C": 8, "D": 12, "E": 11, "F": 17, "G": 17},
    "C": {"A": 10, "B": 8, "C": 0, "D": 11, "E": 3, "F": 9, "G": 9},
    "D": {"A": 21, "B": 12, "C": 11, "D": 0, "E": 11, "F": 10, "G": 18},
    "E": {"A": 13, "B": 11, "C": 3, "D": 11, "E": 0, "F": 6, "G": 7},
    "F": {"A": 19, "B": 17, "C": 9, "D": 10, "E": 6, "F": 0, "G": 9},
    "G": {"A": 12, "B": 17, "C": 9, "D": 18, "E": 7, "F": 9, "G": 0}
}

#Genetic algorithm parameters
population_size = 100
generations = 500
mutation_rate = 0.01

#Generate an initial random population of routes
def generate_initial_population(cities, population_size):
    population = [list(cities.keys()) for _ in range(population_size)]
    for i in range(population_size):
        random.shuffle(population[i])
    return population

#Calculate the total distance of a route
def calculate_distance(route, cities):
    total_distance = 0
    for i in range(len(route) - 1):
        city1 = route[i]
        city2 = route[i + 1]
        total_distance += cities[city1][city2]
    
    #Adds the return distance to the starting city (A)
    total_distance += cities[route[-1]][route[0]]  #Return to the starting city (A)
    
    return total_distance

def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1) - 1)
    child1 = parent1[:crossover_point]
    child2 = [city for city in parent2 if city not in child1]
    child1 += child2
    return child1

def mutate(route):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(route)), 2)
        route[idx1], route[idx2] = route[idx2], route[idx1]


def genetic_algorithm(cities, population_size, generations, mutation_rate):
    population = generate_initial_population(cities, population_size)
    for generation in range(generations):
        population.sort(key=lambda route: calculate_distance(route, cities))
        new_population = population[:population_size // 2]
        while len(new_population) < population_size:
            parent1, parent2 = random.choices(population[:population_size // 2], k=2)
            child = crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)
        population = new_population
    return population[0]

#Finds the best route (shortest path)
shortest_route = genetic_algorithm(cities, population_size, generations, mutation_rate)

#Ensure that the route starts and ends at city "A"
if shortest_route[0] != "A":
    shortest_route.insert(0, "A")
if shortest_route[-1] != "A":
    shortest_route.append("A")

#Calculates the total distance of the modified route
shortest_distance = calculate_distance(shortest_route, cities)

#Print the best route and its distance
print(f"Shortest Route: {shortest_route} \nShortest Distance: {shortest_distance}")

