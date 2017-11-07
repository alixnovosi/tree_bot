"""Main class for bot."""

import random
import sys
import time
from datetime import datetime
from os import path

import botskeleton
import treegen


# Delay between tweets in seconds.
DELAY = 600

if __name__ == "__main__":
    HERE = path.abspath(path.dirname(__file__))
    SECRETS_DIR = path.join(HERE, "SECRETS")
    BOT_SKELETON = botskeleton.BotSkeleton(SECRETS_DIR, bot_name="treegen_bot", delay=DELAY)

    LOG = botskeleton.set_up_logging()

    while True:
        IMAGE_PATH = path.join(HERE, f"test-{datetime.now()}.png")

        # Pick what we're tweeting.

        # Black and white/color switch.
        LOG.info("Picking tree type.")
        if random.choice(range(3)) < 1:

            # Invert sometimes.
            if random.choice(range(4)) < 1:
                LOG.info("White and black tree.")
                tree_info = treegen.TreeInfo(colors=False, inverted=True, extra_branching=False,
                                              image_path=IMAGE_PATH)

            else:
                LOG.info("Black and white tree.")
                tree_info = treegen.TreeInfo(colors=False, extra_branching=False,
                                              image_path=IMAGE_PATH)

        else:
            LOG.info("Colorful tree.")
            tree_info = treegen.TreeInfo(image_path=IMAGE_PATH)

            LOG.info(f"Season of tree is {tree_info.season}")

        treegen.draw(tree_info)

        LOG.info("Sending out the tree.")
        status = BOT_SKELETON.send_with_one_media(f"Here's a tree!", IMAGE_PATH)

        BOT_SKELETON.nap()
