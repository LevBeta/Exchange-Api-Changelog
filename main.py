import tomli
from exchanges.bybit import bybit_check_updates
from notifications.telegram import tg_send_message

config_dict = {}

def fetch_config():
    global config_dict
    with open("config.toml", "rb") as file:
        config = tomli.load(file)

    config_dict = {
        "NOTIFICATIONS_METHOD": config.get("NOTIFICATIONS_METHOD"),
        "TELEGRAM_API_KEY": config.get("TELEGRAM_API_KEY"),
        "TELEGRAM_USER_ID": config.get("TELEGRAM_USER_ID")
    }


##Refactor when add more exchanges##
def check_updates():
    while True:
        update = bybit_check_updates()  
        print(config_dict)
        if update != None:
            tg_send_message(
                config_dict["TELEGRAM_API_KEY"], 
                config_dict["TELEGRAM_USER_ID"],
                update,
                "Bybit"
            )


def main():
    fetch_config()
    check_updates()

if __name__ == "__main__":
    main()