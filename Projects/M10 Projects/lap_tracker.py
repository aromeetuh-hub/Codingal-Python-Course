# DSCM4L1 After Class Project: My Running Lap Tracker (starter)
# How to run: python3 lap_tracker.py, or paste into one Google Colab cell and press Run.
# Lines marked (given) are done for you. Your job is TODO 1 to TODO 3. Do them in order.
# Each TODO ends with a Check line: run the file after every TODO and compare.
# Errors appear at the bottom of the output; the last line names the problem.
# Lap 1 earns 1 point, lap 2 earns 3, lap 3 earns 5: each lap earns 2 more than the
# one before, so lap k earns 2*k - 1 points. Find the total after n laps three ways.


def total_formula(n):
    """The odd numbers 1 + 3 + 5 + ... add up to n * n."""
    # TODO 1: Send back the total with the formula and 1 step (replace the line below).
    #         Write out 1 + 3 + 5 for 3 laps and 1 + 3 + 5 + 7 for 4 laps: what is the pattern?
    #         Check: Formula total = 25 for 5 laps.
    return 0, 1  # (given) placeholder: delete this line when you write TODO 1


def total_loop(n):
    total, steps = 0, 0
    # TODO 2: Visit every lap from 1 to n. Add that lap's points to total and add 1 to steps.
    #         Check: Loop total = 25   steps = 5 for 5 laps.
    return total, steps


def total_point_by_point(n):
    total, steps = 0, 0
    # TODO 3: Visit every lap; inside, visit every single point of that lap and add 1 to
    #         total and 1 to steps for each point.
    #         Check: Point by point total = 25   steps = 25 for 5 laps.
    return total, steps


# (given) A: print all three answers for 5 laps and for 50 laps.
for n in [5, 50]:
    print("Laps:", n)
    print("  Formula        total =", total_formula(n)[0], "  steps =", total_formula(n)[1])
    print("  Loop           total =", total_loop(n)[0], "  steps =", total_loop(n)[1])
    print("  Point by point total =", total_point_by_point(n)[0], "  steps =", total_point_by_point(n)[1])
print()
print("Formula: O(1) time. Loop: O(n) time. Point by point: O(n^2) time.")
print("All three keep only a few numbers: O(1) extra space.")
