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
                </MESSAGE>"""\

    CAMPAIGN = "coupons"

    ROUTE = (1, 4,)

    AUTH_KEYS = [
                    "164616Avg1ddsE5965cb6f", 
                    "164616ArvS3YZ6HQ5965cb75",
                    "164616A0b9jPhTWt8I5965cb78",
                    "164616As8IvQ1X53Hx5965cb7b",
                ]

    COUNTRY_CODE = 91

    def __init__(self, **kwargs):
        self.number = kwargs.get('number')
        self.sender_id = kwargs.get('sender_id')
        self.message = kwargs.get('message')
        self.route = ROUTE[0] if kwargs.get('route') == 'P' else ROUTE[1]
        self.auth_key = random.choice(AUTH_KEYS)

    def setUp(self):
        pass

    def deliver(self):
        requests.post("https://control.msg91.com/api/postsms.php", data=xml_data)