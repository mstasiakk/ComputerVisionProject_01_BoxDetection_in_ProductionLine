import os
import subprocess

# Root directory to the Labelme .exe file
LABELME_TOOL_PATH = r"C:\Users\Marcin\AppData\Local\Programs\Python\Python313\Scripts\labelme_export_json.exe"

def labelme_json_to_dataset(json_path):
    base = json_path[:-5]  # removes ".json"
    output_dir = base + "_json" # adds + "_json"
    command = [
        LABELME_TOOL_PATH,
        json_path,
        "-o",
        output_dir
    ]
    print(f"Running: {' '.join(command)}")
    result = subprocess.run(command, shell=False)
    return result.returncode

json_dir = r"D:\VisualStudioCode\Projects\CompVision_LineProduction_Project\Images\JpgImg_Plus_JsonLabels"
for filename in os.listdir(json_dir):
    if filename.endswith(".json"):
        json_file_path = os.path.join(json_dir, filename)
        print(f"Processing: {json_file_path}")
        result = labelme_json_to_dataset(json_file_path)
        if result == 0:
            print(f"Success: {filename}")
        else:
            print(f"Error with: {filename}")