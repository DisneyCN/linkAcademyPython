import requests
import json
# Enter data  
txt = list(input("Enter a message : ").split())
message = "+".join(txt)
curentLang = input('Enter curent language (example: en): ')
translateLang = input('Enter translate language : ')
# Get url
url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

payload = f"q={message}&target={translateLang}&source={curentLang}"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": "75106fd62bmsh49d3626bea21183p1ad209jsn92329c88a3f6",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}
# Get message
json_string = requests.request("POST", url, data=payload, headers=headers)
parsed_json = json.loads(json_string.text)
print('json_string.text: ', json_string.text)
print("Your answer ",parsed_json['data']['translations'][0]['translatedText'])


