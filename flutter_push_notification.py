import json

import requests


class PushNotification:
    FCM_SERVER_KEY = "<YOUR API KEY HERE>"

    def _notify_device(self, message_title, message_body, fcm_registration_id):
        headers = {
            "Content-Type": "application/json",
            'Authorization': "key=" + self.FCM_SERVER_KEY
        }
        url = 'https://fcm.googleapis.com/fcm/send'
        body = {
            'notification': {
                'body': message_body,
                'title': message_title
            },
            'priority': 'high',
            'data': {
                'click_action': 'FLUTTER_NOTIFICATION_CLICK',
            },
            'to': fcm_registration_id,
        }
        response = requests.post(url=url, data=json.dumps(body), headers=headers)
        if response.status_code == 200:
            return True
        else:
            return False

    def alert_user(self, fcm_registration_id):
        """
        Notification is sent when a user account is created
        """
        message_title = "First Message Title🚖"
        message_body = "Thanks to CUBE ROBOTICS"
        return self._notify_device(message_title=message_title, message_body=message_body,
                                   fcm_registration_id=fcm_registration_id)
