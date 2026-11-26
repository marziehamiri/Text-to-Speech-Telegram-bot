# Text-to-Speech Telegram Bot

A simple Telegram bot that converts text messages into speech using Google Text-to-Speech (gTTS) and sends the generated audio back to the user.

## Features

- Converts text messages into speech.
- Generates MP3 audio files using Google Text-to-Speech.
- Sends the generated audio as a voice message in Telegram.
- Supports English text.
- Automatically deletes the generated audio file after sending it.

## Requirements

- Python 3.8 or higher
- A Telegram Bot Token
- Internet connection

## Installation

1. Clone the repository:

```bash
git clone https://github.com/marziehamiri/Text-to-Speech-Telegram-bot.git
```

2. Navigate to the project directory:

```bash
cd Text-to-Speech-Telegram-bot
```

3. Install the required libraries:

```bash
pip install -r requirements.txt
```

## Configuration

Open the Python file and replace `token` with your Telegram Bot Token:

```python
API_TOKEN = 'YOUR_BOT_TOKEN'
```

You can obtain a bot token from [@BotFather](https://t.me/BotFather) on Telegram.

## Usage

1. Run the bot:

```bash
python main.py
```

2. Open your bot in Telegram.
3. Send `/start` to start the bot.
4. Send any English text message.
5. The bot converts your text into speech and replies with an audio message.

## Libraries

- [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/)
- [gTTS](https://pypi.org/project/gTTS/)

## License

This project is open-source and available for educational and personal use.
