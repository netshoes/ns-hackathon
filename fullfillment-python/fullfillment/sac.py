import requests

_SAC_ENDPOINT = "https://faq.directtalk.com.br/1.0/api/Search"

headers = """Host: faq.directtalk.com.br
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0
Accept: application/json
Accept-Language: pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Content-Type: application/json
Connection: keep-alive
Referer: https://faq.directtalk.com.br/1.0/static/dist/index.html
TE: Trailers"""

headers = dict((kv.split(": ")[0], kv.split(": ")[1]) for kv in headers.split("\n"))

def perguntar_sac(pesquisa):
    params = {
        "uuidDepartment": "c5e13fc1-279a-46f6-9e55-dd0561a7e2ce",
        "text": pesquisa
    }

    resp = requests.post(_SAC_ENDPOINT, headers=headers, json=params).json()
    print(resp)
    return resp["articles"]
