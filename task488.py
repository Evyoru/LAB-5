words = input().split()
words.sort(key=len)

result = ""
for word in words:
    result = result + word + ", "

print(result[:-2] + ".")