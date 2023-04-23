from typing import List

from command import BaseMenuCommand
from time import sleep


class BaseMenuMacro:

    def __init__(self):
        self.base_menu_command = BaseMenuCommand()
        self.char_presets = {
            "aester_f": {"class_pos": 0, "is_f": True, "is_alt": True, "skill_pos": 12,
                         "skin_id": 0, "color_id": 2, "voice_id": 2},
            "aester_m": {"class_pos": 0, "is_f": False, "is_alt": True, "skill_pos": 12,
                         "skin_id": 0, "color_id": 2, "voice_id": 3},
            "tank_f": {"class_pos": 1, "is_f": True, "is_alt": False, "skill_pos": 4,
                       "skin_id": 1, "color_id": 2, "voice_id": 0},
            "tank_m": {"class_pos": 1, "is_f": False, "is_alt": False, "skill_pos": 4,
                       "skin_id": 1, "color_id": 1, "voice_id": 3},
            "dancer": {"class_pos": 2, "is_f": True, "is_alt": False, "skill_pos": 14,
                       "skin_id": 2, "color_id": 0, "voice_id": 2},
            "gothic_cannon": {"class_pos": 3, "is_f": False, "is_alt": False, "skill_pos": 5,
                              "skin_id": 1, "color_id": 3, "voice_id": 3},
            "swords": {"class_pos": 4, "is_f": True, "is_alt": False, "skill_pos": 14,
                       "skin_id": 0, "color_id": 1, "voice_id": 3},
            "gothic": {"class_pos": 3, "is_f": False, "is_alt": False, "skill_pos": 5,
                       "skin_id": 2, "color_id": 3, "voice_id": 1},
            "scrolls": {"class_pos": 4, "is_f": True, "is_alt": True, "skill_pos": 6,
                        "skin_id": 0, "color_id": 3, "voice_id": 2},
            "crossbow": {"class_pos": 7, "is_f": True, "is_alt": True, "skill_pos": 11,
                         "skin_id": 2, "color_id": 2, "voice_id": 2},
            "spears": {"class_pos": 1, "is_f": False, "is_alt": False, "skill_pos": 12,
                       "skin_id": 0, "color_id": 1, "voice_id": 2},
            "cat_mage": {"class_pos": 8, "is_f": True, "is_alt": True, "skill_pos": 6,
                         "skin_id": 2, "color_id": 0, "voice_id": 1},
            "cat": {"class_pos": 8, "is_f": True, "is_alt": True, "skill_pos": 6,
                    "skin_id": 0, "color_id": 3, "voice_id": 0},
        }
        self.skill_preset = {
            "mage_1": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 15, 16, 17, 18, 22, 23, 42, 46, 47, 51],
            "mage_2": [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 17, 18, 22, 23, 46, 47, 49, 51],
            "tank": [0, 8, 9, 10, 11, 16, 18, 19, 20, 23, 25, 28, 31, 34, 59, 93, 95, 110, 111, 112, 113, 123],
            "dancer": [0, 1, 2, 3, 8, 10, 24, 27, 31, 35, 37, 46, 50, 53, 83, 88, 90, 91, 92],
            "gothic_cannon": [0, 1, 2, 3, 4, 7, 9, 12, 13, 16, 17, 18, 22, 25, 26, 27, 28, 29, 30, 33, 34, 36, 52, 57, 65],
            "swords": [0, 1, 2, 3, 10, 12, 14, 17, 18, 26, 31, 36, 40, 51, 80, 81, 82, 84, 90],
            "gothic": [0, 1, 2, 3, 4, 13, 15, 16, 17, 22, 23, 25, 26, 33, 37, 41, 43, 44, 46, 50, 52, 54, 58, 60, 63, 83, 86, 95],
            "scrolls": [0, 1, 2, 3, 5, 11, 12, 13, 15, 23, 32, 52, 81, 83, 86],
            "crossbow": [0, 1, 2, 3, 5, 8, 13, 14, 15, 23, 25, 27, 39, 44, 46, 71, 72, 78],
            "spears": [0, 1, 2, 3, 10, 12, 13, 16, 22, 31, 32, 36, 37, 44, 57, 59, 60, 65, 66, 84, 97, 98, 99, 100, 103],
            "cat_mage": [11, 13, 25, 78, 80, 81, 82, 83, 84, 85, 109, 111],
            "cat": [9, 23, 58, 59, 64, 66, 67, 68, 69, 70, 71, 90, 92]
        }

    def reborn_all(self):
        self.base_menu_command.select_menu_button_y(1)
        sleep(1.5)
        char_pos = {"pos": 0}
        self.reborn_single(char_pos=char_pos, **self.char_presets["aester_f"])
        self.reborn_single(char_pos=char_pos, **self.char_presets["aester_m"])
        self.reborn_single(char_pos=char_pos, **self.char_presets["aester_f"])

        self.reborn_single(char_pos=char_pos, **self.char_presets["tank_f"])
        self.reborn_single(char_pos=char_pos, **self.char_presets["tank_m"])
        self.reborn_single(char_pos=char_pos, **self.char_presets["tank_f"])

        self.reborn_single(char_pos=char_pos, **self.char_presets["dancer"])
        self.reborn_single(char_pos=char_pos, **self.char_presets["gothic_cannon"])
        self.reborn_single(char_pos=char_pos, **self.char_presets["dancer"])

        self.reborn_single(char_pos=char_pos, **self.char_presets["swords"])
        self.reborn_single(char_pos=char_pos, **self.char_presets["gothic"])
        self.reborn_single(char_pos=char_pos, **self.char_presets["scrolls"])

        self.reborn_single(char_pos=char_pos, **self.char_presets["crossbow"])
        self.reborn_single(char_pos=char_pos, **self.char_presets["spears"])
        self.reborn_single(char_pos=char_pos, **self.char_presets["crossbow"])

        for _ in range(5):
            self.reborn_single(char_pos=char_pos, **self.char_presets["cat_mage"])

        for _ in range(20):
            self.reborn_single(char_pos=char_pos, **self.char_presets["cat"])
        self.base_menu_command.back()
        sleep(1.5)

    def reborn_single(self, char_pos: dict, class_pos: int, is_f: bool, is_alt: bool, skill_pos: int,
                      skin_id: int, color_id: int, voice_id: int):
        self.base_menu_command.select_menu_button_y(3)
        sleep(0.75)
        self.base_menu_command.select_menu_button_y(char_pos["pos"])
        sleep(0.3)
        self.base_menu_command.move_menu_button_x(class_pos)
        if is_f:
            self.base_menu_command.move_menu_button_y(1)
        if is_alt:
            self.base_menu_command.char_create_change_alt()
        self.base_menu_command.char_create_change_color(color_id)
        self.base_menu_command.char_create_change_skin(skin_id)
        self.base_menu_command.confirm()
        sleep(1.5)
        self.base_menu_command.select_menu_button_y(7)
        self.base_menu_command.select_menu_button_x(voice_id)
        self.base_menu_command.select_menu_button_y(3)
        self.base_menu_command.select_menu_button_y(skill_pos)
        self.base_menu_command.char_create_confirm()
        sleep(0.3)
        self.base_menu_command.select_menu_button_x(-1)
        sleep(2)
        self.base_menu_command.confirm()
        sleep(0.75)
        char_pos["pos"] += 1

    def setup_skill_all(self):
        self.base_menu_command.change_menu_type()
        sleep(0.75)
        self.base_menu_command.select_menu_button_y(1)
        sleep(0.5)
        self.base_menu_command.confirm()
        self.base_menu_command.select_menu_button_y(1)
        sleep(0.5)
        self.setup_skill_single(self.skill_preset["mage_1"])
        self.setup_skill_single(self.skill_preset["mage_1"])
        self.setup_skill_single(self.skill_preset["mage_2"])

        self.setup_skill_single(self.skill_preset["tank"])
        self.setup_skill_single(self.skill_preset["tank"])
        self.setup_skill_single(self.skill_preset["tank"])

        self.setup_skill_single(self.skill_preset["dancer"])
        self.setup_skill_single(self.skill_preset["gothic_cannon"])
        self.setup_skill_single(self.skill_preset["dancer"])

        self.setup_skill_single(self.skill_preset["swords"])
        self.setup_skill_single(self.skill_preset["gothic"])
        self.setup_skill_single(self.skill_preset["scrolls"])

        self.setup_skill_single(self.skill_preset["crossbow"])
        self.setup_skill_single(self.skill_preset["spears"])
        self.setup_skill_single(self.skill_preset["crossbow"])

        for _ in range(5):
            self.setup_skill_single(self.skill_preset["cat_mage"])

        for _ in range(20):
            self.setup_skill_single(self.skill_preset["cat"])

    def setup_skill_single(self, skill_list: List[int]):
        index = 0
        skill_list.sort()
        for i in range(skill_list[-1] + 1):
            if i == skill_list[index]:
                self.base_menu_command.confirm()
                index += 1
            self.base_menu_command.move_menu_button_x(1)
        self.base_menu_command.prepare_next_char_skill()
