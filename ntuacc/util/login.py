import requests
from ..store import HEADERS, session_store


def login(payload: dict) -> bool:
    """The login function makes sure the user is logged in.

    Args:
        payload (dict): a dictionary object to send in the body of the request

    Returns:
        a boolean
    """
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

        session_store["session"] = session

        if not session_store["session"]:
            return False

        return True

    except requests.ConnectionError:
        print("Connection error. Make sure you are connected to Internet.")
        return False

    except requests.HTTPError:
        print("Cannot request!")
        return False
