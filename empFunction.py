import sys

if len(sys.argv) == 2:
    scores = [float(arg) for arg in sys.argv[1:]]
else:
    scores = [50, 60, 70] 

total = sum(scores)  # Use a different variable name
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)
    
print(f"Scores: {scores}")
print(f"Sum of scores: {total}")
print(f"Average of scores: {average:.2f}")
print(f"Maximum score: {maximum}")
print(f"Minimum score: {minimum}")
