from requests import Session
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def set_project_year(project_year: int):
    if (len(str(project_year))) == 4:
        project_year -= 1911
        return project_year

    return project_year


def download_html(
    method: str,
    session: Session,
    project_id: str = None,
    payload: dict = None,
) -> BeautifulSoup:
    HEADERS = {"user-agent": UserAgent().google}

    if method == "post":
        html_body = session.post(
            "https://ntuacc.cc.ntu.edu.tw/acc/apply/ProjectDetail.asp",
            data=payload,
            headers=HEADERS,
        )

    else:
        html_body = session.get(
            f"https://ntuacc.cc.ntu.edu.tw/trace/trace.asp?target=self&APPCODE={project_id}&VYEAR={project_id[:3]}",
            headers=HEADERS,
        )

    html_body.encoding = "big5"
    return BeautifulSoup(html_body.text, "lxml")
