from pawpal_system import *

# -------------------------
# TEST SETUP (Owner, 2 pets, 3+ tasks)
# -------------------------

owner = Owner("Amelia", daily_time_available=55)

pet1 = Pet("Ani", "Dog")
pet2 = Pet("Haze", "Cat")

# Add at least 3 tasks with different durations
pet1.add_task(Task("Morning walk", duration_minutes=20, priority=5))
pet1.add_task(Task("Feed Haze", duration_minutes=5, priority=4))
pet2.add_task(Task("Clean litter box", duration_minutes=10, priority=5))
pet2.add_task(Task("Playtime with Ani", duration_minutes=15, priority=3))

owner.add_pet(pet1)
owner.add_pet(pet2)

# Generate and print today's schedule
scheduler = Scheduler()
plan, explanation = scheduler.generate_plan(owner)
print(plan, explanation)

print("=== PawPal+ Today's Schedule ===")
total = 0
for task in plan:
    print(f"[#{task.number}] {task.description} - {task.duration_minutes} min (priority {task.priority})")
    total += task.duration_minutes

print(f"\nTotal scheduled time: {total} min (out of {owner.daily_time_available} min)\n")

print("=== Reasoning ===")
for line in explanation:
    print("-", line)