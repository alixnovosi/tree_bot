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

    LOG = botskeleton.set_up_logging()

    while True:
        IMAGE_PATH = path.join(HERE, f"test-{datetime.now()}.png")

        # Pick what we're tweeting.
        PRESETS = {
            "White and black": treegen.TreeInfo(colors=False, inverted=True, extra_branching=False,
                                                image_path=IMAGE_PATH),

            "Black and white": treegen.TreeInfo(colors=False, extra_branching=False,
                                                image_path=IMAGE_PATH),

            "Summer": treegen.TreeInfo(season=treegen.Seasons.SUMMER, image_path=IMAGE_PATH),

            "Winter": treegen.TreeInfo(season=treegen.Seasons.WINTER, image_path=IMAGE_PATH),

            "Fall (one-color)": treegen.TreeInfo(season=treegen.Seasons.FALL,
                                                 image_path=IMAGE_PATH),

            "Fall (multi-color)": treegen.TreeInfo(season=treegen.Seasons.FALL, mixed_fall=True,
                                                  image_path=IMAGE_PATH),
        }



        # Black and white/color switch.
        LOG.info("Picking tree type.")
        tree_desc = random.choice(list(PRESETS.keys()))
        tree_info = PRESETS[tree_desc]

        LOG.info(f"Picked {tree_desc}. Drawing.")
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
        ])

        status = BOT_SKELETON.send_with_one_media(TEXT, IMAGE_PATH)

        BOT_SKELETON.nap()
