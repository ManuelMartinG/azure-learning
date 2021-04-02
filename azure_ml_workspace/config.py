import os
from dotenv import load_dotenv


class AzureMLConfig:

    def __init__(self):
        dotenv_path = '.env'
        load_dotenv(dotenv_path)

    @property
    def workspace(self):
        return os.environ.get("Workspace")

    @property
    def subscription_id(self):
        return os.environ.get("SubscriptionId")

    @property
    def resource_group(self):
        return os.environ.get("ResourceGroup")
