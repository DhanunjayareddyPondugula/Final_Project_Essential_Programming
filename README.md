# Final_Project_Essential_Programming
# Hospital Management System

## Introduction

This project implements a Hospital Management System in Python using the Tkinter library for the graphical user interface. It offers functionalities for managing patient records, generating key statistics, and performing various tasks based on user roles such as management, admin, nurse, and clinician.

## How to Run

1. **Clone the repository** to your local machine:

git clone https://github.com/your_username/hospital_management_system.git

2. **Navigate** to the project directory:

cd hospital_management_system

3. **Run the main program**:

python hospital_app.py

## Features

- **Management/Admin**:
- Generate key statistics related to hospital operations.
- **Nurse/Clinician**:
- Retrieve patient information.
- Add new patient records.
- Remove patient records.
- Count patient visits.

The system provides a user-friendly interface for easy interaction and management of hospital data.

## Installation

### Dependencies

- Python 3.x
- Tkinter library

Install Tkinter using pip:

pip install tk

### CSV File

Patient records are stored in a CSV file named `PA3_patients.csv`. Ensure that this file exists and has appropriate permissions for read and write operations.

Hospital role related username and passwords are stored in a csv file named `PA3_credentials.csv`. Ensure that this files exists and has appropriate permissions for read and write operations.

## Usage

1. Launch the application by running `hospital_app.py`.
2. Select your role from the login screen.
3. Use the provided interface to perform various tasks based on your role.

## Logging

The system logs usage information, including the tasks performed by users, for monitoring and auditing purposes. Log files are stored in the `logs` directory.

## Contributing

Contributions to the project are welcome. Please fork the repository, make your changes, and submit a pull request.
