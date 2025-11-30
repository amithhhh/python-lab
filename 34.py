class Bank:
	def __init__(self, name, accno, acctype, balence):
		self.name = name
		self.accno = accno
		self.acctype = acctype
		self.balence = balence
	def deposit(self, amount):
		self.balence += amount
	def withdraw(self, amount):
		if amount > self.balence:
			print("[-]Sorry, Not sufficient balence");
		else:
			self.balence -= amount
	def display(self):
		print("Bank Details: ")
		print(f"name: {self.name}")
		print(f"accno: {self.accno}")
		print(f"acctype: {self.acctype}")
		print(f"balence: {self.balence}")

client = Bank("Kroos", 1234, "Fixed Deposit", 1000)

client.display()

choice = input("Enter the choice(deposit/withdraw): ")

if choice == "deposit":
	amount = int(input("Enter the amount to deposit: "))
	client.deposit(amount)
	client.display()
elif choice  == "withdraw":
	amount = int(input("Enter the amount to withdraw: "))
	client.withdraw(amount)
	client.display()
else:
	print("[-]Wrong choice.")
