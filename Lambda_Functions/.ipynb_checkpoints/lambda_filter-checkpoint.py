import json

THRESHOLD = 0.75

def lambda_handler(event, context):
    raw = event['inferences']

    # Decode if needed from bytes to string
    if isinstance(raw, bytes):
        raw = raw.decode("utf-8")
    
    # Parse JSON string into list
    if isinstance(raw, str):
        inferences = json.loads(raw)
    else:
        inferences = raw  # already a list

    # Get the max confidence and the index of the top prediction
    max_confidence = max(inferences)
    vehicle_index = inferences.index(max_confidence)

    # Define known suspicious vehicle classes
    index_to_vehicle = {
        0: "bicycle",
        1: "bus",
        2: "motorcycle",
        3: "pickup_truck",
        4: "tractor",
        5: "tank"
    }

    if max_confidence >= THRESHOLD and vehicle_index in index_to_vehicle:
        vehicle = index_to_vehicle[vehicle_index]
        message = f'Suspicious {vehicle} detected!'
        suspicious = True
    else:
        vehicle = 'unknown'
        message = 'No suspicious vehicle detected'
        suspicious = False

    # Update and return
    event['suspicious'] = suspicious
    event['predicted_vehicle'] = vehicle
    event['message'] = message
    event['confidence'] = max_confidence
    event['inferences'] = inferences

    return event