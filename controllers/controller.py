import requests
from typing import Union
from api_app.models.account import AccountRead,Account
class Controller : 
    api_base_endpoint = "http://0.0.0.0:1996/"
    accounts_endpoint  = "accounsts"
    channels_endpoint = "channels"
    api_endpoint      = "apis"
    whitelist_endpoint= "whitelist_keywords"
    blacklist_endpoint= "blacklist_keywords"
    def __init__(self) : 
        self.session = requests.Session()
        self.session.headers = {
                                    'accept': 'application/json',
                                    'Content-Type': 'application/json',
                                }

    def add_accounts(self,channel_id,accounts) -> Union[dict, list] : 
        response =  self.session.post(self.api_base_endpoint+self.accounts_endpoint+"/"+str(channel_id),
                                      json=accounts)
        
        if response.status_code == 200 :
            accounts = response.json()
            return accounts
        else  :
            return response.json()
    def get_channel(channel_id)

        
        
            