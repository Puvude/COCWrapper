import requests
from typing import List


class Members:
    def __init__(self, url: str, headers: str):
        self.url: str = url
        self.headers: str = headers

    def get_json_response(self) -> requests.get:
        return requests.get(self.url, headers=self.headers).json()

    def get_clan_info(self) -> List[dict]:
        return self.get_json_response()["items"]

    def get_test(self):
        return [item['league']['name'] for item in self.get_json_response()["items"]]

    def get_clan_members(self) -> List[str]:
        clan_data: dict = self.get_json_response()
        number_of_members: int = len(clan_data["items"])

        return [clan_data["items"][member]["name"] for member in range(number_of_members)]

    def get_number_of_members(self) -> int:
        return len(self.get_clan_info())

    def get_donations_of_member(self) -> List[int]:
        clan_data: list = self.get_json_response()["items"]
        return [value["donations"] for value in clan_data]
