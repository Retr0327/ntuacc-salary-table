import requests
from fake_useragent import UserAgent

HEADERS = {"user-agent": UserAgent().google}


def login(payload: dict) -> requests.Session:
    try:
        session = requests.session()
        response = session.post(
            "https://ntuacc.cc.ntu.edu.tw/acc/secure.asp",
            data=payload,
            headers=HEADERS,
        )

        status = response.status_code

        if status != requests.codes.ok:
            raise requests.HTTPError

        return session
    except requests.ConnectionError:
        return "Connection error. Make sure you are connected to Internet."
    except requests.HTTPError:
        return "Cannot request!"
