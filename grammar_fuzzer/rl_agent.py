import numpy as np


class ClassicQ:

    q = [{}]
    q_count = [{}]

    def __init__(self, actions, obs_space):
        self.actions = actions
        self.obs_space = obs_space

    def best_action(self, obs):
        max_val = -1
        res = 0
        for i in self.q[obs]:
            if self.q[obs][i] > max_val:
                res = i
        return res

    def e_greedy_action(self, obs, greedy_prob=0.1  ):
        if np.random.random() < greedy_prob:
            return np.random.choice(list(self.q[obs]))
        return self.best_action(obs)

    def step(self):
        with open('info.txt', 'r') as f:
           data = f.readlines()
        try:

            try:
                int(data[0])
                data = data[1:]
            except ValueError:
                pass
            reward = int(data[-2])
            for i in data[:-1]:
                try:
                    int(i)
                    continue
                except:
                    pass
                obs, action = i.split(';')
                action = action[:-1]
                self.q_count[obs][action] += 1
                self.q[obs][action] += (self.q[obs][action] + reward)/self.q_count[obs][action]
                with open('rewards.txt.', 'a') as rewards:
                    rewards.write(str(reward)+'\n')
            with open('info.txt', 'w') as f:
               f.write('')
        except:
            pass