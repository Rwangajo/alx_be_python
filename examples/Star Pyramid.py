i = 5     #(rows)
j = 1     #(row)   start from the first row

while j <= i:
    # print spaces before stars
    spaces = i - j
    while spaces > 0:
        print(" ", end="")
        spaces -= 1
    
    # Print stars (2 * row - 1 stars for a centered pyramid)
    stars = 1
    while stars <= (2 * j -1):
        print("*", end="")
        stars += 1
    
    print()  # Move to next line after printing one row
    j += 1
