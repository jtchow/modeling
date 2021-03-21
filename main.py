from models.MoneyModel import MoneyModel
import matplotlib.pyplot as plt


if __name__ == "__main__":
    # model = MoneyModel(10, 3)
    # for i in range(10):
    #     model.step()
    # for corp in model.corp_schedule.agents:
    #     print(f"Corporation {corp.unique_id}'s wealth: {corp.wealth}")
    # for agent in model.agent_schedule.agents:
    #     print(f"Agent {agent.unique_id}'s wealth: {agent.wealth}")
    all_income = []
    for run in range(100):
        model = MoneyModel(num_agents=10, num_corps=3)
        for agent in model.agent_schedule.agents:
            all_income.append(agent.income)
    plt.hist(all_income, bins=12)

