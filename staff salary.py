class Staff:
    # Class variable to store the common bonus for all staff members
    bonus_percentage = 0.1  # 10% bonus

    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    @classmethod
    def set_bonus_percentage(cls, percentage):
        # Class method to set the bonus percentage for all staff members
        cls.bonus_percentage = percentage

    def calculate_total_salary(self):
        # Instance method to calculate the total salary including bonus
        bonus_amount = self.base_salary * self.bonus_percentage
        total_salary = self.base_salary + bonus_amount
        return total_salary

# Example usage:

# Create two staff members
staff1 = Staff("John", 50000)
staff2 = Staff("Jane", 60000)

# Display initial total salaries
print(f"{staff1.name}'s initial total salary: ${staff1.calculate_total_salary()}")
print(f"{staff2.name}'s initial total salary: ${staff2.calculate_total_salary()}")

# Set a common bonus percentage for all staff members using the class method
Staff.set_bonus_percentage(0.15)  # 15% bonus

# Display total salaries after changing the bonus percentage
print(f"{staff1.name}'s total salary after bonus change: ${staff1.calculate_total_salary()}")
print(f"{staff2.name}'s total salary after bonus change: ${staff2.calculate_total_salary()}")
