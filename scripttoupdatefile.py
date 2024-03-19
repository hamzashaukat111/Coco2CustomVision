import json

# Define base URL of your blob storage container
base_url = "https://softdeskstorage.blob.core.windows.net/testobjectdetectiondataset/"

# Path to your COCO annotation file
coco_file_path = "_updtannotations.coco.json"

# Load COCO annotation file
with open(coco_file_path, "r") as file:
    coco_data = json.load(file)

# Prepend base URL to each image filename
for image in coco_data["images"]:
    image["file_name"] = base_url + image["file_name"]

# Write updated COCO annotation file
with open(coco_file_path, "w") as file:
    json.dump(coco_data, file, indent=4)

print("Image URLs updated successfully.")
