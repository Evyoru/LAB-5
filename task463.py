text = input()

result = ""
previous_space = False

for ch in text:
    if ch == " ":
        if not previous_space:
            result = result + "_"
        previous_space = True
    else:
        result = result + ch
        previous_space = False

print(result)