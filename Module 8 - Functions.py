# Module 8 Assignment - Functions in Python
# Student Name: Anh Duc Luu Nguyen

# Define the custom function "greater-than" (using underscores for Python naming rules)
def greater_than(x, y):
    if x > y:
        return True
    else:
        return False

# --- Test Scenario 1: a = 2, b = 3 ---
a = 2
b = 3
result = greater_than(a, b)

# Print using string conversion as required by instructions
print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result))

# --- Test Scenario 2: a = 10, b = 6 ---
a = 10
b = 6
result = greater_than(a, b)

print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result))
