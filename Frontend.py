from FrontendInterface import FrontendInterface

class Frontend(FrontendInterface):
    def __init__(self, backend):
        self.backend = backend

    def run(self):
        print("Welcome to the UW Path Finder!")
        start = input("Enter the start location: ")
        goal = input("Enter the goal location: ")

        print(f"Finding path from {start} to {goal}...")
        path = self.backend.get_path(start, goal)

        if path:
            print("Path found:", " -> ".join(path))
        else:
            print(f"No path found from {start} to {goal}.")
