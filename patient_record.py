class PatientRecord:
    def __init__(self, Patient_ID, Visit_ID, Visit_time, Visit_department, Gender, Race, Age, Ethnicity, Insurance, Zip_code, Chief_complaint, Note_ID, Note_type):
        self.Patient_ID = Patient_ID
        self.Visit_ID = Visit_ID
        self.Visit_time = Visit_time
        self.Visit_department = Visit_department
        self.Gender = Gender
        self.Race = Race
        self.Age = Age
        self.Ethnicity = Ethnicity
        self.Insurance = Insurance
        self.Zip_code = Zip_code
        self.Chief_complaint = Chief_complaint
        self.Note_ID = Note_ID
        self.Note_type = Note_type

    def __str__(self):
        return f"Patient ID: {self.Patient_ID}\nVisit ID: {self.Visit_ID}\nVisit Time: {self.Visit_time}\nVisit Department: {self.Visit_department}\nGender: {self.Gender}\nRace: {self.Race}\nAge: {self.Age}\nEthnicity: {self.Ethnicity}\nInsurance: {self.Insurance}\nZip Code: {self.Zip_code}\nChief Complaint: {self.Chief_complaint}\nNote ID: {self.Note_ID}\nNote Type: {self.Note_type}"
