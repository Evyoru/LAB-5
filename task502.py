text = input()

best = 0

for i in range(len(text)):
    candidate = int(text[:i] + text[i + 1:])
    if candidate > best:
        best = candidate

print(best)