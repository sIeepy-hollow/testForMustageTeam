# Exchange Rate Monitoring Bot

## Project Description
This project features a Telegram bot designed to monitor the exchange rate of the US Dollar to the Ukrainian Hryvnia. The bot automatically updates data every hour using Google Finance, saves it to a local database, and provides it to users on request in the form of an Excel file.

## Key Features
- Automatic collection of exchange rate data every hour.
- Storage of historical exchange rate data in a local database.
- Ability for users to request the latest data in Excel format.

## Technologies
- Python 3.8+
- Aiogram for Telegram bot creation
- Selenium for web scraping
- SQLAlchemy for database interaction
- Pandas for data manipulation and Excel file creation
- Schedule for task scheduling

## Installation and Setup
To get this project up and running, follow these steps:


### Setting Up the Virtual Environment

- python -m venv venv
- source venv/bin/activate  # On Unix
- venv\Scripts\activate  # On Windows

### Installing Dependencies

- pip install -r requirements.txt

### Configuring Environment Variables
Create a .env file in the project root and add the following variables:
- TOKEN=<Your_Telegram_Bot_Token>

### Running the Bot
- python main.py

### Running the Parser (in a separate process/terminal)
- python tasks.py