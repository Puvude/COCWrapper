import re
from typing import List

from members import Members


class Clan(Members):
    def __init__(self, url: str, headers: str):
        super().__init__(url, headers)
        self.keys_to_remove: List[str, ...] = ['league.id', 'league.iconUrls', 'playerHouse']
        self.clan_info: List[dict] = self.get_clan_info()

    def get_total_donations(self) -> int:
        return sum([d['donations'] for d in self.get_clan_info()])

    def get_average_donations(self) -> int:
        total_donation = sum([value["donations"] for value in self.get_clan_info()])
        return round(total_donation / self.get_number_of_members())

    def filer_clan_info(self) -> None:
        for item in self.clan_info:
            for tag in self.keys_to_remove:
                keys = tag.split('.')
                if len(keys) == 1:
                    item.pop(tag, None)
                    for key, value in item.items():
                        if isinstance(value, dict):
                            league = list(value.values())[0]
                            item[key] = league
                elif len(keys) == 2:
                    item[keys[0]].pop(keys[1], None)

    def format_role_name(self) -> List[dict]:
        self.filer_clan_info()

        new_data = []
        for column in self.clan_info:
            new_dict = {re.sub(r'(?<!^)(?=[A-Z])', ' ', key).title(): value for key, value in column.items()}
            new_dict["Role"] = re.sub(r'(?<!^)(?=[A-Z])', '-', column["role"]).title()
            new_data.append(new_dict)

        return new_data
