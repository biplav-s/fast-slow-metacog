
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

   4. Solver
      - C (solver)
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

class MC:
    c = [1, 1] # cost of each solver
    r = [1, 1] # reliability of a solver

    
    
    def __init__(self):
        print ("Class for MC")
        
        
    def get_c(self):
        return self.c
        
    def get_r(self):
        return self.r
        
            