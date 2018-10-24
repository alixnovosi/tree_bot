"""Main class for bot."""

import random
import sys
import time
from datetime import datetime
from os import path

import botskeleton
import treegen


# Delay between tweets in seconds.
DELAY = 3600

if __name__ == "__main__":
    HERE = path.abspath(path.dirname(__file__))
    SECRETS_DIR = path.join(HERE, "SECRETS")
    BOT_SKELETON = botskeleton.BotSkeleton(SECRETS_DIR, bot_name="treegen_bot", delay=DELAY)

    LOG = BOT_SKELETON.log

    while True:
        IMAGE_PATH = path.join(HERE, f"test-{datetime.now()}.png")

        # Pick what we're tweeting.
        COMMON_CAPTION = "A pixelated tree, drawn by a computer."
        PRESETS = [
            {
                "description": "White and black",
                "obj": treegen.TreeInfo(colors=False, inverted=True, extra_branching=False,
                                                image_path=IMAGE_PATH),
                "caption": (f"{COMMON_CAPTION} It is white, on a black"
                            " background."
                            ),
            },
            {
                "description": "Black and white",
                "obj": treegen.TreeInfo(colors=False, extra_branching=False,
                                                image_path=IMAGE_PATH),
                "caption": (f"{COMMON_CAPTION} It is black, on a white"
                            " background."
                            ),
            },
            {
                "description": "Summer",
                "obj": treegen.TreeInfo(season=treegen.Seasons.SUMMER, image_path=IMAGE_PATH),
                "caption": (f"{COMMON_CAPTION} It is meant to be a deciduous"
                            " tree in summer, when it hasn't lost its leaves. Its trunk is brown,"
                            " and its leaves are green. The background is a light blue,"
                            " representing the sky"
                            ),
            },
            {
                "description": "Winter",
                "obj": treegen.TreeInfo(season=treegen.Seasons.WINTER, image_path=IMAGE_PATH),
                "caption": (f"{COMMON_CAPTION} It is meant to be a deciduous tree in winter,"
                            " when it's lost its leaves. It is brown, trunk and branches. The"
                            " background is a light blue."
                            ),
            },
            {
                "description": "Fall (one-color)",
                "obj": treegen.TreeInfo(season=treegen.Seasons.FALL,
                                                 image_path=IMAGE_PATH),
                "caption": (f"{COMMON_CAPTION} It is meant to be a deciduous tree in fall, when"
                            " the leaves are starting to turn. This caption came before it was"
                            " drawn, so I can't say what color the leaves are, but they're either"
                            " red, orange, or yellow. The background is a light blue."
                            ),
            },
            {
                "description": "Fall (multi-color)",
                "obj": treegen.TreeInfo(season=treegen.Seasons.FALL, mixed_fall=True,
                                                  image_path=IMAGE_PATH),
                "caption": (f"{COMMON_CAPTION} It is meant to be a deciduous tree in fall, when"
                            " the leaves are starting to turn. The leaves are red, yellow, and"
                            " orange. The trunk is brown, and the background is a light blue."
                            ),
            },
            {
                "description": "Spring",
                "obj": treegen.TreeInfo(season=treegen.Seasons.SPRING, image_path=IMAGE_PATH),
                "caption": (f"{COMMON_CAPTION} It is meant to be a tree blossoming in spring."
                            " The leaves are pink, representing blossoms. The trunk is brown, and"
                            " the background is a light blue."
                            ),
            },
        ]

        # Black and white/color switch.
        LOG.info("Picking tree type.")
        TREE_TYPE = random.choice(PRESETS)
        tree_info = TREE_TYPE["obj"]

        LOG.info(f"Picked {TREE_TYPE['description']}. Drawing.")
        tree_info.draw()

        LOG.info("Sending out the tree.")

        TEXT = random.choice([
            "Here's a tree!",
            "Here's a tree.",
            "TREE",
            "tree",
            "this is a tree",
            "I've drawn a tree for you.",
            "I've drawn a tree for you!",
            "🌳",
            "Please, have a tree picture.",
            "I (a computer) drew a pixelly tree for you.",
            "do you like this tree",
            "T R E E",
            "🌳" * 140,
            "T   R\n  E\n  E",
            "🌳tree🌳",
        ])

        status = BOT_SKELETON.send_with_one_media(TEXT, IMAGE_PATH, TREE_TYPE["caption"])

        BOT_SKELETON.nap()
