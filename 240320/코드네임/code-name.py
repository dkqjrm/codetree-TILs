class Agent:
    def __init__(self, name="", score=""):
        self.name = name
        self.score = score

    def __str__(self):
        return f'{self.name} {self.score}'

agents = []
for i in range(5):
    agents.append(Agent(*input().split()))

mini = 1e9
for agent in agents:
    if int(agent.score) <= mini:
        mini = int(agent.score)
        min_agent = agent

print(min_agent)