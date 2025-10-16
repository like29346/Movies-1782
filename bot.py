import os
import sys
# =============================================== 
#  Configuration Loader for Telegram Bot (Render/Server Use) 
# =============================================== 

def get_config(key, required=True):
    """Fetches environment variable and ensures critical keys are present."""
    value = os.getenv(key)
    
    
        
    return value.strip() if value else None


# --- Configuration Variables loaded from Render ---
API_ID = get_config("27699873")
API_HASH = get_config("4615359950a50d32c2ab3ad80475d87e")
BOT_TOKEN = get_config("8437160489:AAEKPj7yArqb7Viv8L_yh0ogn_ouRNJFUpM")
MONGO_URI = get_config("mongodb+srv://movies123:Movies@123@cluster0.cozjses.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Other essential keys
BOT_OWNER = [int(x) for x in get_config("5311840807").split()] if get_config("5311840807") else []
LOG_CHANNEL = int(get_config("LOG_CHANNEL")) if get_config("1002630246729") else None
UPDATE_CHANNEL = get_config("1003103870573")

# Optional Keys
DATABASE_URL = get_config("Database movies1782🎬", required=False)
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
            api_id=int(27699873),
            api_hash="4615359950ad32c2ab3d4b80475d87e",
            bot_token="8437160489:AAEKPj7yArqb7Viv8L_yh0ogn_ouRNJFUpM"

        )
        
        # app.run() कमांड बॉट को शुरू करता है और इसे Render पर चालू रखता है।
        print("🚀 Starting the Pyrogram Bot...")
try:
    app.run()              
except Exception as e:
    print(f"An error occurred: {e}")
