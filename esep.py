N = int(input(" "))
array = list(map(int, input(" ").split()))
result = [array[i] for i in range(0, N, 2)]
print("", *result)