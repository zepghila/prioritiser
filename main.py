# import itertools
# import matplotlib.pyplot as plt

# def rank_tasks(tasks, criterion):
#     ranked_tasks = {}
#     for task1, task2 in itertools.combinations(tasks, 2):
#         print(f"Which task is more {criterion}?")
#         print(f"1: {task1}")
#         print(f"2: {task2}")
#         choice = input("Enter 1 or 2: ")
#         if choice == '1':
#             ranked_tasks[task1] = ranked_tasks.get(task1, 0) + 1
#         elif choice == '2':
#             ranked_tasks[task2] = ranked_tasks.get(task2, 0) + 1
#     return sorted(ranked_tasks.items(), key=lambda x: x[1], reverse=True)

# def main():
#     tasks = input("Enter the list of tasks separated by commas: ").split(',')
#     tasks = [task.strip() for task in tasks]

#     print("\n--- Ranking by Urgency ---")
#     urgency_ranking = rank_tasks(tasks, "urgent")

#     print("\n--- Ranking by Importance ---")
#     importance_ranking = rank_tasks(tasks, "important")

#     urgency_dict = {k: v for k, v in urgency_ranking}
#     importance_dict = {k: v for k, v in importance_ranking}

#     plt.figure(figsize=(10, 10))

#     for task in tasks:
#         plt.scatter(urgency_dict.get(task, 0), importance_dict.get(task, 0))
#         plt.text(urgency_dict.get(task, 0), importance_dict.get(task, 0), task)

#     plt.xlabel('Urgency')
#     plt.ylabel('Importance')
#     plt.title('Task Prioritization')
#     plt.grid(True)
#     plt.show()

# if __name__ == "__main__":
#     main()

import itertools
import random
import matplotlib.pyplot as plt

def rank_tasks(tasks, criterion, description):
    ranked_tasks = {task: 0 for task in tasks}  # Initialize all tasks with a count of zero.
    total_questions = len(list(itertools.combinations(tasks, 2)))
    question_count = 0

    print(f"--- Ranking by {criterion} ---")
    print(description)

    for task1, task2 in itertools.combinations(tasks, 2):
        question_count += 1
        options = [task1, task2]
        random.shuffle(options)

        print(f"Which task is more {criterion}? [{question_count} of {total_questions}]")
        print(f"1: {options[0]}")
        print(f"2: {options[1]}")
        
        while True:
            try:
                choice = input("Enter 1 or 2: ")
                if choice not in ['1', '2']:
                    raise ValueError("Invalid input. Please enter either 1 or 2.")
                break
            except ValueError as e:
                print(e)

        selected_task = options[int(choice) - 1]
        ranked_tasks[selected_task] = ranked_tasks.get(selected_task, 0) + 1

    return sorted(ranked_tasks.items(), key=lambda x: x[1], reverse=True)

def main():
    tasks = input("Enter the list of tasks separated by commas: ").split(',')
    tasks = [task.strip() for task in tasks]

    urgency_description = "Tasks that require immediate attention and are often associated with deadlines or time-sensitive opportunities."
    importance_description = "Tasks that contribute to long-term goals and have significant impact on your role and objectives."

    urgency_ranking = rank_tasks(tasks, "urgent", urgency_description)
    importance_ranking = rank_tasks(tasks, "important", importance_description)

    print("\n--- Ranked by Urgency ---")
    for i, (task, count) in enumerate(urgency_ranking):
        print(f"{i+1}. {task} (Count: {count})")

    print("\n--- Ranked by Importance ---")
    for i, (task, count) in enumerate(importance_ranking):
        print(f"{i+1}. {task} (Count: {count})")

    urgency_dict = {k: v for k, v in urgency_ranking}
    importance_dict = {k: v for k, v in importance_ranking}

    plt.figure(figsize=(10, 10))

    for task in tasks:
        plt.scatter(urgency_dict.get(task, 0), importance_dict.get(task, 0))
        plt.text(urgency_dict.get(task, 0), importance_dict.get(task, 0), task)

    plt.xlabel('Urgency')
    plt.ylabel('Importance')
    plt.title('Task Prioritization')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
