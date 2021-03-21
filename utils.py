import numpy as np
import matplotlib.pyplot as plt
import scipy


def generate_incomes(num_agents, base_income):
    distribution = np.random.gamma(shape=5, scale=.1, size=num_agents)
    incomes = [modifier * base_income for modifier in distribution]
    return incomes



