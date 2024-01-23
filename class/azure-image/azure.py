import os,time
from dotenv import load_dotenv

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import ComputerVisionOcrErrorException

load_dotenv()
key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
endpoint = os.environ['COMPUTER_VISION_ENDPOINT']
location = "japanwest"

