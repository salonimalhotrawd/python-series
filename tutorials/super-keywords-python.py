# @Program: Super Keyword in Python
# @Author: Saloni Malhotra
# @Date: 27-07-2026


class Employee:

    def __init__(self, name):
        print("Employee Class Constructor Calls")
        print("=" * 55)
        self.name = name

    def show_employee(self):
        print(f"Employee Name: {self.name}")


class Manager(Employee):

    def __init__(self, name, department):
        print("Manager Constructor\n")
        print("=" * 55)
        super().__init__(name)
        self.department = department

    def show_manager(self):
        super().show_employee()
        print(f"Department: {self.department}")


class TeamLead(Manager):

    def __init__(self, name, designation, team_size):
        print("TeamLead Constructor")
        print("=" * 55)

        super().__init__(name, designation)
        self.team_size = team_size

    def show_team(self):
        super().show_manager()
        print(f"Team Size: {self.team_size}")


lead = TeamLead("Saloni Malhotra", "Frontend", 8)
lead.show_team()
