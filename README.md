# Healthcare File Processing Tool

A Python tool that processes healthcare text files and converts patient information into structured JSON.

## Features

- Extracts patient data from text files
- Validates required fields
- Validates age
- De-identifies patient names
- Converts data to JSON
- Generates an error report

## Workflow

Text File → Extraction → Validation → De-identification → JSON

## Example

Input:

Patient Name: Ahmed Ali
Age: 31
Gender: Male
Diagnosis: Diabetes
Medication: Metformin

Output:

{
    "name": "[DE-IDENTIFIED]",
    "age": 31,
    "gender": "Male",
    "diagnosis": "Diabetes",
    "medication": "Metformin"
}

## Technologies

- Python
- JSON
- File Processing
- Data Validation
- Healthcare Data De-identification
