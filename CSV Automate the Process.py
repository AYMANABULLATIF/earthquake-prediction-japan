import re
import csv
import os

# Base directory where the extracted folders are located
base_dir = r'C:\Users\aeman\OneDrive\Desktop\earthquake-prediction-japan\extracted_files'
log_file_path = os.path.join(base_dir, 'non_matching_lines.log')

# Function to parse a line from the data file
def parse_line(line):
    # Expanded regular expression for more flexible matching
    match = re.match(
        r"^A(\d{12,15})\s+"  # Timestamp
        r"(\d{2,3})?\s*"  # Optional latitude degrees
        r"(\d{4,7})?\s*"  # Optional latitude minutes/seconds
        r"(\d{2,3})?\s*"  # Optional longitude degrees
        r"(\d{4,7})?\s*"  # Optional longitude minutes/seconds
        r"(\d{2,3})?\s*"  # Optional depth or another value
        r"(\d+)?\s*"  # Optional intensity
        r"(\d+)?\s*"  # Optional magnitude
        r"(.+?)?\s+"  # Location description (may include spaces)
        r"(\d[NKS]?)?$",  # Metadata (optional)
        line.strip()
    )
    
    if match:
        # Extract the components
        timestamp = match.group(1)
        latitude = match.group(3) or "N/A"
        longitude = match.group(5) or "N/A"
        intensity = match.group(7) or "N/A"
        location_description = match.group(9).strip() if match.group(9) else "Unknown"
        metadata = match.group(10) or "N/A"

        # Convert the timestamp to a more readable format if needed
        if len(timestamp) >= 14:
            formatted_timestamp = (
                f"{timestamp[:4]}-{timestamp[4:6]}-{timestamp[6:8]} "
                f"{timestamp[8:10]}:{timestamp[10:12]}:{timestamp[12:]}"
            )
        else:
            formatted_timestamp = f"{timestamp[:4]}-{timestamp[4:6]}-{timestamp[6:8]}"

        return [
            formatted_timestamp,
            latitude,
            longitude,
            intensity,
            location_description,
            metadata,
        ]
    else:
        # Log non-matching lines
        with open(log_file_path, 'a') as log_file:
            log_file.write(f"Line did not match: {line.strip()}\n")
        return None

# Loop through each folder in the base directory
for folder in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder)
    
    if os.path.isdir(folder_path):
        # Loop through each .dat file in the current folder
        for filename in os.listdir(folder_path):
            if filename.endswith('.dat'):
                dat_file_path = os.path.join(folder_path, filename)
                csv_file_path = os.path.join(folder_path, f'{os.path.splitext(filename)[0]}.csv')

                with open(dat_file_path, "r", encoding="shift_jis") as infile, open(
                    csv_file_path, "w", newline="", encoding="shift_jis"
                ) as outfile:  # Writing the CSV in Shift-JIS
                    csv_writer = csv.writer(outfile)
                    csv_writer.writerow(
                        [
                            "Timestamp",
                            "Latitude",
                            "Longitude",
                            "Intensity",
                            "Location Description",
                            "Metadata",
                        ]
                    )

                    for line in infile:
                        parsed_data = parse_line(line)
                        if parsed_data:
                            csv_writer.writerow(parsed_data)

print("All .dat files have been processed and saved as CSV files. Check the log file for non-matching lines.")

