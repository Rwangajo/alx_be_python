def calculate_area(length, width):
    area = length * width
    return area

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
result = calculate_area(length, width)

print("The area is:", result)
