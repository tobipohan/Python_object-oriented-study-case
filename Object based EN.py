# Definisikan class Karyawan sebagai parent class
class Employee:
    def __init__(self, name, age, income, overtime_pay):
        self.name = name
        self.age = age
        self.income = income
        self.extra_income = 0
        self.overtime_pay = overtime_pay
    def overtime(self):
        self.extra_income += self.overtime_pay
    def extra_project(self, total_extra):
        self.extra_income += total_extra
    def total_income(self):
        return self.income + self.extra_income

# Definisikan class TenagaLepas sebagai child class dari class Karyawan 
class Freelancer(Employee):
    def __init__(self, name, age, income):
        super().__init__( name, age, income, 0)
    def extra_project(self, total_extra):
        self.extra_income += total_extra * 0.1

# Definisikan class AnalisData sebagai child class dari class Karyawan 
class DataAnalyst(Employee):
    def __init__(self, name, age = 21, income = 6500000, overtime_pay = 100000):
        super().__init__( name, age, income, overtime_pay)

# Definisikan class IlmuwanData sebagai child class dari class Karyawan
class DataScientist(Employee):
    def __init__(self, name, age = 25, income = 12000000, overtime_pay = 150000):
        super().__init__( name, age, income, overtime_pay)

# Definisikan class PembersihData sebagai child class dari class TenagaLepas
class DataCleaner(Freelancer):
    def __init__(self, name, age, income = 4000000):
        super().__init__( name, age, income)

# Definisikan class DokumenterTeknis sebagai child class dari class TenagaLepas
class TechnicalDocumenter(Freelancer):
    def __init__(self, name, age, income = 2500000):
        super().__init__( name, age, income)

# Definisikan class Perusahaan 
class Company:
    def __init__(self, name, adress, phone_number):
        self.name = name
        self.adress = adress
        self.phone_number = phone_number
        self.employee_list = []
    def activate_employee( self, employee):
        self.employee_list.append(employee)
    def deactivate_employee( self, employee_name):
        for employee in self.employee_list:
            if employee.name == employee_name:
                self.employee_list.remove(employee)
                break
    def total_expense (self):
        total_expense = 0
        for employee in self.employee_list:
            total_expense += employee.total_income()
        return total_expense

# Create object karyawan sesuai dengan tugasnya masing-masing
# seperti yang dinyatakan dalam tabel.
ani = DataCleaner('Ani', 25)
budi = TechnicalDocumenter('Budi', 18)
cici = DataScientist('Cici')
didi = DataScientist('Didi', 32, 20000000)
efi = DataAnalyst('Efi')
febi = DataAnalyst('Febi', 28, 12000000)

# Create object perusahaan
company = Company('ConVict', 'Seraphim street, Block 72', '(021) 99915XX')

# Aktifkan setiap karyawan yang telah didefinisikan
company.activate_employee(ani)
company.activate_employee(budi)
company.activate_employee(cici)
company.activate_employee(didi)
company.activate_employee(efi)
company.activate_employee(febi)

# Cetak keseluruhan total pengeluaran perusahaan
print(company.total_expense())