# import requests

# url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"

# payload = "q=English%20is%20hard%2C%20but%20detectably%20so"
# headers = {
# 	"content-type": "application/x-www-form-urlencoded",
# 	"Accept-Encoding": "application/gzip",
# 	"X-RapidAPI-Key": "75106fd62bmsh49d3626bea21183p1ad209jsn92329c88a3f6",
# 	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
# }

# response = requests.request("POST", url, data=payload, headers=headers)

# print(response.text)


def func(*z, x):
    print(x)	
    
func(1,x="4+1")