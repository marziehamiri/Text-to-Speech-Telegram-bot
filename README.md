# Telegram Text-to-Speech Bot

A simple Telegram bot built with Python that converts text messages into speech and sends the generated audio back to users.

The bot uses Google Text-to-Speech (gTTS) to generate MP3 audio from text messages and delivers the result as a voice message in Telegram.

## Features

- Convert text messages into speech.
- Generate English speech using gTTS.
- Use an Australian English accent (`com.au`).
- Send generated audio as a Telegram voice message.
- Automatically delete temporary audio files after sending.
- Handle incoming text messages automatically.

## Technologies Used

- Python
- pyTelegramBotAPI
- gTTS

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/marziehamiri/Telegram-Text-to-Speech-Bot.git
```

**2. Navigate to the project directory**

```bash
cd Telegram-Text-to-Speech-Bot
```

**3. Create a virtual environment**

```bash
python -m venv venv
```

**4. Activate the virtual environment**

Windows:

```bash
venv\Scripts\activate
```

**5. Install the required libraries**

```bash
pip install -r requirements.txt
```

## Configuration

Create a Telegram bot using [BotFather](https://t.me/BotFather) and get your API token.

Set your token in the `API_TOKEN` variable in `main.py`.

For security reasons, do not publish your actual Telegram bot token on GitHub.

## Usage

1. Run the bot:

```bash
python main.py
```

2. Open your Telegram bot.
3. Send the `/start` command.
4. Send an English text message.
5. Receive the generated speech as a voice message.

## Project Structure

```text
Telegram-Text-to-Speech-Bot/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How It Works

1. The bot receives a text message from the user.
2. The message text is passed to gTTS.
3. gTTS converts the text into speech.
4. The generated audio is saved as an MP3 file.
5. The bot sends the audio to the user as a voice message.
6. The temporary MP3 file is deleted after sending.

## Requirements

```text
pyTelegramBotAPI
gTTS
```

## Author

Marzieh Amiri

