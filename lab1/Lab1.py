def task_1():
    n = int(input("Enter number: "))
    for i in range (0, n):
        print(i+1)

def task_2():
    x1 = int(input("Enter first number: "))
    x2 = int(input("Enter second number: "))
    print("max number is " + str(max(x1, x2)))

a = [
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 0, 1, 1],
    [1, 1, 0, 0]
]

n = 0
def f(i = 0, j = 0):
    if (i < 0) or (j < 0) or (i > 3) or (j > 3):
        return False
    if a[i][j] == 0:
        return False
    a[i][j] = 0
    destroy_neighbor(i+1, j+1)
    destroy_neighbor(i+1, j-1)
    destroy_neighbor(i-1, j+1)
    destroy_neighbor(i-1, j-1)
    return True

def destroy_neighbor(i, j):
    if (i < 0) or (j < 0) or (i > 3) or (j > 3):
        return
    if a[i][j] == 0:
        return
    a[i][j] = 0
    destroy_neighbor(i + 1, j + 1)
    destroy_neighbor(i + 1, j - 1)
    destroy_neighbor(i - 1, j + 1)
    destroy_neighbor(i - 1, j - 1)

for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        if f(i, j):
            n += 1
print(n)