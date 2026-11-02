marks = [int(i) for i in input().split()]
#out = {5:3, 4:2, 3:2, 2:1}

print(marks)
out = {}

for i in marks:
    if i in out:
        out[i] += 1
    else:
        out[i] = 1

print(out)
print(out[5])
