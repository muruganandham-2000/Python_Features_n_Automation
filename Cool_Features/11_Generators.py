# Generator
def generate_numbers(n):
    for i in range(n):
        yield i**2


for num in generate_numbers(5):
    print(num)
