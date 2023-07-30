from typing import Optional, Dict, Any, List

TRENDS_SITEKEY = '6LfnfJYaAAAAAGZJh3AZH1Xmkg7dIj3IP5-xz19W'

class CaptchaTokenProvider:

    def obtain_token(self, url: str, action: str, cookies: Optional[List[Dict[str, Any]]]) -> Optional[str]:
        raise NotImplementedError()

    def report_success(self) -> None:
        pass

    def report_access_denied(self) -> None:
        pass


class NoopCaptchaTokenProvider(CaptchaTokenProvider):

    def obtain_token(self, url: str, action: str, cookies: Optional[List[Dict[str, Any]]]) -> Optional[str]:
        return None
