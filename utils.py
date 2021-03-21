import numpy as np


def generate_incomes(num_agents, base_income):
    distribution = np.random.gamma(shape=3, scale=.2, size=num_agents)
    incomes = [modifier * base_income for modifier in distribution]
    return incomes



