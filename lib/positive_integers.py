def positive_integers(a, b, c):
    positive_sum = (a > 0)+(b > 0)+(c > 0)
    return positive_sum == 2


result = positive_integers(-4, 8, -2)
print(result)
