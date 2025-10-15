from pathlib import Path 
import os 
 
env_generator = """#!/usr/bin/env python3 
# =============================================== 
#  Safe .env Generator for Telegram Bot 
# =============================================== 
# This script interactively asks you for values and creates a .env file. 
# Your sensitive data never leaves your computer. 
 
import os 
 
print("🛠️  Telegram Bot .env Generator") 
print("Fill in your details below. Press Enter to skip any optional field.") 
print("------------------------------------------------------") 
 
def ask(key, example="", secret=False): 
    prompt = f"{key}" 
    if example: 
        prompt += f" (e.g. {example})" 
    prompt += ": " 
    val = input(prompt) 
    return val.strip() 
 
fields = { 
    "API_ID": ask("API_ID", "27699873"), 
    "API_HASH": ask("API_HASH", "4615359950a50d32c2ab3ad80475d87e"), 
    "BOT_OWNER": ask("BOT_OWNER", "5311840807"), 
    "UPDATES_CHANNEL": ask("UPDATES_CHANNEL", "1003103870573"), 
    "DATABASE_URL": ask("DATABASE_URL", "Database movies1782🎬"), 
    "MONGO_URI": ask("MONGO_URI", "MONGO_URI": ask("MONGO_URI", "mongodb+srv://movies123:Movies@123@cluster0.cozjses.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
"), 
    "UPDATES_CHANNEL_USERNAME": ask("UPDATES_CHANNEL_USERNAME", "@Movies_ Update"), 
    "BROADCAST_AS_COPY": ask("BROADCAST_AS_COPY", "True or False"), 
    "CHANNEL_ID": ask("CHANNEL_ID", "1002630246729"), 
    "USER_SESSION_STRING": ask("USER_SESSION_STRING", "(your session string)"), 
    "BOT_USERNAME": ask("BOT_USERNAME", "@movies1872BOT"), 
    "BOT_TOKEN": ask("BOT_TOKEN", "8437160489:AAEKPj7yArqb7Viv8L_yh0ogn_ouRNJFUpM"), 
    "BOT_SESSION_NAME": ask("BOT_SESSION_NAME", "movies1872BOT"), 
    "LOG_CHANNEL": ask("LOG_CHANNEL", "1002630246729") 
} 
 
env_content = "\\n".join([f"{k}={v}" for k, v in fields.items() if v]) 
env_path = Path(".env") 
env_path.write_text(env_content, encoding="utf-8") 
 
print("\\n✅ .env file created successfully at", env_path.resolve()) 
print("------------------------------------------------------") 
print("You can now run your bot with: python3 bot.py") 
""" 
 
script_path = Path("/mnt/data/generate_env.py") 
script_path = Path("generate_env.py")
 
os.chmod(script_path, 0o755) 
 
{"path": str(script_path), "size_bytes": script_path.stat().st_size}
