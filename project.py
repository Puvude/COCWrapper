from members import Members


class Project(Members):
    def __init__(self, url, headers):
        super().__init__(url, headers)

    def get_players(self):
        from main import Next

        list_of_players: list = []
        while Next.COUNTRY_ID != 32000260:
            Next.COUNTRY_ID += 1

            self.url = f"https://api.clashofclans.com/v1/locations/{Next.COUNTRY_ID}/rankings/players"

            new_players = self.get_json_response()
            list_of_players.append(new_players)

        return list_of_players
