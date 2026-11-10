scores = input("Enter the scores separated by spaces: ")

scores = [float(score) for score in scores.split()]

if len(scores) == 0:
    print("Please enter at least one score.")
else:
    total = sum(scores)
    average = total / len(scores)
    minimum = min(scores)
    maximum = max(scores)
   

    print("Scores:", scores)
    print("Total:",total)
    print("Average:", average)
    print("Minimum:", minimum)
    print("Maximum:", maximum)
