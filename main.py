import requests
import csv

def extractor_data_to_csv(url):
    try:
        # Make API request
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            if data:
                csv_file = "data.csv"

                # Extract headers from the data
                headers = data[0].keys() if isinstance(data, list) and len(data) > 0 else []

                # Open CSV file in write mode
                with open(csv_file, 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=headers)

                    # Write headers to the CSV
                    writer.writeheader()

                    # Write data rows to the CSV
                    writer.writerows(data)

                return f"Data extracted successfully and saved in {csv_file}."
            else:
                return "No data available for extraction."
        else:
            return "Failed to call the API."
    except requests.exceptions.RequestException as e:
        return f"Request error: {e}"

# Prompt the user for the API URL
url = input("Enter the API URL: ")

# Extract the data
result = extractor_data_to_csv(url)

print(result)
