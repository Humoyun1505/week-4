def hours_to_minutes(hours):
    return hours*60
def minutes_to_seconds(minutes):
    return minutes*60
def total_seconds(hours, minutes, seconds):
    total_mins = hours_to_minutes(hours) + minutes
    return minutes_to_seconds(total_mins) + seconds
def format_time(total_minutes):
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return f"{int(hours)} hours and {int(minutes)} minutes"
def can_fit_task(available_hours, task_hours, task_minutes):
    available_minutes = hours_to_minutes(available_hours)
    task_total_minutes = hours_to_minutes(task_hours) + task_minutes
    return task_total_minutes <= available_minutes
def schedule_summary(task_name, hours, minutes):
    total_secs = minutes_to_seconds(minutes)
    print(f"Task: {task_name}")
    print(f"  Duration: {int(hours)} hours, {int(minutes)} minutes")
    print(f"  Total Minutes: {minutes}")
    print(f"  Total Seconds: {total_secs}\n")      
print("TIME CONVERTER AND SCHEDULER")
print("========================================")
converted_minutes = hours_to_minutes(2.5)
print(f"Converting 2.5 hours to minutes: {converted_minutes} minutes\n")
total_secs = total_seconds(1, 45, 30)
print(f"Total seconds for 1 hour, 45 minutes, 30 seconds: {total_secs} seconds\n")
formatted_time = format_time(200)
print(f"Formatting 200 minutes: {formatted_time}\n")
fits = can_fit_task(3.5, 3, 20)
print("Can a 3 hour 20 minute task fit in 3.5 hours?")
if fits:
    print("  Yes, the task fits!\n")
else:
    print("  No, not enough time!\n")
print("SCHEDULE SUMMARIES:")
print("------------------------------")
schedule_summary("Study", 2, 30)
schedule_summary("Exercise", 0, 45)
