from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("24658337")
API_HASH = getenv("bf99242dbb7f3501f28d39f0a0383cbf")

BOT_TOKEN = getenv("6444935129:AAGmLtUrxj03_xbijnVBE_Ef-f9JjrG1-kQ", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("5490773419"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/cfc2971662ab9f0e6854d.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/f8abaa00e1a953eb0e036.jpg")

SESSION = getenv("BQGeZ2wAIrF_gCqrpCceVpz8lQ9kCtgci_CPpbV9cvMc0ovJSFKndf1goniy_G6NF3hoj3TX97rO0SItx24JhorX8BaB2z0n5-jLe3fq5suk2wSuKKPrp6xhEKu1RKZdDsLexCuAzvSiS_waviER98LKTOWzc7eHyrgmXsRBbn0trHmLVpgNAcJm3uXNwbOAKYENbxZZ-TUooMA0YbthiiTtkHgBpg_tJCfb9WFC_xzdiXcBQSSVXf8VBbpduwQzcIiMkupXseB5MSPmECUhDyh5yWOdFu5ABWhNHdHzg5BEfkLxECpacar1SRdPr42FyqOncoJkX9JlhNY-YP0eSHsJ5_8DpAAAAAFmgxz5AA", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/yae_support")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/yaemikologs")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6590287973").split()))


FAILED = "https://telegra.ph/file/6248889bdd92ff9a1d04b.jpg"
