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

OWNER_ID = 8699868928

HEROKU_APP_NAME = ""
HEROKU_API_KEY = ""

# ------------------ USERS ------------------

SUDO_USERS = [6321617217 , 8499276647 , 6339597481 , 7816235846]

for x in ALTRON:
    if x not in SUDO_USERS:
        SUDO_USERS.append(x)

if OWNER_ID not in SUDO_USERS:
    SUDO_USERS.append(OWNER_ID)

# ------------------ BOT TOKENS ------------------

BOT_TOKEN = "8727891881:AAH-rWCHq5oIbCNNghJRu7fManKyFW28Tgc"
BOT_TOKEN2 = "8638885960:AAEvJj_X6KBct4hW1ju_WZ3oPt3FZ78Khw0"
BOT_TOKEN3 = "8857420192:AAEnsoOn19i4Z7NytOaSWPKcqZRv3AaCsGY"
BOT_TOKEN4 = "8786308264:AAGDboNRXcbzDhbTCxk7cc_SDy7qxWG9jSA"
BOT_TOKEN5 = "8730008848:AAFB14oTtkmJHT7rOhsEmdR1XM19kGHFXj0"
BOT_TOKEN6 = "8938699227:AAGLyXKKmBy_UjLe_uVLFTpnHOfjIylTroM"
BOT_TOKEN7 = "8745412754:AAFxAXirF67T4fA0LkP0B8UGTtlvwkv2UlY"
BOT_TOKEN8 = "8705417949:AAGvZMTAq-MR-6SkTcQXBgHIFplt6wjrXb4"
BOT_TOKEN9 = "8549184662:AAFqptT7mc1Ep7coqbHy6vph7MKy07PkE60"
BOT_TOKEN10 = "8603828305:AAHwlrycyP7-rfKlCi1zmK4_BqbCYpZQyT8"

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
