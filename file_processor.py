import json
import os

INPUT_FOLDER = "."
OUTPUT_FOLDER = "processed_files"
ERROR_FILE = "error_report.txt"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

with open(ERROR_FILE, "w") as error_file:
    error_file.write("FILE PROCESSING ERROR REPORT\n")
    error_file.write("============================\n")

for filename in os.listdir(INPUT_FOLDER):

    if not filename.endswith(".txt") or filename == ERROR_FILE:
        continue

    with open(filename, "r") as file:
        content = file.read()

    patient_data = {}

    for line in content.splitlines():
        if ": " in line:
            key, value = line.split(": ", 1)
            key = key.lower().replace("patient ", "")
            patient_data[key] = value

    required_fields = [
        "name",
        "age",
        "gender",
        "diagnosis",
        "medication"
    ]

    errors = []

    for field in required_fields:
        if field not in patient_data or not patient_data[field]:
            errors.append("Missing: " + field)

    if "age" in patient_data:
        try:
            patient_data["age"] = int(patient_data["age"])

            if patient_data["age"] <= 0:
                errors.append("Age must be greater than 0")

        except ValueError:
            errors.append("Age must be a number")

    if errors:
        with open(ERROR_FILE, "a") as error_file:
            error_file.write("\nFile: " + filename + "\n")
            for error in errors:
                error_file.write("- " + error + "\n")
        continue

    patient_data["name"] = "[DE-IDENTIFIED]"

    output_filename = filename.replace(".txt", ".json")
    output_path = os.path.join(OUTPUT_FOLDER, output_filename)

    with open(output_path, "w") as file:
        json.dump(patient_data, file, indent=4)

print("File processing completed.")
