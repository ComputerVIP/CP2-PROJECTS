#Using PyBrain AI
# https://www.tutorialspoint.com/pybrain/introduction_to_pybrain_networks.htm

from pybrain.tools.shortcuts import buildNetwork
Network = buildNetwork(2, 3, 1)
print(Network)