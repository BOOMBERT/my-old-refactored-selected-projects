from typing import Dict, Literal


def get_initial_menu_button_schemas(window_width: str, window_height: str) -> Dict:
    DIFFICULTY_LEVEL_BUTTONS_PATCH = "assets/initial_menu/buttons/"
    return {
        "easy": {
            "horizontal_position": window_width // 5,
            "vertical_position": window_height // 2 - 100,
            "image": DIFFICULTY_LEVEL_BUTTONS_PATCH + "easy/base.png",
            "choiced_image": DIFFICULTY_LEVEL_BUTTONS_PATCH + "easy/choice.png"
        },
        "normal": {
            "horizontal_position": window_width // 5,
            "vertical_position": window_height // 2,
            "image": DIFFICULTY_LEVEL_BUTTONS_PATCH + "normal/base.png",
            "choiced_image": DIFFICULTY_LEVEL_BUTTONS_PATCH + "normal/choice.png"
        },
        "hard": {
            "horizontal_position": window_width // 5,
            "vertical_position": window_height // 2 + 100,
            "image": DIFFICULTY_LEVEL_BUTTONS_PATCH + "hard/base.png",
            "choiced_image": DIFFICULTY_LEVEL_BUTTONS_PATCH + "hard/choice.png"
        },
        "play": {
            "horizontal_position": window_width // 2,
            "vertical_position": window_height // 2,
            "image": DIFFICULTY_LEVEL_BUTTONS_PATCH + "play.png"
        }
    }

def get_target_image_by_difficulty_level(difficulty_level: Literal["easy", "normal", "hard"]) -> str:
    TARGET_IMAGES_PATH = "assets/game/target/?_level.png"
    return TARGET_IMAGES_PATH.replace("?", difficulty_level)
