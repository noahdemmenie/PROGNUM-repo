a = 1
b = 2

for k in range(99):
    c = a + b
    a = b
    b = c
print(f"100-th term = {a}")