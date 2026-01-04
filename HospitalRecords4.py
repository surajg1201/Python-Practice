class Patient:
    def __init__(self, pid, name, age, disease):
        self.pid = pid
        self.name = name
        self.age = age
        self.disease = disease

    def display_info(self):
        print(f"\nPatient ID: {self.pid}")
        print(f"\nName: {self.name}")
        print(f"\nAge: {self.age}")
        print(f"\nDisease: {self.disease}")
        print("*" * 30)


class Hospital:
    def __init__(self, hospital_name):
        self.hospital_name = hospital_name
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"\nPatient '{patient.name}' added successfully!")

    def show_all_patients(self):
        print(f"\nHospital: {self.hospital_name}")
        print("Patient Records:\n")
        for patient in self.patients:
            patient.display_info()


hospital = Hospital("Alchemist Hospital")

n = int(input("Enter number of patients to add: "))

for i in range(n):
    print(f"\nEnter details of patient {i+1}: ")
    pid = int(input("Patient ID: "))
    name = input("Name: ")
    age = int(input("Age: "))
    disease = input("Disease: ")

    p = Patient(pid, name, age, disease)
    hospital.add_patient(p)
hospital.show_all_patients()
