class ElectricityBillGenerator:
    def __init__(self, customer_name, customer_id, units_consumed):
        self.customer_name = customer_name
        self.customer_id = customer_id
        self.units_consumed = units_consumed
        self.rate_per_unit = 0.12  # Replace with your actual rate per unit

    def calculate_bill(self):
        total_amount = self.units_consumed * self.rate_per_unit
        return total_amount

    def generate_bill_statement(self):
        bill_statement = f"Electricity Bill\nCustomer Name: {self.customer_name}\nCustomer ID: {self.customer_id}\n"
        bill_statement += f"Units Consumed: {self.units_consumed} kWh\nRate per Unit: ${self.rate_per_unit:.2f}\n"
        bill_statement += f"Total Amount: ${self.calculate_bill():.2f}"
        return bill_statement

# Example Usage
customer_name = input("Enter customer name: ")
customer_id = input("Enter customer ID: ")
units_consumed = float(input("Enter units consumed: "))

bill_generator = ElectricityBillGenerator(customer_name, customer_id, units_consumed)
bill_statement = bill_generator.generate_bill_statement()

print("\n", bill_statement)