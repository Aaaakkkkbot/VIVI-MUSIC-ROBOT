from VelionaMusicBot.core.bot import VIVIBot
from VelionaMusicBot.core.dir import dirr
from VelionaMusicBot.core.git import git
from VelionaMusicBot.core.userbot import Userbot
from VelionaMusicBot.misc import dbb, heroku, sudo
from aiohttp import ClientSession

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = VIVIBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

aiohttpsession = ClientSession()
