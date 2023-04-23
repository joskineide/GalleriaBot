from utils import Runner


class BaseMenuCommand:

    def __init__(self):
        self.runner = Runner()

    def confirm(self):
        self.runner.run_command("q")

    def back(self):
        self.runner.run_command("w")

    def move_menu_button_x(self, pos):
        if pos < 0:
            for _ in range(-pos):
                self.runner.run_command("left")
        else:
            for _ in range(pos):
                self.runner.run_command("right")

    def select_menu_button_x(self, pos):
        self.move_menu_button_x(pos)
        self.confirm()

    def move_menu_button_y(self, pos):
        if pos < 0:
            for _ in range(-pos):
                self.runner.run_command("up")
        for _ in range(pos):
            self.runner.run_command("down")

    def select_menu_button_y(self, pos):
        self.move_menu_button_y(pos)
        self.confirm()

    def char_create_change_alt(self):
        self.runner.run_command("r")

    def char_create_change_skin(self, pos):
        for _ in range(pos):
            self.runner.run_command("3")

    def char_create_change_color(self, pos):
        for _ in range(pos):
            self.runner.run_command("e")

    def char_create_confirm(self):
        self.runner.run_command("space")

    def change_menu_type(self):
        self.runner.run_command("r")

    def prepare_next_char_skill(self):
        self.runner.run_command_list(["3_0", "1_0","2_0"])




