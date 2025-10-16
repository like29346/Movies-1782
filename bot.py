import os
import sys
# Pyrogram क्लाइंट को इस्तेमाल करने के लिए यह import ज़रूरी है
from pyrogram import Client 

# =============================================== 
#  Configuration Loader for Telegram Bot (Render/Server Use) 
# =============================================== 

def get_config(key, required=True):
    """
    Environment variable (कुंजी) को Fetch करता है।
    Render से Environment Variables सीधे os.getenv() से लोड होते हैं।
    """
    value = os.getenv(key)
    
    # अगर value मिलती है, तो उसे trim करके लौटाता है, वरना None
    return value.strip() if value else None


# --- Configuration Variables loaded from Render ---
# NOTE: मैं मान रहा हूँ कि आपने Render डैशबोर्ड में Key के रूप में वही Value डाली हैं 
# जो आप get_config() में पास कर रहे हैं।
# उदाहरण: Render Key = "27699873", Render Value = "27699873"

API_ID = get_config("27699873")
API_HASH = get_config("4615359950a50d32c2ab3ad80475d87e")
BOT_TOKEN = get_config("8437160489:AAEKPj7yArqb7Viv8L_yh0ogn_ouRNJFUpM")
MONGO_URI = get_config("mongodb+srv://movies123:Movies@123@cluster0.cozjses.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Other essential keys
BOT_OWNER = [int(x) for x in get_config("5311840807").split()] if get_config("5311840807") else []
LOG_CHANNEL = int(get_config("1002630246729")) if get_config("1002630246729") else None
UPDATE_CHANNEL = get_config("1003103870573")

# Optional Keys
DATABASE_URL = get_config("movies123", required=False)
USER_SESSION_STRING = get_config("1BVtsOKEBu7HCXYkQunrqrwAFCE6ivknaOrXWfguNisN_T8SGFVo26zIsfahH-1boT_a46rYpWy6-vPjRVr2mnKAXIvaZpTmgijXz8_au0GjW_M7cyCiswNOEFqRWHXiOSsgf6Ltzar7pDBr_fJDz_wSRBKCdM0GU1f6mUioRYukcvplKFYfdg8W4b_Hdw2fW_IXgl0SPC32gWOeTkRKDiAx04AFTT9Zh9DftIR7PvbsV76xa4BBi-FYuGPUQiSaqgioZ5RYWjQ-ZAJb_fhXtcwFiJDgOqnfHKvR5OP8mm4-EC3WuLWFANuicRNq2N23NS7YZtEvMqedDx9p3TlX92voRvM31tzk=", required=False)


# ===============================================
#  मुख्य रनिंग ब्लॉक (MAIN RUNNING BLOCK)
# ===============================================

if __name__ == "__main__":
    print("✅ Configuration loaded successfully from Render Environment Variables.")

    try:
        # Pyrogram क्लाइंट को शुरू करते हैं
        app = Client(
            "MovieBot", # Session Name. आप इसे "my_telegram_bot" से बदल सकते हैं।
            api_id=int(API_ID),
            api_hash=API_HASH,
            bot_token=BOT_TOKEN
        )
        
        # app.run() कमांड बॉट को शुरू करता है और इसे Render पर चालू रखता है।
        print("🚀 Starting the Pyrogram Bot...")
        app.run()
        
    
