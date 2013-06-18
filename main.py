######################################################
# Developed by Alborz Geramiard Oct 25th 2012 at MIT #
######################################################
from Tools import *
from Domains import *
from Agents import *
from Representations import *
from Policies import *
from Experiments import *

# Etc
#----------------------
DEBUG               = 0
SHOW_ALL            = 0
SHOW_PERFORMANCE    = 0
LOG_INTERVAL        = 1 
PERFORMANCE_CHECKS  = 10
LEARNING_STEPS      = 20000
RESULT_FILE         = 'result.txt'
# Domain
#----------------------
MAZE                = '/Domains/PitMazeMaps/4by5.txt'
NOISE               = 0
# Representation
#----------------------
RBFS                = 9
Discovery_Threshold = 1
# Policy
#----------------------
EPSILON             = .1 # EGreedy
#Agent
#----------------------
initial_alpha       = .1

#domain          = PitMaze(MAZE, noise = NOISE)
#domain          = BlocksWorld(blocks=3,noise = NOISE)
domain          = MountainCar(noise = NOISE)
#representation  = Tabular(domain)
#representation  = IncrementalTabular(domain)
#representation  = iFDD(domain,Discovery_Threshold)
#representation  = IndependentDiscretization(domain)
representation  = RBF(domain, rbfs = RBFS)
policy          = eGreedy(representation, epsilon = EPSILON)
agent           = SARSA(representation,policy,domain,initial_alpha)
experiment      = OnlineExperiment(agent,domain,max_steps = LEARNING_STEPS,show_all= SHOW_ALL, performanceChecks = PERFORMANCE_CHECKS, show_performance = SHOW_PERFORMANCE, log_interval = LOG_INTERVAL)

if DEBUG:
    domain.printAll()
    representation.printAll()
    policy.printAll()
    agent.printAll() 

experiment.run()
experiment.save(RESULT_FILE)
pl.show()

 