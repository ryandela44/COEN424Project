import requests


def get_prediction_from_custom_vision(image_url=None, image_file=None):
    headers = {
        "Prediction-Key": "0a7a65ff01ff413a9c440f07ba7e09cd",
        "Content-Type": "application/octet-stream" if image_file else "application/json"
    }

    if image_url:
        # If an image URL is provided
        data = {"Url": image_url}
        response = requests.post(
            "https://groceryitemsmodel-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/bc706eab-8a93-4c23-bd2b-6a8a088eb287/detect/iterations/GroceriesObjectDetection/url",
            headers=headers, json=data)
    elif image_file:
        # If an image file is provided
        response = requests.post(
            "https://groceryitemsmodel-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/bc706eab-8a93-4c23-bd2b-6a8a088eb287/detect/iterations/GroceriesObjectDetection/image",
            headers=headers, data=image_file)

    return response.json() if response.status_code == 200 else None
