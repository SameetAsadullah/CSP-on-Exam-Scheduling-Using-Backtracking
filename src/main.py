"""
Naive backtracking search without any heuristics or inference.
"""

VARIABLES = ["A", "B", "C", "D", "E", "F", "G"]
DOMAIN = ["Monday", "Tuesday", "Wednesday"]
CONSTRAINTS = [
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("B", "D"),
    ("B", "E"),
    ("C", "E"),
    ("C", "F"),
    ("D", "E"),
    ("E", "F"),
    ("E", "G"),
    ("F", "G")
]


def backtrack(assignment):
    """Runs backtracking search to find an assignment."""
    # Check if assignment is complete
    if len(assignment) == len(VARIABLES):
        return assignment
    var = select_unassigned_variable(assignment)
    for value in DOMAIN:
        if consistent(var, value, assignment):
            assignment[var] = value
            result = backtrack(assignment)
            if result is not None:
                return result
    return None


def select_unassigned_variable(assignment):
    """Chooses a variable not yet assigned, in order."""
    for var in VARIABLES:
        if var not in assignment.keys():
            return var


def consistent(var, value, assignment):
    """Checks to see if an assignment is consistent."""
    for var1, var2 in CONSTRAINTS:
        if var1 == var or var2 == var:
            for var3, day in assignment.items():
                if (var3 == var2 or var3 == var1) and day == value:
                    return False
    return True


solution = backtrack(dict())
print(solution)
