import json

import requests


class SmsApi:
    _headers = {'content-type': 'application/json',
                'X-SMS-Apikey': "<NSANO_SMS_API_KEY>"}
    _url = "https://mysms.nsano.com/api/v1/sms/single"

    def _send_sms(self, recipient, msg):
        """
        Makes API request to NSANO SMS API endpoint
        :param recipient: Phone number for SMS to be sent to.
        :param msg: Message to be sent to recipient
        :return: True for successful request code 200, False otherwise
        """
        data = {'sender': "<Registered Name with NSANO>", 'recipient': recipient, 'message': msg}
        response = requests.post(url=self._url, data=json.dumps(data), headers=self._headers)
        if response.status_code == 200:
            return True
        return False

    def verification_sms(self, recipient, code, ):
        """
         SENDS SMS TO USER WITH VERIFICATION CODE TO VERIFY PHONE NUMBER
        :param recipient: phone number for SMS to be sent to.
        :param code: User profile verification code

        :return:
        """
        message = f"Hello Keezy,\nUse this activation code: {code} to verify your account, keep it secret."
        return self._send_sms(recipient, message)
