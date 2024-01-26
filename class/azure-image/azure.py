import os,time
from dotenv import load_dotenv

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import ComputerVisionOcrErrorException
from azure.cognitiveservices.vision.computervision.models import TextOperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials

load_dotenv()
key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
endpoint = os.environ['COMPUTER_VISION_ENDPOINT']
location = "japanwest"

image_path = "img.test.jpg"

def main(image_path):
  computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(key))
  
  local_image = open(image_path, "rb")
  try:
    result = computervision_client.read_in_stream(local_image, raw=True)
  except ComputerVisionOcrErrorException as e:
    print("error: ",e.response)
    raise e
  
  # local_image.close()
  
