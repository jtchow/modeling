from models.MoneyModel import MoneyModel
import matplotlib.pyplot as plt


if __name__ == "__main__":
    all_wealth = []
    for run in range(100):
        model = MoneyModel(10)
        for i in range(10):
            model.step()
        for agent in model.schedule.agents:
            all_wealth.append(agent.wealth)
    plt.hist(all_wealth, bins=range(max(all_wealth) + 1))
