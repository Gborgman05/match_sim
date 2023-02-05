import random 
from pprint import pprint

class match_node:
    def __init__(self, name=None):
        self.name = name
        self.matches = 0
        self.right = None
        self.throughput = 0
        self.roll_history = []
        self.throughput_history = []


    def pass_matches(self):
        numRolled = random.randint(1, 6)
        # if you rolled higher than your number of matches, give all your matches
        given = min(self.matches, numRolled)
        if self.right:
            self.right.matches += given
            self.matches -= given
        else:
            self.matches -= given 
        # record how many i gave
        self.throughput += given
        self.throughput_history.append(given)
        self.roll_history.append(numRolled)
    def __repr__(self):
        return (f"kid: {self.name} throughput: {self.throughput}, throughput_avg: {self.throughput / len(self.throughput_history)}")

def main():
    random.seed(10)
    num_kids = 10
    num_steps = 100
    for num_steps in [10, 100, 1000]:
        print(f"number of kids passing matches: {num_kids}")
        print(f"number of total steps recorded: {num_steps}")
        kid_line = []
        for i in range(num_kids):
            kid = match_node(i)
            kid_line.append(kid)
        for i in range(num_kids - 1):
            kid_line[i].right = kid_line[i+1]
        # kid on the left has infinite matches
        kid_line[0].matches = 1000000
        for i in range(num_steps):
            # go backwards in line so you can't pass same matches through line initially
            # for j in range(num_kids -1, -1, -1):
            for j in range(0, num_kids):
                kid_line[j].pass_matches()
        pprint(kid_line)


    
     


if __name__ == "__main__":
    main()