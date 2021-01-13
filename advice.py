##Simple API call to get advice for the day...
import requests

def advice_for_the_day(text):
    print("************** Advice for the day! **************")
    print(text)
    
request = requests.get("https://api.adviceslip.com/advice")

if request.status_code == 200:
    dict = request.json()
    advice = dict['slip']['advice']
    advice_for_the_day(advice)