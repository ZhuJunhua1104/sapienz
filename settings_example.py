import os

DEBUG = True
# if False, "0" will be used
ENABLE_STRING_SEEDING = True
# use headless evaluator
HEADLESS = False


# === Emulator ===
DEVICE_NUM = 1
# seconds
AVD_BOOT_DELAY = 500
# Default value will be setted at the end of this file or the template
AVD_SERIES = "api19_"
EVAL_TIMEOUT = 120
TIMEOUT_CMD = "timeout"
# "gtimeout" for MacOS


# === Env. Paths ===
#     path should end with a '/'
ANDROID_HOME = os.getenv("ANDROID_HOME",
                         "/home/sapienz/Library/android-sdk-linux/")
# the path of sapienz folder
WORKING_DIR = os.getenv("SAPIENZ_TOOLFOLDER",
                        "/home/sapienz/Desktop/sapienz_open_release/")


# === GA parameters ===
SEQUENCE_LENGTH_MIN = 20
SEQUENCE_LENGTH_MAX = 500
# SEQUENCE_LENGTH_MAX = 1000
SUITE_SIZE = 5
# MU
POPULATION_SIZE = 50
# LAMBDA
OFFSPRING_SIZE = 50
GENERATION = 100
# Crossover probability
CXPB = 0.7
# Mutation probability
MUTPB = 0.3

# === Only for main_multi ===
# start from the ith apk
APK_OFFSET = 0
APK_DIR = ""
REPEATED_RESULTS_DIR = ""
REPEATED_RUNS = 20


# === MOTIFCORE script ===
# for initial population
MOTIFCORE_SCRIPT_PATH = '/mnt/sdcard/motifcore.script'
# header for evolved scripts
MOTIFCORE_SCRIPT_HEADER = 'type= raw events\ncount= -1\nspeed= 1.0\nstart data >>\n'
