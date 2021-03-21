from models.MoneyModel import MoneyModel
import matplotlib.pyplot as plt


def show_income_distribution_results(num_iterations, num_agents, num_corps):
    all_income = []
    for run in range(num_iterations):
        model = MoneyModel(num_agents=num_agents, num_corps=num_corps)
        for agent in model.agent_schedule.agents:
            all_income.append(agent.income)
    plt.hist(all_income, bins=12)
    plt.show()


if __name__ == "__main__":
    # model = MoneyModel(10, 3)
    # for i in range(10):
    #     model.step()
    # for corp in model.corp_schedule.agents:
    #     print(f"Corporation {corp.unique_id}'s wealth: {corp.wealth}")
    # for agent in model.agent_schedule.agents:
    #     print(f"Agent {agent.unique_id}'s wealth: {agent.wealth}")
    # todo maybe randomly generate parameters and run a bunch of times, check at end of each run if target variable is reached and save the params that gave the best ones
    show_income_distribution_results(num_iterations=1000, num_agents=10, num_corps=3)


