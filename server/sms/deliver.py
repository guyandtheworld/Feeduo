import random
import requests


class Router(object):

    XML_DATA = """<MESSAGE> \
                        <AUTHKEY>{0}</AUTHKEY> \
                        <SENDER>{1}</SENDER> \
                        <ROUTE>{2}</ROUTE> \
                        <CAMPAIGN>{3}</CAMPAIGN> \
                        <COUNTRY>{4}</COUNTRY> \
                        <SMS TEXT="{5}"> \
                            <ADDRESS TO="{6}"></ADDRESS> \
                        </SMS> \
                  </MESSAGE>"""

    CAMPAIGN = "coupons"

    ROUTE = (1, 4,)

    AUTH_KEYS = [
                    "164616Avg1ddsE5965cb6f", 
                    "164616ArvS3YZ6HQ5965cb75",
                    "164616A0b9jPhTWt8I5965cb78",
                    "164616As8IvQ1X53Hx5965cb7b",
                ]

    COUNTRY_CODE = 91

    POST_URL = "https://control.msg91.com/api/postsms.php"

    def __init__(self, **kwargs):
        self.xml_data = self.XML_DATA
        self.auth_key = random.choice(self.AUTH_KEYS)
        self.sender_id = kwargs.get('sender_id')
        if 'route' in kwargs:
            self.route = self.ROUTE[0] if kwargs.get('route') == 'P' else self.ROUTE[1]
        else:
            self.route = self.ROUTE[0]
        self.message = kwargs.get('message')
        self.number = kwargs.get('number')

    def setUp(self):
        self.xml_data = self.xml_data.format(
                self.auth_key,
                self.sender_id,
                self.route,
                self.CAMPAIGN,
                self.COUNTRY_CODE,
                self.message,
                self.number,
            )

    def send(self):
        response = requests.post(self.POST_URL, data=self.xml_data).text
