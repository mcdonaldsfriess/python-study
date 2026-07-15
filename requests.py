import requests

resp = requests.get("https://api.github.com/users/mcdonaldsfriess")


print(resp.status_code) # 200 = ok, 404 = not found, 500 = server error
data = resp.json() # convert the response to a Python dictionary
print(data["public_repos"]) # mcdonaldsfriess



#a complete example

import requests

def get_bitcoin_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()          # turns 404/500 into an exception
        data = resp.json()
        return data["bpi"]["USD"]["rate"]
    except requests.exceptions.RequestException as e:
        print("Network/API error:", e)
        return None
    except KeyError:
        print("Response shape wasn't what I expected")
        return None

print(get_bitcoin_price())


#instead of gluing ?key=value onto the url by hand, pass a dict:

resp = requests.get("https://api.github.com/search/repositories", params={"q": "requests+language:python"})
print(resp.url) # https://api.github.com/search/repositories?q=requests+language%

#404 is still a successful request. requests.get only throws on network failure, not on a bad http status. check resp.status_code or call resp.raise_for_status() otherwise resp.json()may explode on an error page.

