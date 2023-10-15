
# Telegram Bot: Dollar-to-Ruble Exchange Rate Bot

This Telegram bot provides users with the current exchange rate of the US Dollar to the Russian Ruble, taking into account the predefined commission. The bot is built using Python and aiogram library, and the project uses Poetry for environment management. Firebase is used as the database for storing data.

## Prerequisites

Before running the bot, ensure you have the following prerequisites installed:

- Python (version 3.11 or higher)
- Poetry (version 1.6.1 or higher)
- Firebase account and project
- Telegram Bot Token

This Telegram bot provides users with the current exchange rate of the US Dollar to the Russian Ruble, taking into account the predefined commission. The bot is built using Python and aiogram library, and the project uses Poetry for environment management. Firebase is used as the database for storing data.


## Installation

1. Clone the repository:

   ````shell
   git clone git@github.com:NNakleskin/USD-RUB-currency-bot.git

   ````
2. Navigate to the project directory:

   ````shell
   cd USD-RUB-currency-bot

   ````
3. Install dependencies using Poetry:

   ````shell
   poetry install

   ````
4. Create a new file named `.env` in the project directory and add the following variables:

   ````plaintext
   BOT_TOKEN=<YOUR_TOKEN>
   FIREBASE_URL=<YOUR_URL>

   Replace `<YOUR_TOKEN>` with your Telegram Bot Token obtained from the BotFather. Replace `<YOUR_URL>` with the URL of your Firebase project.

   ````


## Firebase Configuration

Ensure you have set up a Firebase project and enabled the Firestore database. The `FIREBASE_URL` in the `.env` file should point to the URL of your Firebase project.

## Contributing

Contributions to this project are welcome. If you find any issues or want to add new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
