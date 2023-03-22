import requests

from clan import Clan
from excel import Excel
from members import Members
from project import Project


class Next:
    COUNTRY_ID: int = 32000020
    URL: str = f"https://api.clashofclans.com/v1/locations/{COUNTRY_ID}/rankings/players"

    with open("token.txt", "r") as f:
        HEADERS: str = {"Authorization": f.readline()}


class Main:
    CLAN_TAG: str = "2PCJRYPJQ"
    URL: str = f"https://api.clashofclans.com/v1/clans/%23{CLAN_TAG}/members"

    with open("token.txt", "r") as f:
        HEADERS: str = {"Authorization": f.readline()}


if __name__ == '__main__':
    # Execute the API request
    response: requests.Response = requests.get(Main.URL, headers=Main.HEADERS)

    # Process the API response in JSON format
    if response.status_code == 200:
        # Class: Members
        class_members = Members(Main.URL, Main.HEADERS)

        # New Project
        class_project = Project(Next.URL, Next.HEADERS)

        # Class: Clan
        class_clan = Clan(Main.URL, Main.HEADERS)

        # Class: Excel
        class_excel = Excel(Main.CLAN_TAG, Main.URL, Main.HEADERS)
    else:
        print("Error retrieving clan data.")
