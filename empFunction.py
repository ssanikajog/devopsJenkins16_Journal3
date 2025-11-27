import sys

if len(sys.argv) == 2:
    scores = [float(arg) for arg in sys.argv[1:]]
else:
    scores = [50, 60, 70] 

def calculate_sum(scores):
    return sum(scores)

def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

def calculate_max(scores):
    if len(scores) == 0:
        return None
    return max(scores)

def calculate_min(scores):
    if len(scores) == 0:
        return None
    return min(scores)

total = calculate_sum(scores)
average = calculate_average(scores)
maximum = calculate_max(scores)
minimum = calculate_min(scores)
    
print(f"Scores: {scores}")
print(f"Sum of scores: {total}")
print(f"Average of scores: {average:.2f}")
print(f"Maximum score: {maximum}")
print(f"Minimum score: {minimum}")