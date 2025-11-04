def calculate_average(score1, score2, score3):
    return (score1 + score2 + score3) / 3
def drop_lowest(score1, score2, score3):
    scores = [score1, score2, score3]
    scores.remove(min(scores))
    return sum(scores) / 2
def calculate_weighted(assignments, midterm, final):
    return (assignments * 0.30) + (midterm * 0.30) + (final * 0.40)
def determine_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'
def needs_improvement(current_avg, target_grade):
    valid_grades = ['A', 'B', 'C', 'D']
    if target_grade == 'A':
        required = 90
    elif target_grade == 'B':
        required = 80
    elif target_grade == 'C':
        required = 70
    elif target_grade == 'D':
        required = 60
    else:
        return 'F'
    if current_avg < required:
        return True, round(required - current_avg, 2)
    else:
        return False, 0

a1 = 85
a2 = 78
a3 = 92
midterm_score = 88
final_score = 82
regular_avg = round(calculate_average(a1, a2, a3), 2)
dropped_avg = round(drop_lowest(a1, a2, a3), 2)
better_avg = max(regular_avg, dropped_avg)
weighted_avg = round(calculate_weighted(better_avg, midterm_score, final_score), 2)
letter = determine_grade(weighted_avg)
improve_needed, points_needed = needs_improvement(weighted_avg, 'A')
print("STUDENT GRADE CALCULATOR")
print("=" * 40)
print(f"Assignment Scores: {a1}, {a2}, {a3}")
print(f"Midterm Score: {midterm_score}")
print(f"Final Score: {final_score}")
print("-" * 40)
print(f"Regular Assignment Average: {regular_avg:.2f}")
print(f"Average with Lowest Dropped: {dropped_avg:.2f}")
print(f"Using Better Average: {better_avg:.2f}\n")
print(f"Weighted Course Average: {weighted_avg:.2f}")
print(f"Letter Grade: {letter}\n")
print(f"Needs improvement for an 'A': {'Yes' if improve_needed else 'No'}")
print(f'Points needed :{points_needed:.2f}')
print(f'Already meets or exceeds "B" grade requirement')

