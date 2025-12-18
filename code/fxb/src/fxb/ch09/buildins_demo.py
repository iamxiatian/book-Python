import math

scores = [72, 98, 80, 69, 85]
total = 0
for score in scores:
    total += score

total = sum(scores)

max_score = -math.inf
for x in scores:
    max_score = max(max_score, x)
    
max_score = max(scores)

has_pass = False
for x in scores:
    if x >= 60:
        has_pass = True
        break
has_pass = any(x >= 60 for x in scores)

all_pass = True
for x in scores:
    if x < 60:
        all_pass = False
        break
all_pass = all(x >= 60 for x in scores)


def f(x:int)->float:
    return x * 1.1

new_scores = []
for x in scores:
    new_scores.append(f(x))
    

high_scores = []
for x in scores:
    if x >= 80:
        high_scores.append(x)
high_scores = filter(x >= 80, scores)
print(high_scores)
