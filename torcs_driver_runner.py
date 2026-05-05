## ----------------- Input argsparse -----------------

# --driver_paths : list[]
# --params : json

# get num drivers from len(driver_paths)
# if --params exists, we are in simple driver mode - len(driver_paths) should be 1

import argparse
import json

parser = argparse.ArgumentParser(
    prog='TORCS Driver Runner',
    description='Handles running of drivers, their lifespan and heartbeat.',)
parser.add_argument('--driver_paths', type=list, help='The index of the car (0-9)')
parser.add_argument('--params', type=json, help='The name of the team.')



## ----------------- Running drivers, heartbeat, stdout -----------------



## ----------------- Ui and appearance -----------------