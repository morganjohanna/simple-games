"""
This is code for Mr. Flynn's Math Game. It procedurally generates expressions of a simple mathematical equation composed of positive integers between 1 and 10 and basic mathematical operators (+, -, *, /). One expression (the answer) is a single integer while the other contains 4 coefficients. The player is tasked with determining the operators and order in which the 4 coefficients should be calculated to equal the answer; each coefficient must be used exactly once. If stuck, a player can skip the current problem. The game times the player and displays the time it took them to solve a problem if they input a valid solution.
"""

import keyboard
import time

class MathGame():
    """
    Main class managing game iterations, problem generation, and player solution validation.
    """
    
    def __init__(self):
        """
        Initializes class instance.
        """
        
        self.running = True
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.answer = 0
        self.player_answer = "0"
        self.solution_valid = False

    def main(self):
        """
        Controls the main game loop and prints player information, keeps track of time, allows the player to skip a problem, and enables them to control when the next problem is presented and the timer begins.
        """

        while running:
            # Part 1
            # print intro text, how to play, give an example, how to skip/proceed, how to quit
            # generate new problem with new_problem()
            # wait for player input to proceed
            # for key input:
                # keyboard.wait("space") to proceed
            
            # Part 2
            # print new problem
            # start clock with time.time()
            # wait for player input to proceed, self.player_answer = input("What is your solution?\n")
            
            # Part 3
            # if skip: pass
            # else: stop clock with time.time(), run solution_check()
                # if self.solution_valid: print congratulations method and time it took to solve
                # else: print invalid answer message with example right answer (not specific to the problem)
            
            #repeat

    def new_problem(self):
        """
        Randomly generates two expressions, without operators, of an equation: a problem (the four unique, random positive integers between 1 and 10) and a solution (a unique, random positive integer between 1 and 10). The player must determine the operators and order required for the problem to equal the solution.
        
        Returns
        -------
        self.a: integer
            The first coefficient of the equation, unique from the other returned values; min 1, max 10
        self.b: integer
            The first coefficient of the equation, unique from the other returned values; min 1, max 10
        self.c: integer
            The first coefficient of the equation, unique from the other returned values; min 1, max 10
        self.d: integer
            The first coefficient of the equation, unique from the other returned values; min 1, max 10
        self.answer: integer
            The first expression of the equation, unique from the other returned values; min 1, max 10
        """

        # generate everything with randint(1, 11), regenerate if duplicate

    def solution_check(self):
        """
        Validates the player's solution for allowed input per game rules and that it is a correct answer. Leading zeroes will not be recognized (e.g. 6 is accepted, but 06 will confuse the validator).

        Returns
        -------
        self.solution_valid: boolean
            Marked True if solution is valid
        """

        # use regex to filter out and separate digits and operators and make sure 10 doesn't get lost
            # if self.player_answer contains input != exactly 1 each of self.a, self.b, self.c, or self.d (except for operators), mark invalid
            # if self.player_answer contains anything other than a single operator (+ - * /) not between numbers, mark invalid

game = MathGame()
game.main()