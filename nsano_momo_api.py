from uuid import uuid4

import requests


class MoMoApi:
    reference_number = uuid4().hex[:24]
    _url = '<ASSIGNED URL>' + "<NSANO_MOMO_API_KEY>"

    def credit(self, phone_number, amount, mno):
        """
        Sends cash from your bank account to customer's phone number
        also known as DISBURSEMENT
        :param phone_number: mtn account to receive the cash
        :param amount: Amount to be sent to account
        :param mno: Mobile Network Operator, this field specifies which mobile network field the user is using
        :return: True if transaction was successful, false otherwise
        """
        data = {
            'msisdn': phone_number,
            'amount': str(amount),
            'mno': mno,
            'kuwaita': 'mikopo',
            'refID': self.reference_number
        }
        response = requests.post(url=self._url, data=data)
        if response.status_code == 200:
            return True
        return False

    def debit(self, phone_number, amount, mno):
        """
        Money is taken from a user mobile money wallet and sent to your bank account
        :param amount: Amount to be requested from account
        :param phone_number:mtn account to request payment
        :param mno: Mobile Network Operator, this field specifies which mobile network field the user is using
        :return: True if transaction was successful, false otherwise
        """
        data = {
            'msisdn': phone_number,
            'amount': str(amount),
            'mno': mno,
            'kuwaita': 'malipo',
            'refID': self.reference_number
        }
        response = requests.post(url=self._url, data=data)
        if response.status_code == 200:
            return True
        return False
