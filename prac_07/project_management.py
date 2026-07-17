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


def load_projects(filename=FILENAME):
    """Load projects from projects.txt"""
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

main()

