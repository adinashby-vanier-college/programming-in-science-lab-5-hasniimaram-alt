# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    if n < 2:
        return "*"
   
    result = ""
    i = 0
   
    while i < n:
        if i == 0 or i == n - 1:
            result += "*" * n  
        else:
            result += "*" + " " * (n - 2) + "*"  
        result += "\n"
        i += 1
    return result.strip()  



# 1
# 12
# 123
# 1234
def number_pattern(n):
    def generate_pattern(current, limit, result=[]):
        if current > limit:
            return '\n'.join(result)
        result.append(''.join(map(str, range(1, current + 1))))
        return generate_pattern(current + 1, limit, result)
   
    return generate_pattern(1, n)


# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    total = 0
    count = 1
    while count <= n:
        total += count
        count += 1
    return total

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = []
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        result.append(spaces + stars)
    return '\n'.join(result)