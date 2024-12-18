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

Follow these steps to get the bot up and running on your local machine:

### 1. Clone the repository

To get a copy of this project on your computer:

1. Ensure you have [Git](https://git-scm.com/downloads) installed on your computer.

2. Open your terminal or command prompt.

3. Run the following command to clone the repository:

    ```bash
    git clone https://github.com/c1lc1l/word-bot.git
    ```

4. After running the above command, the project will be downloaded to your computer.

### 2. Navigate to the project directory

Once the repository is cloned, change into the project directory:

```bash
cd discord-bot
```

### 3. Install Python and dependencies

Ensure you have Python installed on your machine. If not, you can download it from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can install the required dependencies using `pip`. Run the following command:

```bash
pip install -r requirements.txt
```

### 4. Verify installation

To verify that Python and `pip` are correctly installed, run the following commands:

```bash
python --version
pip --version
```

You should see the installed versions of Python and `pip` in your terminal.

---

## Setup

### 1. Create a `.env` file

In the root directory of your project, create a `.env` file and add the following content:

```plaintext
DISCORD_TOKEN=your_token_here
```

Replace `your_token_here` with your actual Discord bot token. You can obtain this token by creating a bot on the [Discord Developer Portal](https://discord.com/developers/applications).

---

## Usage

### 1. Run the bot

Once everything is set up, run the bot with this command:

```bash
python discord-bot.py
```

If everything is configured correctly, you should see the bot come online in your Discord server!

### 2. Available commands

Once the bot is running, you can use the following commands in your Discord server:

- `$sort <word1> <word2> <word3>`: Sort the words in ascending order.
- `$flip <word>`: Reverse the given word.
- `$count <word1> <word2>`: Count the total number of words.
- `$shuffle <word1> <word2> <word3>`: Shuffle the words randomly.

---

## Contributing

If you'd like to contribute to the project, feel free to fork the repository, make changes, and submit a pull request. Here are a few ways you can contribute:

1. Fixing bugs
2. Adding new features
3. Improving documentation

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
