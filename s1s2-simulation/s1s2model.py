
"""

   1. System - a simulation environment
      - Config: 1S1, 1S2, 1MC
      - states: (actions x ....)
      - actions:  a1, a2, a3, a4
      - current_state
      - current_action 

   2. MC
      - mc_value: value of action, state
      - solver_choice: {default, s2}
      - reliability_value[solvers / state]: prob of action being selected 
        by solver conditioned by state
      - solver_cost

   4. Solver
      - Cost (solver)
      - SolverType: S1 or S2
      - SolverOutput
        * Action
        * Confidence
   
   5. World - // design time representation pieces
      - State
        * Reward
      - Action
        * expected_value        
      - Reward(action, state)


    """

import random

# The agent system
class AgentSystem:
    mc = None             # The configured mc. We can get solvers from it
    current_time = 0      # Current time
    aggregate_reward = 0  # Aggregate reward earned by the agent
    aggregate_cost = 0    # Aggregate cost incurred by the agent
    aggregate_duration = 0  # Aggregate duration taken by the agent; maybe same as cost

    
    def __init__(self):
        print ("Agent System class instantiated")

    def printAgentSystem(self):
        print("mc: ", self.mc)
        print("current_time:", self.current_time)
        print("aggregate_reward:", self.aggregate_reward)
        print("aggregate_cost:", self.aggregate_cost)        
        print("aggregate_duration:", self.aggregate_duration) 
        
    # Run simulation up to time instant given
    def runSimulation(self, time):
        
        for i in range(time):
            index = self.mc.chooseSolver()
            
            self.aggregate_duration += self.mc.solvers[index].solver_time_taken
            self.aggregate_reward += self.mc.solvers[index].solver_output_reward      
            self.current_time = self.aggregate_duration

            print(" -> sim = " + str(i) + ", solver = " + str(index) + ", duration = " + str(self.aggregate_duration) +
                 ",  agg. reward = " + str(self.aggregate_reward))

 
# For the MC
class MC:         
    solvers = []           # Solvers registered 
    mc_value = 1.0         # Value of action, given a state
    solver_choice = None   # Nothing at the start
    reliability_values = {} # A dictionary containing reliability for each solver
    solver_costs = {}       # A dictionary containing costs for each solver

    
    def __init__(self):
        print ("MC class instantiated")

    def printMC(self):
        print("solvers: ", self.solvers)
        print("mc_value:", self.mc_value)
        print("solver_choice:", self.solver_choice)
        print("reliability_values:", self.reliability_values)        
        print("solver_costs:", self.solver_costs) 

    # Choose solver from list
    def chooseSolver(self):
        solverIndex = random.choice(range(0, len(self.solvers)))
        self.solver_choice = solverIndex
        return solverIndex
 

# For the solver
class Solver:
    name = ""
    solver_type = 'S1'  # Solver type by fefault
    solver_output_action = 'default_action' # Solver's output is default action
    solver_output_confidence = 0.5            # Solver's output's default confidence is 0.5
    solver_output_reward = 1.0                # Solver's reward for the output chosen
    solver_time_taken = 1.0                   # Time that this solver takes
    
    def __init__(self):
        print ("Solver class instantiated")
        
    def printSolver(self):
        print("name: ", self.name)
        print("solver_type:", self.solver_type)
        print("solver_output_action:", self.solver_output_action)
        print("solver_output_confidence:", self.solver_output_confidence)   
        print("solver_output_reward:", self.solver_output_reward)   
        print("solver_time_taken:", self.solver_time_taken)        


            