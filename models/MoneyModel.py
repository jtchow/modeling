from mesa import Agent, Model
from mesa.time import RandomActivation
from utils import generate_incomes


class Person(Agent):
    """An agent with fixed initial wealth."""
    def __init__(self, unique_id, model, income):
        super().__init__(unique_id, model)
        self.wealth = 5
        self.income = income
        print(f'Agent number {self.unique_id} makes ${self.income}.')

    def step(self):
        print(f'I am agent number {self.unique_id} and I have {self.wealth} dollars')
        if self.wealth == 0:
            return
        selected_corp = self.random.choice(self.model.corp_schedule.agents)
        selected_corp.wealth += 1
        self.wealth -= 1
        print(f"""
                Agent {self.unique_id} gave Corporation {selected_corp.unique_id} 1 dollar. 
                Agent {self.unique_id} has {self.wealth} dollars.
                """
              )


class Corporation(Agent):
    """An corporation agent with fixed initial wealth."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 100

    def step(self):
        print(f'Corporation number {self.unique_id} has {self.wealth} dollars')
        if self.wealth == 0:
            return
        print(f'Corporation number {self.unique_id} does something')
        # todo what do corporations do at steps?
        # other_agent = self.random.choice(self.model.schedule.agents)
        # other_agent.wealth += 1
        # self.wealth -= 1
        # print(f"""
        #         Agent {self.unique_id} gave Agent {other_agent.unique_id} 1 dollar.
        #         Agent {self.unique_id} has {self.wealth} dollars.
        #         """
        #       )


class MoneyModel(Model):
    """A model with some number of agents."""
    def __init__(self, num_agents, num_corps):
        # todo move these into a config yaml or something, or better yet randomly generated
        self.num_agents = num_agents
        self.num_corps = num_corps
        self.agent_schedule = RandomActivation(self)
        self.corp_schedule = RandomActivation(self)
        self.incomes = generate_incomes(num_agents, 80000)
        for i in range(self.num_agents):
            person_income = self.incomes[i]
            a = Person(i, self, person_income)
            self.agent_schedule.add(a)

        for i in range(self.num_corps):
            corp = Corporation(i, self)
            self.corp_schedule.add(corp)

    def step(self):
        self.agent_schedule.step()
        self.corp_schedule.step()