from prac_07.project import Project

FILENAME = "projects.txt"

def main():
    projects = load_projects()

    MENU = """\nMenu:
    L - Load projects
    S - Save projects
    D - Display projects
    F - Filter projects by date
    A - Add new project
    U - Update project
    Q - Quit"""
    choice = ""
    while choice.upper() != "Q":
        print(MENU)
        choice = input(">>> ").upper()
        if choice == "L":
            filename = input("Filename to load: ")
            projects = load_projects(filename)
        elif choice == "S":
            filename = input("Filename to save: ")
            save_projects(projects, filename)
        # elif choice == "D":
        #     display_projects(projects)
        # elif choice == "F":
        #     filter_projects_by_date(projects)
        # elif choice == "A":
        #     add_new_project(projects)
        # elif choice == "U":
        #     update_project(projects)
        # elif choice == "Q":
        #     save_choice = input("Save to default file before quitting? (Y/N): ").upper()
        #     if save_choice == "Y":
        #         save_projects(projects)
        #     print("Goodbye!")
        else:
            print("Invalid choice")


def load_projects(filename=FILENAME):
    """Load projects from projects.txt and store list of project objects"""
    projects = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # skip header
        for line in in_file:
            parts = line.strip().split('\t')
            if len(parts) == 5:
                name, start_date, priority, cost_estimate, completion = parts
                projects.append(Project(name, start_date, priority, cost_estimate, completion))
    print(f"Loaded {len(projects)} projects from {filename}")
    return projects


def save_projects(projects, filename=FILENAME):
    """Save projects in the txt file"""
    with open(filename, "w", encoding="utf-8-sig") as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}")
    print(f"Projects saved to {filename}")
main()

