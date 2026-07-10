#before

scores = [88, 92,79, 95]
total = 0
for s in scores:
    total += s
average = total / len(scores)
print(average)

scores2 = [79, 85, 90]
total = 0
for s in scores2:
    total += s
average = total / len(scores2)
print(average)




#after
def average(scores):
    return sum(numbers) / len(numbers)

print(average([88, 92,79, 95]))
print(average([79, 85, 90]))