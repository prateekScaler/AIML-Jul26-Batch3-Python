# Small functions, one job each: one computes, one decides, the main program connects them.
def calculate_average(score1, score2, score3):
    total = score1 + score2 + score3
    return total / 3

def check_result(average):
    if average >= 40:
        return "Pass"
    return "Fail"

average = calculate_average(80, 90, 70)
result = check_result(average)
print("Average:", average)
print("Result:", result)
