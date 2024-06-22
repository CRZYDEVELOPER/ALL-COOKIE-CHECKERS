import random
def random_proxy(txtfile):
    with open(txtfile, "r") as f:
        lines = f.readlines()  # Read all lines into a list
        return random.choice(lines)
