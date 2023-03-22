from typing import List

import webcolors

from excel import Excel


class Color(Excel):
    def determine_color_donation(self) -> List[str]:
        list_of_member_donation: List[int, ...] = [d['donations'] for d in self.get_clan_info()]
        color_codes: List[str] = []

        for donation in list_of_member_donation:
            if donation >= self.average_donation * 1.9:
                color_code = "darkgreen"
                color_codes.append(color_code)
            elif donation >= self.average_donation * 1.6:
                color_code = "green"
                color_codes.append(color_code)
            elif donation >= self.average_donation * 1.3:
                color_code = "yellow"
                color_codes.append(color_code)
            elif donation >= self.average_donation:
                color_code = "lightgrey"
                color_codes.append(color_code)
            elif donation <= self.average_donation * 0.3:
                color_code = "orange"
                color_codes.append(color_code)
            elif donation <= self.average_donation * 0.6:
                color_code = "red"
                color_codes.append(color_code)
            elif donation <= self.average_donation * 0.9:
                color_code = "darkred"
                color_codes.append(color_code)

        return color_codes

    def convert_color_to_hex(self) -> List[str]:
        return [webcolors.rgb_to_hex(webcolors.name_to_rgb(color)) for color in self.determine_color_donation()]

    def apply_color_formatting(self):
        return {"background-color: " + color for color in self.convert_color_to_hex()}
