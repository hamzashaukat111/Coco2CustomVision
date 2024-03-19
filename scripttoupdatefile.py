import json

# Define base URL of your blob storage container
base_url = "https://softdeskstorage.blob.core.windows.net/augmenteddatacont/"

# Path to your COCO annotation file
coco_file_path = "_Augmentedannotations.coco.json"

# Load COCO annotation file
with open(coco_file_path, "r") as file:
    coco_data = json.load(file)

# Add coco_url field to each image entry
for image in coco_data["images"]:
    image["coco_url"] = base_url + image["file_name"]

# Write updated COCO annotation file
with open(coco_file_path, "w") as file:
    json.dump(coco_data, file, indent=4)

print("coco_url added successfully.")