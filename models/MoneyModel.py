from mesa import Agent, Model
from mesa.time import RandomActivation


class MoneyAgent(Agent):
    """An agent with fixed initial wealth."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1

    def step(self):
        print(f'I am agent number {self.unique_id} and I have {self.wealth} dollars')
        if self.wealth == 0:
            return
        other_agent = self.random.choice(self.model.schedule.agents)
        other_agent.wealth += 1
        self.wealth -= 1
        print(f"""
                Agent {self.unique_id} gave Agent {other_agent.unique_id} 1 dollar. 
                Agent {self.unique_id} has {self.wealth} dollars.
                """
              )


class MoneyModel(Model):
    """A model with some number of agents."""
    def __init__(self, num_agents, num_corps):
        self.num_agents = num_agents, num_corps
        self.schedule = RandomActivation(self)
        # Create agents
        for i in range(self.num_agents):
            a = MoneyAgent(i, self)
            self.schedule.add(a)

    def step(self):
        self.schedule.step()