import pydirectinput
from time import sleep
from macro import BaseMenuMacro

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sleep(3)

    # print("asd")

    base_menu_macro = BaseMenuMacro()

    base_menu_macro.reborn_all()

    base_menu_macro.setup_skill_all()

    #
    # def next_skill_char(to_select):
    #     return "|3_s|2_s|1_s" + to_select
    #
    # def select_all_skills(positions):
    #     char_command = ""
    #     for position in positions:
    #         for _ in range(position):
    #             char_command += "|right_vs"
    #         char_command += "|q_vs"
    #     return char_command
    #
    # time.sleep(3)
    #
    # delay = {
    #     "vs": 0,
    #     "s": 0.1,
    #     "m": 0.5,
    #     "l": 1,
    #     "xl": 1.5,
    #     "xxl": 2,
    # }
    #
    # full_input = ""
    # create_aester_f = select_char(0, True, True, 12, 0, 2, 2)
    # create_aester_m = select_char(0, False, True, 12, 0, 2, 3)
    #
    # create_tank_f = select_char(1, True, False, 4, 1, 2, 0)
    # create_tank_m = select_char(1, False, False, 4, 1, 1, 3)
    #
    # create_dancer = select_char(2, True, False, 14, 2, 0, 2)
    # create_gothic_cannon = select_char(3, False, False, 5, 1, 3, 3)
    #
    # create_swords = select_char(4, True, False, 14, 0, 1, 3)
    # create_gothic = select_char(3, False, False, 5, 2, 3, 1)
    # create_scrolls = select_char(4, True, True, 6, 0, 3, 2)
    #
    # create_crossbow = select_char(7, True, True, 11, 2, 2, 2)
    # create_spears = select_char(1, False, False, 12, 0, 1, 2)
    #
    # create_cat_mage = select_char(8, True, True, 6, 2, 0, 1)
    # create_cat = select_char(8, True, True, 6, 0, 3, 0)
    #
    # index = {
    #     "index": 1
    # }
    #
    # if None is None:
    #     full_input += create_aester_f
    #     full_input += append_next_create(create_aester_m, index)
    #     full_input += append_next_create(create_aester_f, index)
    #
    #     full_input += append_next_create(create_tank_f, index)
    #     full_input += append_next_create(create_tank_m, index)
    #     full_input += append_next_create(create_tank_f, index)
    #
    #     full_input += append_next_create(create_dancer, index)
    #     full_input += append_next_create(create_gothic_cannon, index)
    #     full_input += append_next_create(create_dancer, index)
    #
    #     time.sleep(0.1)
    #     full_input += append_next_create(create_swords, index)
    #     full_input += append_next_create(create_gothic, index)
    #     full_input += append_next_create(create_scrolls, index)
    #
    #     time.sleep(0.1)
    #     full_input += append_next_create(create_crossbow, index)
    #     full_input += append_next_create(create_spears, index)
    #     full_input += append_next_create(create_crossbow, index)
    #
    #     for _ in range(5):
    #         full_input += append_next_create(create_cat_mage, index)
    #
    #     for _ in range(20):
    #         full_input += append_next_create(create_cat, index)
    #
    #     full_input += "|w_xl|r_l|down_vs|q_m|q_vs|down_vs|q_m"
    #
    # create_skill_mage_1 = select_all_skills([0,1,1,1,1,1,1,1,1,1,1,4,1,1,1,1,4,1,19,4,1,4])
    # create_skill_mage_2 = select_all_skills([0,1,1,2,1,1,1,1,1,1,2,2,1,1,1,1,4,1,23,1,2,2])
    #
    # create_skill_tank = select_all_skills([0,8,1,1,1,5,2,1,1,3,2,3,3,3,25,34,2,15,1,1,1,10])
    #
    # create_skill_dancer = select_all_skills([0,1,1,1,5,2,14,3,4,4,2,9,4,3,30,5,2,1,1])
    # create_skill_cannon = select_all_skills([0,1,1,1,1,3,2,3,1,3,1,1,4,3,1,1,1,1,1,3,1,2,16,5,8])
    #
    # create_skill_swords = select_all_skills([0,1,1,1,7,2,2,3,1,8,5,5,4,11,29,1,1,2,6])
    # create_skill_hammer = select_all_skills([0,1,1,1,1,9,2,1,1,5,1,2,1,7,4,4,2,1,2,4,2,2,4,2,3,20,3,9])
    # create_skill_scroll = select_all_skills([0,1,1,1,2,6,1,1,2,8,9,20,29,2,3])
    #
    # create_skill_crossbow = select_all_skills([0,1,1,1,2,3,5,1,1,8,2,2,12,5,2,25,1,6])
    # create_skill_spear = select_all_skills([0,1,1,1,7,2,1,3,6,9,1,4,1,7,13,2,1,5,1,18,13,1,1,1,3])
    #
    # create_skill_cat_mage = select_all_skills([11,2,12,53,2,1,1,1,1,1,24,2])
    # create_skill_cat = select_all_skills([9,14,35,1,5,2,1,1,1,1,1,19,2])
    #
    # full_input += create_skill_mage_1
    # full_input += next_skill_char(create_skill_mage_1)
    # full_input += next_skill_char(create_skill_mage_2)
    #
    # full_input += next_skill_char(create_skill_tank)
    # full_input += next_skill_char(create_skill_tank)
    # full_input += next_skill_char(create_skill_tank)
    #
    # full_input += next_skill_char(create_skill_dancer)
    # full_input += next_skill_char(create_skill_cannon)
    # full_input += next_skill_char(create_skill_dancer)
    #
    # full_input += next_skill_char(create_skill_swords)
    # full_input += next_skill_char(create_skill_hammer)
    # full_input += next_skill_char(create_skill_scroll)
    #
    # full_input += next_skill_char(create_skill_crossbow)
    # full_input += next_skill_char(create_skill_spear)
    # full_input += next_skill_char(create_skill_crossbow)
    #
    # for _ in range(5):
    #     full_input += next_skill_char(create_skill_cat_mage)
    #
    # for _ in range(20):
    #     full_input += next_skill_char(create_skill_cat)
    #
    # command_list = full_input.split("|")
    #
    # for command in command_list:
    #
    #     if not command: continue
    #
    #     key = command.split("_")[0]
    #     duration = command.split("_")[1]
    #
    #     pydirectinput.keyDown(key)
    #     pydirectinput.keyUp(key)
    #
    #     time.sleep(delay[duration])
