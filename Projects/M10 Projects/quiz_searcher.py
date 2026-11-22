# DSCM4L2 After Class Project: My Quiz Result Searcher (starter)
# How to run: python3 quiz_searcher.py, or paste into one Google Colab cell and press Run.
# Lines marked (given) are done for you. Your job is TODO 1 to TODO 3. Do them in order.
# Each TODO ends with a Check line: run the file after every TODO and compare.
# Errors appear at the bottom of the output; the last line names the problem.
# A teacher searches a class's quiz scores and looks for pairs of students with the
# same score. Count the checks for 8 and 16 students and classify each by its growth.


def count_checks(scores, target):
    """Linear search: return (index or -1, checks made)."""
    checks = 0
    # TODO 1: Linear search: visit every index, add 1 to checks for each score you look
    #         at, and send back the index and checks as soon as the score equals target.
    #         Check: best search 1 check; missing score 8 checks for 8 students.
    return -1, checks


def same_score_pairs(scores):
    """Compare every pair of students once: return (pairs with the same score, checks)."""
    pairs = 0
    checks = 0
    # TODO 2: Compare every pair of students exactly once: for each i, look only at the
    #         students after it (j bigger than i). Add 1 to checks per comparison and 1
    #         to pairs when the two scores are equal.
    #         Check: 1 with 28 checks (every pair) for 8 students.
    return pairs, checks


# (given) A: the fastest way, with a dictionary. Read it after TODO 2.
def same_score_pairs_fast(scores):
    """Optimal: count how often each score was seen before (dictionary): n checks."""
    seen = {}
    pairs = 0
    for s in scores:
        pairs = pairs + seen.get(s, 0)
        seen[s] = seen.get(s, 0) + 1
    return pairs, len(scores)


# (given) B: two classes; class_b has twice as many students.
class_a = [45, 62, 78, 85, 91, 56, 73, 62]
class_b = class_a + [88, 45, 70, 99, 62, 81, 77, 50]
results = []
for scores in [class_a, class_b]:
    n = len(scores)
    best = count_checks(scores, scores[0])[1]
    missing = count_checks(scores, 100)[1]
    pairs, pair_checks = same_score_pairs(scores)
    fast_pairs, fast_checks = same_score_pairs_fast(scores)
    results.append((missing, pair_checks))
    print(f"{n} students: best search {best} check, missing score {missing} checks")
    print(f"  same-score pairs: {pairs} with {pair_checks} checks (every pair);"
          f" {fast_pairs} with {fast_checks} checks (dictionary)")
print()
print("From 8 to 16 students (x2):")
# TODO 3: results[0] holds (missing checks, pair checks) for 8 students and results[1]
#         for 16. Print how many times bigger each count got, with its Big-O, using the
#         labels missing-score search and same-score pairs. Round the pairs to 2 decimals.
#         Check: x 2.0 -> O(n) ... and x 4.29 -> O(n^2) ...
print("  dictionary version  : n checks -> O(n) time, O(n) extra space (the best way)")
