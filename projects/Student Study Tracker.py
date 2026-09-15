subjects = {}

def add_subject():
    name = input("Enter subject: ").title()
    topics = input("Enter topics(comma separated): ").split(",")

    subjects[name] = {
        "topics":[t.strip() for t in topics],
        "completed": set()
    }
    print("subjectadded!")

def complete_topic():
    name = input("Enter subject: ").title()
    if name not in subjects:
        print("subject not found!")
        return
    print(subjects[name]["topics"])
    topic = input("Enter completed topic: ").strip()
    if topic in subjects[name]["topics"]:
        subjects[name]["completed"].add(topic)
        print("topic compeleted!")
    else:
        print("topic not found!")

def progress():
    for name, data in subjects.items():
        total = len(data["topics"])
        done = len(data["completed"])
        percent = (done / total)*100
        print(f"\n{name}")
        print(f"completed: {done} / {total}")
        print(f"progress: {percent:.0f}%")

while True:
    print("\n1. Add subject")
    print("2. complete topic")
    print("3. View progress")
    print("4. Exit")

    choice = input("choose:")

    if choice == "1":
        add_subject()
    elif choice == "2":
        complete_topic()
    elif choice == "3":
        progress()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")

