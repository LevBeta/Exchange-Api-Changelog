# API Exchange Change-Log Notifier (Very Alpha Version)

## Overview

This project is a simple tool for monitoring and notifying users about updates to the change-log of a specific API exchange. In its current early version, it supports monitoring the Bybit exchange's change-log and sends notifications to users via a Telegram bot.

## Features

- Monitors the change-log of the Bybit exchange.
- Sends notifications to users via Telegram.
- Easily extendable to support other exchanges and notification methods in the future. (More easily in the next versions)

![image](https://github.com/LevBeta/Exchange-Api-Changelog/assets/105949605/65f39a84-965d-43f4-a1bd-fab6b9f38f7f)


## TO-DO

Currently, the monitoring system updates only once every 24 hours. To provide more timely updates, we need to adjust the script to poll for changes at shorter intervals. So the logic behing checking updates will have to change

## Prerequisites

Before using this tool, make sure you have the following:

- Python 3.x installed on your system.
- A Telegram bot API key and user chat ID to receive notifications.

## Getting Started

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/api-exchange-changelog.git
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Update the config.toml
   ```bash
   TELEGRAM_API_KEY = "your_telegram_bot_api_key"
   TELEGRAM_USER_ID = "your_telegram_user_chat_id"
   ```

4. Run the tool
   ```bash
   python3 main.py
   ```

## Extending for Other Exchanges
To extend this tool to support other exchanges, follow these steps:

1. Create a new Python file for the exchange (e.g., myexchange.py) within the exchanges directory.
2. Implement the logic for monitoring the change-log of your desired exchange in this file.
3. Modify the main.py to import and use the new exchange module.


## License

[MIT](https://choosealicense.com/licenses/mit/)

