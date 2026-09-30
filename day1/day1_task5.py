# Pomodoro 5: Highest and lowest score
# Same list, test_scores = [95, 82, 71, 60, 45, 100, 79, 88]. This time, without using any built-in shortcut function, find and print the highest score and the lowest score by looping through the list yourself.
# Rules for this one:
# No max() or min(), even though Python has them, you're building the underlying logic by hand this time, same reason you're not allowed to use sum() for this specific task even though you now know it exists
# Print both values at the end, clearly labeled

test_scores = [95, 82, 71, 60, 45, 100, 79, 88]
highest_score = test_scores[0]
lowest_score = test_scores[0]

for n in test_scores:
    if n > highest_score:
        highest_score = n

    if n < lowest_score:
        lowest_score = n

print(highest_score)
print(lowest_score)
