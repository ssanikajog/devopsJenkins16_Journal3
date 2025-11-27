import sys

if len(sys.argv) > 1:
    arg_str = " ".join(sys.argv[1:])
    scores = [float(x) for x in arg_str.split()]
else:
    scores = [50, 60, 70] 

total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)
    
print(f"Scores: {scores}")
print(f"Sum of scores: {total}")
print(f"Average of scores: {average:.2f}")
print(f"Maximum score: {maximum}")
print(f"Minimum score: {minimum}")
