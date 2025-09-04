tasks = []

while True:
  action = input("Add task (a), Show tasks (s), Exit (e):").lower()

  if action =="a":
    task = input("Enter task:")
    tasks.append(task)
    print(f"Task added: {task}")

  elif action =="s":
    if not tasks:
      print("No tasks yet.")
    else:
      print("\n Your Task: ")
      for i,t in enumerate(tasks,1):
        print(f"{i}. {t}")

  elif action == "e":
    print(" Goodbye!")
    break

  else:
    print(" Invalid choice.Try again.")
