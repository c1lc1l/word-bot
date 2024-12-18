# Discord Word Bot

A simple and interactive **Discord bot** built with **Python** that offers word-related functionalities such as sorting, flipping, counting, and more.

## Features

- Sort words alphabetically
- Reverse words
- Count words
- Shuffle words randomly
- And more fun commands!

---

## Installation

Follow these detailed steps to get the bot up and running on your local machine:

### 1. Clone the repository  
Clone this repository to your local machine using Git. Open your terminal and run:  
`git clone https://github.com/yourusername/yourrepositoryname.git`  
Replace `yourusername` and `yourrepositoryname` with your actual GitHub username and repository name.

### 2. Navigate to the project directory  
Change to the directory where the repository was cloned. Run the following command:  
`cd discord-bot`  
This will take you to the folder containing all the project files.

### 3. Install Python and dependencies  
Ensure you have Python installed on your machine. If you don’t, you can download it from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can install the required dependencies using `pip`. Run the following command to install the packages listed in the `requirements.txt` file:  
`pip install -r requirements.txt`  
This will automatically install all necessary libraries, such as `discord.py` and `python-dotenv`, that are required to run the bot.

### 4. Verify installation  
To verify that Python and `pip` are correctly installed, you can run the following commands:  
`python --version`  
`pip --version`  
You should see the installed versions of Python and pip in your terminal.

---

## Setup

### 1. Create a `.env` file  
In the root directory of your project, create a `.env` file and add the following content:  
`DISCORD_TOKEN=your_token_here`  
Replace `your_token_here` with your actual Discord bot token. You can obtain this token by creating a bot on the [Discord Developer Portal](https://discord.com/developers/applications).

---

## Usage

### 1. Run the bot  
Once everything is set up, run the bot with this command:  
`python discord-bot.py`  
If everything is configured correctly, you should see the bot come online in your Discord server!

### 2. Available commands  
Once the bot is running, you can use the following commands in your Discord server:

- `$sort <word1> <word2> <word3>`: Sort the words in ascending order.
- `$flip <word1> <word2> <word3>`: Reverse the order of the words.
- `$flipsort <word1> <word2> <word3>`: Sort the words in descending order.
- `$count <word1> <word2> <word3>`: Count the number of words provided.
- `$shuffle <word1> <word2> <word3>`: Shuffle the words randomly.
- `$hello`: Get a random greeting from the bot.
- `$cil`: Get a fun easter egg message from the bot.

---

## Troubleshooting

If you encounter any issues, please check the following:

- Ensure your Discord bot token is correctly set in the `.env` file.
- Verify that all dependencies are installed using `pip install -r requirements.txt`.
- If the bot isn't responding, make sure your bot is added to a Discord server where it has appropriate permissions to send messages.

For additional help, feel free to open an issue on the GitHub repository.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.