import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "26119931"))
    API_HASH = os.environ.get("API_HASH", "79e5b0d03df604b1bd1ee8b2f753372e")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5782334409:AAF9H9NZ-VY_vVZmIt2rn8JD_MYlAlHOfgI")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQBBjW4UT2GqDGJJn5QvYb-lNTWPUsjo3fnL7uHN0njweYkCmLZyU0o5yWEqUZijsu82qh3vVbg-3zx5QveYPQahcfgrJtWQasGwDMT1_6KQh2yq0PHRBEyRACU2GFNOboetls9R4MJ_lko2yrMeRBqjyO_DSig1Llm4tQrdCz_iSEdEAtrq3MhyUPAmZWrkKceOjwD0xZo8amxsIH4QcZgoBqTro6EQinpeuA-3dK0BSpY1MnAuycNF0TiVIaLLwdhljOqV9CGeVd6CJN_3Ksn-QbpPZDlVzTrucOqPnEcMn7JWLXekF-W1dLSjEK078oH0jCikE_N15WhjvGlJ4k9MAAAAAV-9kLgA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@Ramndi_musicbot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat"https://t.me/alone_support) # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel"https://t.me/alone_support) # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5901226168")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
