import requests
from typing import Union
from models.channel import ChannelRead
from models.account import AccountRead,Account
from loguru import logger
logger.add("bot.log",format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {function} | {message}",colorize=False,enqueue=True,mode="w")
class Controller : 
    api_base_endpoint = "http://0.0.0.0:1996/"
    accounts_endpoint  = "accounts"
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
        logger.info(f"adding accounts to channel_id : {channel_id} accounts_number : {len(accounts)}")
        try : 
            response =  self.session.post(self.api_base_endpoint+self.accounts_endpoint+"/"+str(channel_id),
                                        json=accounts)
            if response.status_code == 200 :
                accounts = response.json()
                logger.info(f"adding successfully")
                return accounts
            else  :
                logger.info(f"error occured error_code {response.status_code} detail : {response.json()['detail']}")
                return response.json()
        except Exception as e : 
            logger.error(f"unexpected error {str(e)}")
    def get_channel(self,channel_id) -> Union[dict, list] : 
        logger.info(f"get channel channel_id : {channel_id} ")
        try : 
            response =  self.session.get(self.api_base_endpoint+self.channels_endpoint+"/"+str(channel_id))
            if response.status_code == 200 :
                channel = response.json()
                print(channel)
                logger.info(f"gettings channel successfully")
                return channel
            else  :
                logger.info(f"error occured error_code {response.status_code} detail : {response.json()['detail']}")
                return response.json()
        except Exception as e : 
            logger.error(f"unexpected error {str(e)}")
    def change_channel_status(self,channel_id,status : bool) -> Union[bool,dict] : 
        try : 
            logger.info(f"change channel status channel_id : {channel_id} status : {str(status)}")
            response =  self.session.post(self.api_base_endpoint+self.channels_endpoint+"/channel_status"+"/"+str(channel_id),
                                         params={"status" : status,})
            if response.status_code == 200 :
                return True
            else :
                logger.info(f"error occured error_code {response.status_code} detail : {response.json()['detail']}")
        except Exception as e : 
            logger.error(f"unexpected error {str(e)}")
    def change_replies_status(self,channel_id,status : bool) -> Union[bool,dict] : 
        try : 
            logger.info(f"change channel replies channel_id : {channel_id} status : {str(status)}")
            response =  self.session.post(self.api_base_endpoint+self.channels_endpoint+"/replies_status"+"/"+str(channel_id),
                                         params={"status" : status,})
            if response.status_code == 200 :
                return True
            else :
                logger.info(f"error occured error_code {response.status_code} detail : {response.json()['detail']}")
        except Exception as e : 
            logger.error(f"unexpected error {str(e)}")
    def change_blacklist_status(self,channel_id,status : bool) -> Union[bool,dict] : 
        try : 
            logger.info(f"change channel blacklist channel_id : {channel_id} status : {str(status)}")
            response =  self.session.post(self.api_base_endpoint+self.channels_endpoint+"/blacklist_status"+"/"+str(channel_id),
                                         params={"status" : status,})
            if response.status_code == 200 :
                return True
            else :
                logger.info(f"error occured error_code {response.status_code} detail : {response.json()['detail']}")
        except Exception as e : 
            logger.error(f"unexpected error {str(e)}")
    
    


            


            