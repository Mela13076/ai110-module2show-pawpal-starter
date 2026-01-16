from pawpal_system import *

def test_ordering_by_priority_then_duration():
    """
    Tasks should be selected in order of:
    - higher priority first
    - if same priority, shorter duration first
    """
    owner = Owner("Amelia", daily_time_available=60)
    dog = Pet("Luna", "Dog")
    cat = Pet("Milo", "Cat")

    # same priority, different durations
    dog.add_task(Task("Short meds", 5, 4))
    dog.add_task(Task("Long grooming", 20, 4))

    # higher priority should come first
    cat.add_task(Task("Walk", 15, 5))

    owner.add_pet(dog)
    owner.add_pet(cat)

    plan, _ = Scheduler().generate_plan(owner)

    assert [t.description for t in plan] == ["Walk", "Short meds", "Long grooming"]


def test_respects_time_limit_and_skips_tasks_that_do_not_fit():
    owner = Owner("Amelia", daily_time_available=20)
    pet = Pet("Luna", "Dog")

    pet.add_task(Task("Walk", 25, 5))          # too long, should be skipped
    pet.add_task(Task("Feed", 5, 4))           # should fit
    pet.add_task(Task("Quick play", 10, 3))    # should fit

    owner.add_pet(pet)

    plan, explanation = Scheduler().generate_plan(owner)

    assert [t.description for t in plan] == ["Feed", "Quick play"]
    assert any("not enough time" in line for line in explanation)


def test_empty_tasks_returns_empty_plan():
    owner = Owner("Amelia", daily_time_available=30)
    plan, explanation = Scheduler().generate_plan(owner)

    assert plan == []
    # Explanation may be empty depending on implementation, so keep this flexible
    assert isinstance(explanation, list)


def test_empty_time_available_returns_empty_plan():
    owner = Owner("Amelia", daily_time_available=0)
    pet = Pet("Milo", "Cat")
    pet.add_task(Task("Feed", 5, 5))
    owner.add_pet(pet)

    plan, explanation = Scheduler().generate_plan(owner)

    assert plan == []
    assert any("not enough time" in line for line in explanation)


def test_completed_tasks_are_skipped():
    owner = Owner("Amelia", daily_time_available=30)
    pet = Pet("Luna", "Dog")

    t1 = Task("Walk", 15, 5)
    t2 = Task("Feed", 5, 4)
    t1.mark_complete()  # should be skipped

    pet.add_task(t1)
    pet.add_task(t2)
    owner.add_pet(pet)

    plan, explanation = Scheduler().generate_plan(owner)

    assert [t.description for t in plan] == ["Feed"]
    assert any("already completed" in line for line in explanation)


def test_task_numbers_are_unique_across_instances():
    # Create multiple tasks and ensure their numbering increments
    t1 = Task("A", 5, 1)
    t2 = Task("B", 5, 1)
    t3 = Task("C", 5, 1)

    assert len({t1.number, t2.number, t3.number}) == 3
    assert t1.number < t2.number < t3.number

def test_task_mark_complete_sets_completed_true():
    task = Task("Feed pet", duration_minutes=5, priority=3)
    assert task.completed is False

    task.mark_complete()
    assert task.completed is True


def test_adding_task_to_pet_increases_task_count():
    pet = Pet("Luna", "Dog")
    assert len(pet.tasks) == 0

    pet.add_task(Task("Morning walk", duration_minutes=20, priority=5))
    pet.add_task(Task("Evening walk", duration_minutes=20, priority=2))
    pet.add_task(Task("Night walk", duration_minutes=20, priority=5))
    assert len(pet.tasks) == 3

