#project euler1
target = 999
total = 0
for i in range(1, target + 1): 
  if i % 3 0 or i % 5 == 0: 
    total += i
print(total)


#project euler2
limit = 4_000_000

a, b = 1, 2
total = 0

while a <= limit:
  if a % 2 == 0:
    total += a
    a, b = b, a + b

print(total)
