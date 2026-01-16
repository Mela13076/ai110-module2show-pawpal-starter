# Diagram

classDiagram
    class Task {
        +description: str
        +duration_minutes: int
        +priority: int
        +frequency: str
        +completed: bool
        +mark_complete() void
        +mark_incomplete() void
    }

    class Pet {
        +name: str
        +species: str
        +tasks: list~Task~
        +add_task(task: Task) void
        +remove_task(task_description: str) bool
        +get_tasks() list~Task~
    }

    class Owner {
        +name: str
        +daily_time_available: int
        +pets: list~Pet~
        +add_pet(pet: Pet) void
        +get_all_tasks() list~Task~
    }

    class Scheduler {
        +generate_plan(owner: Owner) tuple~list~Task~, list~str~~
    }

    Owner "1" --> "0..*" Pet : owns
    Pet "1" --> "0..*" Task : has
    Scheduler ..> Owner : uses constraints
    Scheduler ..> Task : schedules


