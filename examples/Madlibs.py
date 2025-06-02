# Mad Libs Story Generator with Conditionals

# Prompt the user for words
weather_adj = input("Enter an adjective to describe the weather: ")
monkey_adj = input("Enter an adjective to describe a monkey: ")
lion_adj = input("Enter an adjective to describe a lion: ")
experience_adj = input("Enter another adjective to describe the experience: ")
favorite_animal = input("What is your favorite animal? ")
favorite_color = input("What is your favorite color? ")
visit_type = input("Would you rather have a calm or adventurous zoo visit? (calm/adventurous): ").lower()

# Story base
story = f"\nOn a beautiful {weather_adj} day, I went to the zoo. "
story += f"I saw a funny {monkey_adj} monkey swinging from the trees. "
story += f"Then, I spotted a majestic {lion_adj} lion lounging in the sun. "
story += f"What a wild and {experience_adj} experience! "

# Conditional touches
if visit_type == "adventurous":
    story += f"Suddenly, a {favorite_color} {favorite_animal} escaped its enclosure and started dancing! "
    story += "Everyone laughed and took out their phones to record the moment."
elif visit_type == "calm":
    story += f"I spent the rest of the afternoon quietly watching a {favorite_color} {favorite_animal} nap peacefully. "
    story += "It was the most relaxing part of my day."
else:
    story += "The rest of the visit was pretty uneventful, but still enjoyable."

# Final touch
story += "\n\nI can't wait to go back to the zoo again!"

# Print the story
print("\nHere's your Mad Libs story:")
print(story)
