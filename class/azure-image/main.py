import os
import time
from dotenv import load_dotenv
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import ComputerVisionOcrErrorException
# from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
# from azure.cognitiveservices.vision.computervision.models import ComputervisionOcrErrorException
from msrest.authentication import CognitiveServicesCredentials

# read_file is read image file and return binary data
# def read_file(path: str) -> list[bytes]:
#     return open(path, "rb")

# read_env is read environment variable

def read_env() -> [str, str]:
    key = os.environ["COMPUTER_VISION_SUBSCRIPTION_KEY"]
    endpoint = os.environ["COMPUTER_VISION_ENDPOINT"]
    if key == "": #or region == "":
        raise Exception("Environment variable is not set")
    
    # endpoint = "https://" + region + ".api.cognitive.microsoft.com/"

    return endpoint, key

def main():
    load_dotenv()
    # read environment variable
    try:
        endpoint , key = read_env()
    except Exception as err:
        print("Environment variable is not set",err)
        exit(1)
    location = "japanwest"
    
    # set cognitive creadential
    credentials = CognitiveServicesCredentials(key)

    # set client
    cv_client = ComputerVisionClient(endpoint=endpoint, credentials=credentials)
    
    # read image file
    try:
        path = "img/sample.png"
        # if os.environ["IMAGE_PATH"] != "":
            # path = os.environ["IMAGE_PATH"]

        image_data = open(path,"rb")#read_file(path=path)
    except Exception as err:
        print("Image file is not found :",err)
        exit(1)

    # call API        
    try:
        results  = cv_client.read_in_stream(image_data, language="en", raw=True)
    except Exception as err:
        print("Azure Cognitive Service Error :", err)
        exit(1)
    
    # get operation location
    operation_location = results.headers["Operation-Location"]
    # get operation id
    operation_id = operation_location.split("/")[-1]
    # get result
    result = cv_client.get_read_result(operation_id)
    
    # wait for status
    while result.status == "notStarted" or result.status == "running":
        time.sleep(1)
        result = cv_client.get_read_result(operation_id)

    # get result
    result = result.analyze_result.read_results[0].lines
    # print result
    for line in result:
        print(line.text)

# main function
if __name__ == "__main__":
    main()