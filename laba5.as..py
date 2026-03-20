#1 - Создайте класс Employee с общими атрибутами, такими как name (имя), id (идентификационный номер) и методами, например, get_info(), который возвращает базовую информацию о сотруднике.
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def get_info(self):
        return f"Сотрудник: {self.name}, ID: {self.id}"

#2 - Создайте класс Manager с дополнительными атрибутами, такими как department (отдел) и методами, например, manage_project(), символизирующим управление проектами.
class Manager(Employee): 
    def __init__(self, name, id, department):
        Employee.__init__(self, name, id)
        self.department = department
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Отдел: {self.department}"
    def manage_project(self, project_name):
        return f"{self.name} управляет проектом '{project_name}' в отделе {self.department}"

#3 - Создайте класс Technician с уникальными атрибутами, такими как specialization (специализация), и методами, например, perform_maintenance(), означающим выполнение технического обслуживания.
class Technician(Employee):   
    def __init__(self, name, id, specialization):
        Employee.__init__(self, name, id)
        self.specialization = specialization
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Специализация: {self.specialization}"
    def perform_maintenance(self, equipment):
        return f"{self.name} выполняет обслуживание {equipment} (специализация: {self.specialization})"

#4 - Создайте класс TechManager, который наследует как Manager, так и Technician. Этот класс должен комбинировать управленческие способности и технические навыки, например, иметь методы для управления проектами и выполнения технического обслуживания.
class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Manager.__init__(self, name, id, department)
        self.specialization = specialization
        self._team = []
    
    def get_info(self):
        return (f"TechManager : {self.name}, ID: {self.id}, "
                f"Отдел: {self.department}, Специализация: {self.specialization}")

#5 - Добавьте метод add_employee(), который позволяет TechManager добавлять сотрудников в список подчинённых.
    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self._team.append(employee)
            return f"{employee.name} добавлен в команду {self.name}"
        else:
            return "Ошибка: можно добавлять только объекты типа Employee"

#6 - Реализуйте метод get_team_info(), который выводит информацию о всех подчинённых сотрудниках.
    def get_team_info(self):
        if not self._team:
            return f"У {self.name} пока нет подчиненных"
        
        team_info = f"\n{'='*60}\nКоманда менеджера {self.name}:\n{'='*60}"
        for i, employee in enumerate(self._team, 1):
            team_info += f"\n{i}. {employee.get_info()}"
        team_info += f"\n{'='*60}\nВсего сотрудников в команде: {len(self._team)}"
        return team_info
    
    def lead_technical_project(self, project_name, equipment):
        manage = self.manage_project(project_name)
        maintain = self.perform_maintenance(equipment)
        return f"{manage}\nДополнительно: {maintain}"


#7 - Создайте объекты каждого класса и демонстрируйте их функциональность.
def print_sweet_line():
    print("=" * 70)

#Создание системы и распределение ролей
def main():
    print_sweet_line()
    print("Employee management system")
    print_sweet_line()

    print("\n1. Creating a Basic Employee:")
    employee1 = Employee("Paul", "E001")
    print(employee1.get_info())

    print("\n2. Creating a Manager:")
    manager1 = Manager("Margaret", "M001", "Sales")
    print(manager1.get_info())
    print(manager1.manage_project("Expanding the customer base"))
    

    print("\n3. Creating a Technician:")
    tech1 = Technician("Leon", "T001", "Network equipment")
    print(tech1.get_info())
    print(tech1.perform_maintenance("routers Cisco"))

    print("\n4. Creation of a technical manager:")
    tech_manager = TechManager("Frank", "TM001", "IT", "System administration")
    print(tech_manager.get_info())

    print("\n5. Project management:")
    print(tech_manager.manage_project("Server upgrades"))

    print("\n6. Maintenance:")
    print(tech_manager.perform_maintenance("Server"))

    print("\n7. Technical project management:")
    print(tech_manager.lead_technical_project("Implementation of cloud solutions",
                                               "virtual machines"))

    print("\n8. Team formation:")

    emp2 = Employee("Albert", "E002")
    tech2 = Technician("Claudia", "T002", "Databases")
    tech3 = Technician("Thomas", "T003", "Web-development")
    manager2 = Manager("Cara", "M002", "Development")
    

    print(tech_manager.add_employee(emp2))
    print(tech_manager.add_employee(tech2))
    print(tech_manager.add_employee(tech3))
    print(tech_manager.add_employee(manager2))

    print("\n9. INFO:")
    print(tech_manager.get_team_info())
    

    print("\n10. Демонстрация полиморфизма (вызов get_info() для разных типов):")
    all_employees = [employee1, manager1, tech1, tech_manager, emp2, tech2, tech3, manager2]
    

main()