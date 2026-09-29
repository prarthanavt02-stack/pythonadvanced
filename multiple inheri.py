class Hospital:
    def __init__(self):

        self.hosp_name=input('Enter the hospital name')
        self.location=input('Enter the location')
        self.phone=int(input('Enter the phone number'))

    def display_hospital(self):
        print(self.hosp_name,self.location,self.phone)

class Department:

    def __init__(self):

        self.dept_name=input('Enter the department name')
        self.doct_name=input('Enter the doctor name')

    def display_department(self):
        print(self.dept_name,self.doct_name)


class Patient(Hospital,Department):

    def __init__(self):

        Hospital.__init__(self)
        Department.__init__(self)
        self.patient_name=input('Enter the patient name')
        self.age=int(input('Enter the age'))
        self.gender=input('Enter gender')
        self.admission_date=input('Enter the admission date')
        self.bed_no=int(input('Enter bed no'))
        self.discharge_date=""

    def full_summary(self):

        Hospital.display_hospital(self)
        Department.display_department(self)
        print('Patient Name:', self.patient_name)
        print('Age:', self.age)
        print('Gender:', self.gender)
        print('Admission Date:', self.admission_date)
        print('Bed No:', self.bed_no)
        if

    def set_discharge(self):
        self.discharge_date = input('Enter discharge date')
        print("Discharge date")

p=Patient()
p.full_summary()
p.set_discharge()