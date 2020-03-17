import numpy as np
import random

reward = np.array([[-1,0,0,-1,-1,-1],
             [0,-1,-1,-1,0,100],
             [0,-1,-1,0,-1,-1],
             [-1,-1,0,-1,-1,-1],
             [-1,0,-1,-1,-1,-1],
             [-1,0,-1,-1,-1,100]])
print("Reward matrix is: ")
print(reward)
print("=====================================")
q = np.zeros([6,6])
gamma = 0.8
# initial = np.random.randint(0,6)
def find_cost(l):
    state = l[1]
    nstate=[]
    for j in range(len(reward[state])):
        if reward[state,j] != -1:
            nstate.append([state, j])
    maxi = max(q[j[0], j[1]] for j in nstate)
    return int(maxi)

def logic(initial, final):
    state = initial
    # print(str(state) + '-', end='')
    while(state != final):
        nstate=[]
        for j in range(len(reward[state])):
            if reward[state,j] != -1:
                nstate.append([state, j])
        nstate1 = random.choice(nstate)
        compute = find_cost(nstate1)
        q[nstate1[0],nstate1[1]] = reward[nstate1[0], nstate1[1]] + (gamma*compute)
        state = nstate1[1]
        # print(str(state) + '-', end='')

for i in range(5000):
    initial = np.random.randint(0,6)
    final = np.random.randint(0,6)
    logic(initial,final)


print("\nQ matrix is: ")
print(q)
print("=====================================")
while(1):
    initial1 = int(input("\nEnter initial "))
    final1 = 5
    logic(initial1, final1)
    print(initial1, end='')
    state1 = initial1
    while (state1!=final1):
        state1 = list(q[state1]).index(max(q[state1]))
        print('->', state1, end='')
    print("\nYo! You reached to goal state as per reward matrix")
