import random

print("Welcome to Madlibs! It is wonderful to meet you!")
name = input("What is your name?...")
print(f"Thank you, {name}, it is so nice to meet you!!")
adj1 = input(f"{name}, kindly provide an adjective for how you think your life will go:... ").lower()
noun1 = input(f"{name}, kindly provide three feelings separated by a comma:'... ").lower()
noun1s = noun1.split(',')
print(noun1s)
noun1s = random.choice(noun1s).lower()
number = input(f"{name}, please provide a favorite number:... ").lower()
noun2 = input(f"{name}, quickly provide your favorite dog:... ").lower()
adj2 = input(f"{name}, passionately provide another feeling:... ").lower()
verb = input(f"{name}, pleasingly provide a verb that describes your action at this time: ").lower()
noun3 = input(f"{name}, kindly provide a third noun for us for the day of the week:... ").lower()
body_part = input(f"{name}, kindly and quickly describe a body part that you really love:... ").lower()
adj3 = input(f"{name}, kindly provide a third adjective that describes your rating of the performance:... ").lower()
print(f"{name}!! Here is your strange statement. Let's hope that it makes sense!!")
print(f"Hello {name}, it is highly probable that your life will be so {adj1}. I suspect that you are {noun1s}, your favorite number is {number} and I bet you hope that this is also the lottery winner for the day. It is our desire that your favorite dog, the {noun2}, is with you today. Surprise!! We have your favorite dog, the {noun2}. But I also imagine that you are very {adj2} now, please {verb} for the rest of your {noun3}, because I know, in my {body_part}, you`re the most {adj3} person for me.")
print(f"{name}, I hope that you had a great experience with our service!! I think that you have passed our initial inquiry and you have been selected to continue in our selection process!")"# Mad-Libs3" 
"# Mad-Libs3" 
