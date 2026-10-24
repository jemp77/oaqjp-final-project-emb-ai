import requests
import json

def emotion_detector(text_to_analyze):
    dominant_emotion = ""
    result = {}
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = obj, headers=headers)
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]["emotion"]
    
    for emotion_name, score in emotions.items():
        if dominant_emotion == "" or score > emotions[dominant_emotion]:
            dominant_emotion = emotion_name
        
        result[emotion_name] = score

    result["dominant_emotion"] = dominant_emotion
    return result