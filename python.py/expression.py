class ExpressionSolver:
    def __init__(self, expression):
        self.expression = expression

    def solve(self):
        try:
            result = eval(self.expression)
            return result
        except Exception as e:
            return f"Error: {e}"


# Taking input from the user
expr = input("Enter a mathematical expression: ")

# Creating object
solver = ExpressionSolver(expr)

# Printing the result
print("Result:", solver.solve())
