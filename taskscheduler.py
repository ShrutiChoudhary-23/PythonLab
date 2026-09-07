tasks = []

while True:
    print("\n--- TASK SCHEDULER ---")
    print("1. Add Task")
    print("2. Run Tasks")
    print("3. Show Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add a new task
    if choice == "1":
        task = input("Enter task name: ")
        priority = input("Enter priority (high/low): ").lower()
        ready = input("Is the task ready? (yes/no): ").lower()

        # Store task information
        tasks.append([task, priority, ready])
        print("Task added successfully.")

    # Run tasks
    elif choice == "2":
        if not tasks:
            print("No tasks in the queue.")
            continue

        print("\nRunning tasks...")

        remaining_tasks = []

        for task in tasks:
            name = task[0]
            priority = task[1]
            ready = task[2]

            # Lazy evaluation using AND and OR
            if (ready == "yes" and priority == "high") or (
                ready == "yes" and priority == "low"
            ):
                print("Executing:", name)

            elif not (ready == "yes"):
                print("Skipping:", name, "- Task is not ready.")
                remaining_tasks.append(task)

            else:
                print("Skipping:", name)

        tasks = remaining_tasks

    # Display tasks
    elif choice == "3":
        if not tasks:
            print("No tasks in the queue.")
        else:
            print("\nPending Tasks:")
            for task in tasks:
                print("Task:", task[0],
                      "| Priority:", task[1],
                      "| Ready:", task[2])

    # Exit
    elif choice == "4":
        print("Exiting Task Scheduler...")
        break

    # Invalid choice
    else:
        print("Invalid choice. Please try again.")