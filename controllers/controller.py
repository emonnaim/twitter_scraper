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
                logger.info(f"error occured error_code : {response.status_code} detail : {response.json()['detail']}")
                return response.json()
        except Exception as e : 
            logger.error(f"unexpected error {str(e)}")
    def get_channel(self,channel_id) -> Union[dict, list] : 
        logger.info(f"get channel channel_id : {channel_id} ")
        try : 
            response =  self.session.get(self.api_base_endpoint+self.channels_endpoint+"/"+str(channel_id))
            if response.status_code == 200 :
                channel = response.json()
                logger.info(f"gettings channel successfully")
                return channel
            else  :
                logger.info(f"error occured error_code : {response.status_code} detail : {response.json()['detail']}")
                return response.json()
        except Exception as e : 
            logger.error(f"unexpected error {str(e)}")
    def change_channel_status(self,channel_id,status : bool) -> Union[bool,dict] : 
        try : 
            logger.info(f"change channel status channel_id : {channel_id} status : {str(status)}")
            response =  self.session.post(self.api_base_endpoint+self.channels_endpoint+"/channel_status"+"/"+str(channel_id),
                                         params={"status" : status,})
            if response.status_code == 200 :
                logger.info(f"change channel status successfully")
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
                logger.info(f"change replies status successfully")
                return True
            else :
                logger.info(f"error occured error_code : {response.status_code} detail : {response.json()['detail']}")
        except Exception as e : 
            logger.error(f"unexpected error {str(e)}")
    def change_blacklist_status(self,channel_id,status : bool) -> Union[bool,dict] : 
        try : 
            logger.info(f"change channel blacklist channel_id : {channel_id} status : {str(status)}")
            response =  self.session.post(self.api_base_endpoint+self.channels_endpoint+"/blacklist_status"+"/"+str(channel_id),
                                         params={"status" : status,})
            if response.status_code == 200 :
                logger.info(f"change blacklist status successfully")
                return True
            else :
                logger.info(f"error occured error_code : {response.status_code} detail : {response.json()['detail']}")
        except Exception as e : 
            logger.error(f"unexpected error {str(e)}")

    def change_tweet_type(self,channel_id,tweet_type) : 
        try :
            logger.info(f"change tweet type channel_id : {channel_id} tweet_type : {str(tweet_type)}")
            response =  self.session.post(self.api_base_endpoint+self.channels_endpoint+"/tweet_type"+"/"+str(channel_id),
                                         params={"tweet_type" : tweet_type,})
            if response.status_code == 200 :
                logger.info(f"change tweet type successfully")
                return True
            else : 
                logger.info(f"error occured error_code : {response.status_code} detail : {response.json()['detail']}")
        except Exception as e : 
            logger.error(f"unexpected error {str(e)}")
    
    def change_retweet_status(self,username) : 
        try : 
            print(1)
        except Exception as e : 
            logger.error(f'unexpected error {str(e)}')
    
    def get_keywords(self,keyword_type,channel_id) : 
        try : 
            logger.info(f"get keywords channel_id : {channel_id}  type : {keyword_type}")
            response =  self.session.get(self.api_base_endpoint+f"{str(keyword_type)}_keywords"+"/"+str(channel_id))
            if response.status_code == 200 :
                keywords = response.json()
                logger.info(f"get keywords successfully")
                return keywords
            else : 
                logger.info(f"error occured error_code : {response.status_code} detail : {response.json()['detail']}")
        except Exception as e : 
            logger.error(f'unexpected error {str(e)}')

    def add_keyword(self,keyword,keyword_type,channel_id) : 
        try : 
            logger.info(f"add keyword type channel_id : {channel_id} keyword : {str(keyword)} type : {keyword_type}")
            response =  self.session.post(self.api_base_endpoint+f"{str(keyword_type)}_keywords"+"/"+str(channel_id),
                                          json=[keyword])
            if response.status_code == 200 :
                logger.info(f"add keyword successfully")
                return True
            else : 
                logger.info(f"error occured error_code : {response.status_code} detail : {response.json()['detail']}")
        except Exception as e : 
            logger.error(f'unexpected error {str(e)}')

    def delete_keyword(self,keyword,keyword_type,channel_id) : 
        try : 
            logger.info(f"delete keyword type channel_id : {channel_id} keyword : {str(keyword)} type : {keyword_type}")
            response =  self.session.delete(self.api_base_endpoint+f"{str(keyword_type)}_keywords"+"/"+str(channel_id),
                                          json=[keyword])
            if response.status_code == 200 :
                logger.info(f"delete keyword successfully")
                return True
            else : 
                logger.info(f"error occured error_code : {response.status_code} detail : {response.json()['detail']}")
        except Exception as e : 
            logger.error(f'unexpected error {str(e)}')

    def get_apis(self) : 
        try : 
            logger.info("get apis")
            response = self.session.get(self.api_base_endpoint+self.api_endpoint)
            if response.status_code == 200 : 
                logger.info(f"get apis successfully")
                return response.json()
            else : 
                logger.info(f"error occured error_code : {response.status_code} detail : {response.json()['detail']}")
        except Exception as e : 
            logger.error(f'unexpected error {str(e)}')
    def select_api(self,channel_id,api_id) : 
        try : 
            logger.info(f"select api for channel_id : {channel_id} api_id : {api_id}")
            response =  self.session.post(
                url=self.api_base_endpoint+self.api_endpoint+"/select_api/"+str(channel_id),
                params={"api_id": int(api_id)}
            )
            if response.status_code == 200 : 
                logger.info(f"select api successfully")
                return True
            else : 
                logger.info(f"error occured error_code : {response.status_code} detail : {response.json()['detail']}")
        except Exception as e : 
            logger.error(f'unexpected error {str(e)}')

    def delete_api(self,api_id) : 
        try : 
            logger.info(f"delete api api_id {api_id}")
            response = self.session.delete(self.api_base_endpoint+self.api_endpoint+f"/{str(api_id)}")
            if response.status_code == 200 : 
                logger.info(f"delete api successfully")
                return True
            else : 
                logger.info(f"error occured error_code : {response.status_code} detail : {response.json()['detail']}")
        except Exception as e : 
            logger.error(f'unexpected error {str(e)}')
    



    

    



            


            