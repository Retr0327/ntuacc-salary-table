import requests
from bs4 import BeautifulSoup
from ..store import HEADERS, session_store


def get_login_content(response: requests.Response) -> BeautifulSoup:
    """The get_login_content function returns the content from the given `response`

    Returns:
        a BeautifulSoup object
    """
    response.encoding = "big5"
    return BeautifulSoup(response.text, "lxml")


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

        content = get_login_content(response).text

        if "錯誤" in content:
            raise Exception()

        session_store["session"] = session

        if not session_store["session"]:
            return False

        return True

    except requests.ConnectionError as error:
        print("Connection error. Make sure you are connected to Internet.")

    except requests.HTTPError as error:
        print("Cannot request!")

    except Exception as error:
        print("Wrong ID or password!")
