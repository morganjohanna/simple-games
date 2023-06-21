"""
This is code for Mr. Flynn's Math Game. It procedurally generates expressions of a simple mathematical equation composed of positive integers between 1 and 10. One expression (the answer) is a single integer while the other contains 4 coefficients and missing operators. The player is tasked with determining the operators and order in which the 4 coefficients should be calculated to equal the answer; each coefficient must be used exactly once and possible operators are + - * / ( ). If stuck, a player can skip the current problem. The game times the player and displays the time it took them to solve a problem if they input a valid solution.
"""

import random
import time
import re

class MathGame():
    """
    Main class managing game iterations, problem generation, and player solution validation.
    """
    
    def __init__(self):
        """
        Initializes class instance.
        """
        
        self.running = False
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.answer = 0
        self.player_answer = "0"
        self.solution_valid = False
        self.new_line = "\n"

    def main(self):
        """
        Controls the main game loop and prints player information, keeps track of time, allows the player to skip a problem, and enables them to control when the next problem is presented and the timer begins.
        """
        rules = "The game is simple. You will be presented with five numbers between 1 and 10, all unique positive integers. Using + - * / and () and being mindful of order of operations, you must input the complete expression so that the problem equals the answer. Each number must be used exactly once.\n\nYou will be timed (in case you want to compete with yourself or a friend) and, if your solution is correct, your time displayed. Sometimes there is more than one solution!"
        example = "Here's an example:\nProblem: 2  5  8  9\nAnswer: 1\nCorrect answer: (8/2+5)/9"
        
        print("Welcome to Mr. Flynn's Math Game!")
        print(rules)
        print(example)
        
        self.running = True

        while self.running:
            self.new_problem()
            input("\n-----\n\nReady to go? Press ENTER to see the next problem!")
            start_time = time.time()
            
            print(f"{self.new_line}Problem: {self.a}  {self.b}  {self.c}  {self.d}{self.new_line}Answer: {self.answer}{self.new_line}")
            self.player_answer = input("Type your solution and press ENTER to stop the clock: ")
            stop_time = time.time()

            duration = stop_time - start_time
            minutes = duration // 60
            seconds = int(duration % 60)
            
            self.solution_check()

            if self.solution_valid:
                print(f"Congratulations, that's right! It only took you {minutes} minutes and {seconds} seconds to find the solution.")
            else:
                print("Sorry, that's not correct.")
                reminder = input("Would you like a reminder of the RULES or to see an EXAMPLE?").lower()
                if reminder == "rules":
                    print(rules)
                elif reminder == "example":
                    print(example)
                else:
                    pass

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

        self.a = random.randint(1, 10)
        self.b = random.randint(1, 10)
        self.c = random.randint(1, 10)
        self.d = random.randint(1, 10)
        self.answer = random.randint(1, 10)

        while self.b == self.a:
            self.b = random.randint(1, 10)

        while self.c == self.a or self.c == self.b:
            self.c = random.randint(1, 10)

        while self.d == self.a or self.d == self.b or self.d == self.c:
            self.d = random.randint(1, 10)

        while self.answer == self.a or self.answer == self.b or self.answer == self.c or self.answer == self.d:
            self.answer = random.randint(1, 10)

        return self.a, self.b, self.c, self.d, self.answer

    def solution_check(self):
        """
        Validates the player's solution for allowed input per game rules and that it is a correct answer. Leading zeroes will not be recognized (e.g. 6 is accepted, but 06 will confuse the validator).

        Returns
        -------
        self.solution_valid: boolean
            Marked True if solution is valid
        """

        permitted_operators = ["(", ")", "*", "/", "+", "-"]
        problem_coefficients = [str(self.a), str(self.b), str(self.c), str(self.d)]

        digits_unpacked = []
        player_answer_unpacked = []
        
        # Duplicate and 0 check: simplifies player input to a list of digits only, corrects for 10, and checks for extraneous zeroes and duplicates
        digits = re.findall(r"\d", self.player_answer)
        digits_unpacked = [*digits]

        for i in range(len(digits_unpacked)-1):
            if digits_unpacked[i] == "1":
                if digits_unpacked[i+1] == "0":
                    digits_unpacked[i] = "10"
                    del digits_unpacked[i+1]
                else:
                    self.solution_valid = False
                    return self.solution_valid

        for i in digits_unpacked:
            digits_unpacked_set = set(digits_unpacked)
            if len(digits_unpacked) != len(digits_unpacked_set):
                self.solution_valid = False
                return self.solution_valid

        # Legal input check: creates list of player input, corrects for 10, and checks that input legal
        player_answer_unpacked = [*self.player_answer]

        for i in range(len(player_answer_unpacked)-1):
            if player_answer_unpacked[i] == "1":
                if player_answer_unpacked[i+1] == "0":
                    player_answer_unpacked[i] = "10"
                    del player_answer_unpacked[i+1]

        for i in range(len(player_answer_unpacked)):
            if player_answer_unpacked[i] not in permitted_operators and player_answer_unpacked[i] not in problem_coefficients:
                self.solution_valid = False
                return self.solution_valid

        # Right answer check: evaluates player solution to check that it equals given answer
        try:
            if eval(self.player_answer) == self.answer:
                self.solution_valid = True
            else:
                self.solution_valid = False
            
            return self.solution_valid
        
        except:
            self.solution_valid = False
            return self.solution_valid

game = MathGame()
game.main()