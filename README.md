# DevQuiz Bot

A Telegram bot for practising programming through short quizzes.
It greets you depending on the time of day, asks what you want to study today
and helps you learn with tests, theory cards and personal statistics.

The bot is developed as a course project for the **Cross-Platform Programming** discipline.

## Idea

Preparing for interviews and exams is easier in small steps. DevQuiz Bot lets you
pick a programming topic right in Telegram and choose how you want to study:

1. The bot greets you: **Good morning / Good afternoon / Good evening**, depending on the time.
2. It asks: **What are we studying today?** and offers a list of topics.
3. After you choose a topic, the main menu opens with four sections.

| Section             | What it does                                                                                                 |
| ------------------- | ------------------------------------------------------------------------------------------------------------ |
| 📝 **Quiz**         | Test questions with answer options. After each answer the bot shows whether it was correct and explains why. |
| 📖 **Theory**       | A list of questions on the topic. Tap a question and see the answer with an explanation right away.          |
| ✅ **Success rate** | How many correct and wrong answers you gave in quizzes, with a percentage.                                   |
| 📈 **Progress**     | How many questions of each topic you have already completed, e.g. _Python: 12 of 30_.                        |

### Topics

- Python
- JavaScript
- React
- SQL / Databases
- Node.js

## Features

| Feature                                                                 | Status     |
| ----------------------------------------------------------------------- | ---------- |
| Bot created and customised in BotFather (avatar, description, commands) | ✅ Done    |
| `/start` — greeting depending on the time of day                        | ✅ Done    |
| `/about` — information about the bot and the content source             | ✅ Done    |
| Topic selection                                                         | 🚧 Planned |
| Quiz mode                                                               | 🚧 Planned |
| Theory mode                                                             | 🚧 Planned |
| Success rate                                                            | 🚧 Planned |
| Progress                                                                | 🚧 Planned |
| Storing questions and answers in MongoDB                                | 🚧 Planned |

## Technologies

| Technology                                                | Purpose                                               |
| --------------------------------------------------------- | ----------------------------------------------------- |
| [Python 3.11+](https://www.python.org/)                   | Programming language                                  |
| [aiogram 3](https://docs.aiogram.dev/)                    | Asynchronous framework for Telegram bots              |
| [asyncio](https://docs.python.org/3/library/asyncio.html) | Asynchronous processing of user messages              |
| [python-dotenv](https://pypi.org/project/python-dotenv/)  | Loading the bot token from the `.env` file            |
| [MongoDB](https://www.mongodb.com/)                       | Database for questions, users and answers _(planned)_ |
| [Motor](https://motor.readthedocs.io/)                    | Asynchronous MongoDB driver for Python _(planned)_    |
| Telegram Bot API (long polling)                           | Receiving updates from Telegram                       |

### Planned data model

| Collection  | What is stored                                                            |
| ----------- | ------------------------------------------------------------------------- |
| `questions` | Topic, question text, answer options, correct option, explanation         |
| `users`     | Telegram user data                                                        |
| `answers`   | Who answered which question, the chosen option and whether it was correct |

Success rate and Progress are calculated from the `answers` collection.

## Project structure

```
devquiz_bot/
├── main.py            # Bot entry point: handlers and polling
├── requirements.txt   # Python dependencies
├── .env.example       # Example of the environment file
├── .gitignore
└── avatar.png         # Bot profile picture
```

## Getting started

1. Install Python 3.11 or newer.
2. Clone the repository:

   ```
   git clone https://github.com/AlexandraKurylo/devquiz-bot.git
   cd devquiz-bot
   ```

3. Install the dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Create a bot with [@BotFather](https://t.me/BotFather) and copy its token.
5. Create a `.env` file next to `main.py` (use `.env.example` as a template):

   ```
   BOT_TOKEN=your_token_from_BotFather
   ```

6. Run the bot:

   ```
   python main.py
   ```

7. Open the bot in Telegram and press **Start**.

> The `.env` file contains the secret token and is excluded from the repository by `.gitignore`.

## Commands

| Command  | Description                      |
| -------- | -------------------------------- |
| `/start` | Start the bot and get a greeting |
| `/about` | About the bot                    |

## Content and credits

All quiz questions are written for this project.
The idea and the format of the questions are inspired by
**[DevLovers](https://www.devlovers.net)** — a platform for preparing for technical interviews.

## Author

Oleksandra Kurylo
