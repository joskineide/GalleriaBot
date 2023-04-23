import pydirectinput
import time


class Runner:

    def __init__(self):
        pydirectinput.PAUSE = 0.06

    # this receives in a particular string format: |q_1|,
    # with the first part being the key pressed and the second being the duration

    def run_command_list(self, command_list):
        for command in command_list:
            if not command:
                continue
            key = command.split("_")[0]
            duration = command.split("_")[1]
            self.run_command(key)
            time.sleep(float(duration))

    def run_command(self, key: str):
        pydirectinput.keyDown(key)
        pydirectinput.keyUp(key)
