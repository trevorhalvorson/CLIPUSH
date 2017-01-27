from pushy import PushyAPI
import json
import uuid


def lambda_handler(event, context):
    # Send the push notification with Pushy
    response = PushyAPI.send_push_notification(event)
    result = json.dumps(
        {
            'success': response.status_code == 200,
            'id': str(uuid.uuid4())
        }
    )
    return result
