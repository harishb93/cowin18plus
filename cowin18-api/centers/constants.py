import os
import json

directory = os.path.dirname(__file__)

# DISTRICT_IDS = []
# with open(os.path.join(directory, "districts/states.json")) as f:
#     states = json.load(f)
#     for state in states["states"]:
#         if state["state_name"] in ["Tamil Nadu"]:
#             with open(
#                 os.path.join(directory, f"districts/{state['state_id']}.json")
#             ) as f:
#                 districts = json.load(f)
#                 district_ids = [
#                     district["district_id"] for district in districts["districts"]
#                 ]
#                 DISTRICT_IDS.extend(district_ids)
DISTRICT_IDS = [
    571,  # Chennai
    265,  # Bangalore Urban
    395,  # Mumbai
    307,  # Ernakulam
    140,  # New Delhi
    581,  # Hyderabad
    725,  # Kolkata
]
DISTRICT_IDS_AND_DISTRICTS = [
    {"id": 571, "name": "Chennai"},
    {"id": 265, "name": "Bangalore Urban"},
    {"id": 395, "name": "Mumbai"},
    {"id": 307, "name": "Ernakulam"},
    {"id": 140, "name": "New Delhi"},
    {"id": 581, "name": "Hyderabad"},
    {"id": 725, "name": "Kolkata"},
]

DISTRICT_KEY = lambda district_id: f"DISTRICT_{district_id}"
