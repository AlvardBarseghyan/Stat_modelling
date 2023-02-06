# import random

# # population size
# N = 1000

# # initial infected
# infected = 1

# # infection rate
# beta = 0.3

# # recovery rate
# gamma = 0.1

# # number of steps to simulate
# steps = 10

# # initialize the number of susceptible, infected, and recovered individuals
# susceptible = N - infected
# recovered = 0

# # simulate the epidemic
# for step in range(steps):
#     # calculate the number of individuals who will become infected
#     newly_infected = beta * susceptible * infected
    
#     # update the number of susceptible, infected, and recovered individuals
#     susceptible -= newly_infected
#     infected += newly_infected - gamma * infected
#     recovered += gamma * infected
    
#     # output the current number of susceptible, infected, and recovered individuals
#     print(f"Step {step}: S={susceptible}, I={infected}, R={recovered}")


# Set initial values for variables
infected_population = 1  # initial number of infected people
susceptible_population = 10  # initial number of susceptible people
total_population = infected_population + susceptible_population  # total population

# Set infection and recovery rates
infection_rate = 0.1  # probability of infection per person per day
recovery_rate = 0.05  # probability of recovery per infected person per day

# Set the number of days to simulate
days = 365

# Loop through each day and update the population
for day in range(days):
    # Calculate the number of new infections
    new_infections = infection_rate * infected_population * susceptible_population / total_population

    # Calculate the number of recoveries
    recoveries = recovery_rate * infected_population

    # Update the population
    infected_population += new_infections - recoveries
    susceptible_population -= new_infections
    total_population = infected_population + susceptible_population

    # Print the current state of the population
    print("Day", day + 1)
    print("Infected:", infected_population)
    print("Susceptible:", susceptible_population)
    print("Total:", total_population)
