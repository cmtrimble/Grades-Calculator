# Initialize an empty list to store assignment scores
assignment_scores = []

# Input assignment details
while True:
    assignment_type = input("Enter assignment type (or 'calculate' to see the result): ")
    if assignment_type.lower() == "calculate":
        break  # Exit the loop
    try:
        points_possible = float(input(f"Enter points possible for {assignment_type}: "))
        num_assignments = int(input(f"Enter number of {assignment_type}: "))
        scores = [float(input(f"Enter score {i + 1} for {assignment_type}: ")) for i in range(num_assignments)]
        assignment_scores.append((assignment_type, points_possible, scores))
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Calculate the unweighted total
total_points_earned = sum(sum(scores) for _, _, scores in assignment_scores)

# Calculate the total points possible
total_points_possible = sum(points_possible for _, points_possible, _ in assignment_scores)

# Calculate the final percentage
final_percentage = (total_points_earned / total_points_possible) * 100

# Determine the final grade (you can customize the grade boundaries)
if final_percentage >= 90:
    final_grade = 'A'
elif final_percentage >= 80:
    final_grade = 'B'
elif final_percentage >= 70:
    final_grade = 'C'
elif final_percentage >= 60:
    final_grade = 'D'
else:
    final_grade = 'F'

# Display individual assignment points
for assignment_type, _, scores in assignment_scores:
    print(f"Your total {assignment_type.lower()} points equals: {sum(scores):.2f}")

print(f"Total points earned: {total_points_earned:.2f}")
print(f"Total points possible: {total_points_possible:.2f}")
print(f"Final Percentage: {final_percentage:.2f}%")
print(f"Final Grade: {final_grade}")
