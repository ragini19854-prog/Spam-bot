import logging
from telethon import TelegramClient
from RAUSHAN.data import ALTRON

# ------------------ LOGGING ------------------

logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.INFO
)

# ------------------ CORE CONFIG ------------------

API_ID = 35411328
API_HASH = "4c8d3c8f5d3483296f5fb530ea2cfcc6"

CMD_HNDLR = "."

OWNER_ID = 8441236350

HEROKU_APP_NAME = ""
HEROKU_API_KEY = ""

# ------------------ USERS ------------------

SUDO_USERS = [8441236350,1188604480,8225211569,8725331299,8563221554,8707693929,8471146802,1106006604,7753720995,8325253288,8323739248]

for x in ALTRON:
    if x not in SUDO_USERS:
        SUDO_USERS.append(x)

if OWNER_ID not in SUDO_USERS:
    SUDO_USERS.append(OWNER_ID)

# ------------------ BOT TOKENS ------------------

BOT_TOKEN = "8729582864:AAEsEADH7wQXOlV5hm8bT1f_LhmLoN_INB0"
BOT_TOKEN2 = "8492531985:AAFfpR_e_hVglfNNi54xgCIFkr2fO50aNlk"
BOT_TOKEN3 = "8611361143:AAEfCrWbD_JODP3DNB9yLMBVN74nR0WZfyM"
BOT_TOKEN4 = "8749385192:AAHgpwpu6Hy9mIUa6k2fX4wQ6Qr38qLqW38"
BOT_TOKEN5 = "7979190403:AAFEu10OyXfdRi4ckTWjpfnRjmpXuMKZcts"
BOT_TOKEN6 = "8637265090:AAHDkPQ81u5ZBUtD-J2HHMoMoL53I-TZ_1I"
BOT_TOKEN7 = "8740366034:AAFF7sjnHH_R7LcBWS7e42dSBG07o9PwNng"
BOT_TOKEN8 = "8721234505:AAEA_BMNvqrWq07wTKxzoQ98LgEWEizn6-I"
BOT_TOKEN9 = "8715356761:AAFZ7RYkmt0B483xp6rsYTaEnNvIKHtbRGU"
BOT_TOKEN10 = "8514898003:AAFZyxjZOoI6lxIzzuV3glpvCLat8WknfNk"

# ------------------ CLIENT HANDLER ------------------

def start_bot(session_name, bot_token):
    try:
        client = TelegramClient(session_name, API_ID, API_HASH)
        client.start(bot_token=bot_token)
        print(f"{session_name} started")
        return client
    except Exception as e:
        print(f"{session_name} failed: {e}")
        return None

# ------------------ START CLIENTS ------------------

X1 = start_bot("X1", BOT_TOKEN)
X2 = start_bot("X2", BOT_TOKEN2)
X3 = start_bot("X3", BOT_TOKEN3)
X4 = start_bot("X4", BOT_TOKEN4)
X5 = start_bot("X5", BOT_TOKEN5)
X6 = start_bot("X6", BOT_TOKEN6)
X7 = start_bot("X7", BOT_TOKEN7)
X8 = start_bot("X8", BOT_TOKEN8)
X9 = start_bot("X9", BOT_TOKEN9)
X10 = start_bot("X10", BOT_TOKEN10)

# ------------------ ACTIVE CLIENTS ------------------

CLIENTS = [x for x in [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10] if x is not None]

print(f"Total Active Bots: {len(CLIENTS)}")
