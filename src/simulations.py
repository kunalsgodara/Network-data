import random

def simulate_spread(G, start_node, beta=0.2, steps=20):
    
    infected = set([start_node])
    newly_infected = set([start_node])
    
    history = [1]

    for step in range(steps):

        next_infected = set()

        for node in newly_infected:
            neighbors = G.neighbors(node)

            for n in neighbors:
                if n not in infected:
                    if random.random() < beta:
                        next_infected.add(n)

        infected.update(next_infected)
        newly_infected = next_infected
        
        history.append(len(infected))

        if len(newly_infected) == 0:
            break

    return history