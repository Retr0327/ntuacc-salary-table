from fake_useragent import FakeUserAgent

session_store = {"session": ""}

HEADERS: dict[str, FakeUserAgent] = {"user-agent": FakeUserAgent().google}
