a = 10
b = 5
c = 3

print("a =", a, ", b =", b, ", c =", c)

result1 = a + b * c
print("a + b * c = {} + {} * {} = {}".format(a, b, c, result1))

result2 = (a + b) * c
print("(a + b) * c = ({} + {}) * {} = {}".format(a, b, c, result2))

result3 = a ** b // c
print("a * b // c = {} * {} // {} = {}".format(a, b, c, result3))

logic = a < b and b > c or a == 10
print("a < b and b > c or a == 10")
print("= {} < {} and {} > {} or {} == {}".format(a, b, b, c, a, a))
print("= {} and {} or {}".format(a < b, b > c, a == 10))
print("= {}".format(logic))
