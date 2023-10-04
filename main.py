# Author: Raghav Maurya
# Email : raghavmaurya201215@icloud.com
# Date  : 3 October 2023 Tuesday
print("Welcome to Kaun Banega Crore Pati")
price = 0.00

questions = [
    "Who is the prime minister of Russia?",
    "What is the capital of Germany?",
    "Who is the founder of FaceBook?",
    "What unit is water?",
    "How many seconds in 2 minute"
]
answers = [
    ["Vladimir Putin", "Paris", "Warren Buffet", "Solid", "120"],
    ["Shri Narendra Modi", "London", "Mark Zuckerberg", "Gas", "118"],
    ["Warren Buffet", "Berlin", "David Dixon", "Liquid", "150"],
    ["Raghav Maurya", "Tokyo", "Tim Cock", "None of these", "250"],
]
answerCorrect = ['vladimir putin', "berlin", 'mark zuckerberg', 'liquid', "120"]
for i in range(5):
    print(questions[i])
    for j in range(4):
        print(answers[j][i])
        if j == 4:
            break

    ans = input(">> ").lower()
    if ans == answerCorrect[i]:
        print("Good")
        price = price + 150.10
    else:
        print("You lose")

print(f"Your Reward is {price:.2f} out of 750.50")
