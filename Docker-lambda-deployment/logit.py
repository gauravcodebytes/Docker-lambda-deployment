import joblib
import pandas as pd
import json

# Load the model from a file
model = joblib.load('/var/task/logit.pkl')

def lambda_handler(event, context):
    try:
        # Read in the request body as the event dict
        if "body" in event: 
            event = event["body"]
            
            if event is not None:
                event = json.loads(event)
            else:
                event = {}
    
        if "G1" in event:
            # Create a DataFrame from the event data
            new_row = { "G1": event.get("G1"), "G2": event.get("G2"),
                        "G3": event.get("G3"), "G4": event.get("G4"),
                        "G5": event.get("G5"), "G6": event.get("G6"),
                        "G7": event.get("G7"), "G8": event.get("G8"),
                        "G9": event.get("G9"), "G10": event.get("G10")}

            new_x = pd.DataFrame([new_row])
            
            # Make prediction
            prediction = str(model.predict_proba(new_x)[0][1])
            
            return { "body": "Prediction: " + prediction }
        
        return { "body": "No parameters" }

    except Exception as e:
        # Handle exceptions and return error message
        return { "body": f"Error: {str(e)}" }

