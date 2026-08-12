class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name


class ElectricityBill(Customer):
    def __init__(self, customer_id, name, units):
        super().__init__(customer_id, name)
        self.units = units
        self.bill_amount = 0

    def calculate_bill(self):

        if self.units <= 100:
            self.bill_amount = self.units * 2

        elif self.units <= 200:
            self.bill_amount = (100 * 2) + ((self.units - 100) * 3)

        elif self.units <= 300:
            self.bill_amount = (100 * 2) + (100 * 3) + ((self.units - 200) * 5)

        else:
            self.bill_amount = (100 * 2) + (100 * 3) + (100 * 5) + ((self.units - 300) * 7)

    def display_bill(self):

        print("\n====================================")
        print("       ELECTRICITY BILL")
        print("====================================")
        print("Customer ID   :", self.customer_id)
        print("Customer Name :", self.name)
        print("Units Used    :", self.units)
        print("Bill Amount   : ₹{:.2f}".format(self.bill_amount))
        print("====================================")

    def save_to_file(self):

        with open("electricity_bill.txt", "a") as file:

            file.write("\n====================================\n")
            file.write("       ELECTRICITY BILL\n")
            file.write("====================================\n")
            file.write("Customer ID   : " + str(self.customer_id) + "\n")
            file.write("Customer Name : " + self.name + "\n")
            file.write("Units Used    : " + str(self.units) + "\n")
            file.write(
                "Bill Amount   : ₹{:.2f}\n".format(self.bill_amount)
            )
            file.write("====================================\n")

        print("\nBill saved successfully!")
        print("Data saved in electricity_bill.txt")


# Main Program

print("\n====================================")
print("   ELECTRICITY BILL CALCULATOR")
print("====================================")

customer_id = input("Enter Customer ID: ")
name = input("Enter Customer Name: ")

try:
    units = float(input("Enter Electricity Units: "))

    if units < 0:
        print("\nUnits cannot be negative.")

    else:
        # Create object
        bill = ElectricityBill(customer_id, name, units)

        # Calculate bill
        bill.calculate_bill()

        # Display bill
        bill.display_bill()

        # Save bill
        bill.save_to_file()

        print("\nThank you for using the system!")

except ValueError:
    print("\nPlease enter a valid number for electricity units.")