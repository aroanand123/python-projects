class BloodBank:
    def __init__(self):
        self.blood_inventory = {'A+': 10, 'A-': 5, 'B+': 8, 'B-': 3, 'AB+': 12, 'AB-': 2, 'O+': 15, 'O-': 7}

    def display_inventory(self):
        print("Blood Inventory:")
        for blood_group, units in self.blood_inventory.items():
            print(f"{blood_group}: {units} units")

    def donate_blood(self, blood_group, units_donated):
        if blood_group in self.blood_inventory:
            self.blood_inventory[blood_group] += units_donated
            print(f"Thank you for donating {units_donated} units of {blood_group} blood!")
        else:
            print(f"Invalid blood group: {blood_group}")

    def request_blood(self, blood_group, units_requested):
        if blood_group in self.blood_inventory:
            available_units = self.blood_inventory[blood_group]
            if available_units >= units_requested:
                self.blood_inventory[blood_group] -= units_requested
                print(f"{units_requested} units of {blood_group} blood provided.")
            else:
                print(f"Insufficient units of {blood_group} blood available.")
        else:
            print(f"Invalid blood group: {blood_group}")


# Example usage:
blood_bank = BloodBank()

blood_bank.display_inventory()

blood_bank.donate_blood('A+', 3)
blood_bank.display_inventory()

blood_bank.request_blood('O-', 5)
blood_bank.display_inventory()