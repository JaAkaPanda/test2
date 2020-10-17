a = 4
b = 2
c = - 3
delta = b ** 2 - 4 * a * c
sqrt_delta = delta ** 0.5
if delta < 0:
    x1 = None
    x2 = None
elif delta == 0:
    x1  = -b / 2 * a
    x2 = None
else:
    x1 = (-b - sqrt_delta) / (2 * a)
    x2 = (-b + sqrt_delta) / (2 * a)    

print ("The results are:", x1, x2)

