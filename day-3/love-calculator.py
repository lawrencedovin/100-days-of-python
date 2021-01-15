print('Welcome to the Love Calculator!')
your_name = input('What is your name?\n ').lower()
partner_name = input('What is their name?\n ').lower()
combined_names = your_name + partner_name

love_scores = 0
true_count = 0
love_count = 0

for char in combined_names:
    if char in 'true':
         true_count += 1
    if char in 'love':
        love_count += 1

total_score = int(str(true_count) + str(love_count))

if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score >= 40 and total_score <= 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")