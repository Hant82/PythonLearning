from datetime import date

class Customer:
    def __init__(self, name, date_of_birth, email, phone):
        self.name = name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone = phone
    
    def get_info(self):
        return [self.name, self.date_of_birth, self.email, self.phone]

class BankAccount:
    def __init__(self, account_number, account_name, owner, balance=0):
        self._account_number = account_number
        self._account_name = account_name
        self.balance = balance
        self._owner = owner

    @property
    def account_number(self):
        return self._account_number

    @property
    def account_name(self):
        return self._account_name

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            raise ValueError("Số dư phải lớn hơn 0")

    def display(self):
        print(f"Số tài khoản khách hàng là: {self._account_number}")
        print(f"Thông tin khách hàng như sau:")
        print(
                f"1. Tên khách hàng: {self._owner.get_info()[0]}", 
                f"2. Ngày sinh: {self._owner.get_info()[1]}",
                f"3. Email: {self._owner.get_info()[2]}",
                f"4. Phone: {self._owner.get_info()[3]}",
                f"5. Số dư là:{self.balance}",
                "====================================",
                sep = '\n')
        

class SavingAccount(BankAccount):
    def __init__(self,account_number, account_name, owner, balance, monthly_interest_rate = 0.005):
        super().__init__(account_number, account_name, owner, balance)
        self._monthly_interest_rate = monthly_interest_rate
    
    def calculate_interest(self):
        interest_money = self._balance * self._monthly_interest_rate
        return interest_money
    


Ha = Customer("Nguyen Thi A","30/01/2000","abc@gmail.com","096xx")

Ha_bank = BankAccount("123456","Tai khoan cua A", Ha, 1000)

Ha_bank_interest = SavingAccount("123456","Tai khoan cua A", Ha, 70070000)
Ha_bank_interest.display()
print(f"Tiền lãi hàng tháng dự tính: {Ha_bank_interest.calculate_interest()}")






