# Word Bot

Be sure to check out my [Dev.to Article](https://dev.to/c1lc1l/deploy-your-discord-bot-using-amazon-ec2-2mdm) on this project!  

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Setting Up the Bot on EC2](#setting-up-the-bot-on-ec2)
    1. [Launch an EC2 Instance](#launch-an-ec2-instance)
    2. [Connect to the EC2 Instance](#connect-to-the-ec2-instance)
    3. [Install Dependencies](#install-dependencies)
    4. [Clone the Repository](#clone-the-repository)
    5. [Set Up Environment Variables](#set-up-environment-variables)
    6. [Run the Bot](#run-the-bot)
    7. [Keep the Bot Running in the Background](#keep-the-bot-running-in-the-background)
5. [Usage](#usage)
6. [Troubleshooting](#troubleshooting)
7. [References](#references)
8. [Acknowledgements](#acknowledgements)

## Introduction

This is a simple Discord bot that responds to user commands. It was created using `discord.py` and can be deployed on an EC2 instance. This bot is designed for beginners to learn about deploying an application on AWS.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Git** installed on your local machine or EC2 instance.
- **Python 3** installed on your EC2 instance.
- A **Discord account** and a bot created in the [Discord Developer Portal](https://discord.com/developers/applications).
- **AWS account** with access to EC2.

## Installation

To set up this project on your local machine:

1. Clone this repository:
    ```bash
    git clone https://github.com/c1lc1l/word-bot.git
    cd word-bot
    ```
2. Install dependencies:
    ```bash
    pip3 install -r requirements.txt
    ```

3. Create a `.env` file in the root directory with your bot's token:
    ```plaintext
    DISCORD_BOT_TOKEN=your-discord-bot-token
    ```

## Setting Up the Bot on EC2

### Launch an EC2 Instance

1. **Sign in to AWS** and go to the **EC2 Dashboard**.
2. Click **Launch Instance** and select **Amazon Linux 2023 AMI**.
3. Choose an instance type (e.g., **t2.micro** for the free tier).
4. Configure your instance, including creating a security group with **SSH** access.
5. Download the `.pem` key file to SSH into the instance later.

### Connect to the EC2 Instance

1. Open **Git Bash** or **Terminal** on your local machine.
2. Navigate to the folder where your `.pem` key is located.
3. Change permissions for the `.pem` file:
    ```bash
    chmod 400 your-key-name.pem
    ```
4. SSH into your EC2 instance:
    ```bash
    ssh -i your-key-name.pem ec2-user@your-ec2-public-ip
    ```

### Install Dependencies

1. Update the package manager and install Python 3 and pip:
    ```bash
    sudo yum update -y
    sudo yum install python3 -y
    sudo yum install python3-pip -y
    ```

2. Install necessary Python packages (Discord and DotEnv):
    ```bash
    pip3 install discord.py python-dotenv
    ```

### Clone the Repository

1. Install Git:
    ```bash
    sudo yum install git -y
    ```

2. Use the clone command:
    ```bash
    git clone https://github.com/c1lc1l/word-bot.git
    cd word-bot
    ```

### Set Up Environment Variables

1. Create a `.env` file in the root directory:
    ```bash
    echo "DISCORD_BOT_TOKEN=your-discord-token" > .env
    ```

### Run the Bot

1. Run the bot on your EC2 instance:
    ```bash
    python3 discord-bot.py
    ```

### Keep the Bot Running in the Background

To keep the bot running after you close the terminal, use `screen`:

1. Install `screen`:
    ```bash
    sudo yum install screen -y
    ```

2. Start a new screen session:
    ```bash
    screen -S discord-bot
    ```

3. Run the bot inside the screen:
    ```bash
    python3 discord-bot.py
    ```

4. Detach from the screen session by pressing `Ctrl + A`, then `D`.
5. Reattach to the session later:
    ```bash
    screen -r discord-bot
    ```

## Usage

Once the bot is running, you can use the following commands in your Discord server:

- `$sort <word1> <word2> <word3>`: Sort the words in ascending order.
- `$flip <word1> <word2> <word3>`: Reverse the order of the words.
- `$flipsort <word1> <word2> <word3>`: Sort the words in descending order.
- `$count <word1> <word2> <word3>`: Count the number of words provided.
- `$shuffle <word1> <word2> <word3>`: Shuffle the words randomly.
- `$hello`: Get a random greeting from the bot.
- `$cil`: Get a fun easter egg message from the bot.

## Troubleshooting

### 1. **Bot Token Not Found in Environment Variables**  
**Error:**  
```
ERROR - DISCORD_BOT_TOKEN not found in environment variables.
```  
**Solution:** Ensure that the `.env` file is correctly placed in the root directory of the project and contains the correct Discord bot token. The `.env` file should look like this:  
```plaintext
DISCORD_BOT_TOKEN=your-discord-bot-token
```  
If you're using a terminal, make sure to load the environment variables properly. You can also manually set the token in the Python script as a temporary workaround.

### 2. **PyNaCl Not Installed**  
**Warning:**  
```
PyNaCl is not installed, voice will NOT be supported.
```  
**Solution:** This is just a warning and won't prevent the bot from running. If you need voice functionality, you can install PyNaCl by running:  
```bash
pip3 install pynacl
```

### 3. **Permission Denied (publickey) When Connecting to EC2**  
**Error:**  
```
Permission denied (publickey).
```  
**Solution:** This error typically occurs if the `.pem` key file has incorrect permissions or is not specified correctly. Ensure the `.pem` file has the correct permissions:  
```bash
chmod 400 your-key-name.pem
```  
Also, verify that you’re using the correct public IP address and the right key pair for your EC2 instance.

### 4. **No Matching Distribution Found for Package**  
**Error:**  
```
ERROR: No matching distribution found for ipython==8.28.0
```  
**Solution:** Ensure that you're installing the correct version of the package for your Python version. You may need to update `pip` and install the correct package versions:
```bash
python3 -m pip install --upgrade pip
```  
Then, retry installing the dependencies.

### 5. **EC2 Instance Not Accessible After Launch**  
**Error:**  
Unable to connect to the EC2 instance after launch.  
**Solution:** Ensure that your security group allows SSH access on port 22 and the public IP of the EC2 instance is correctly configured. Also, verify the `.pem` key file has the correct permissions:
```bash
chmod 400 your-key-name.pem
```

### 6. **Bot Not Responding in Discord**  
**Error:**  
Bot is not responding to messages.  
**Solution:** Verify that the bot is running by checking the logs. If necessary, restart the bot:
```bash
python3 discord-bot.py
```  
Ensure that your bot token is correctly configured in the `.env` file and that the bot is added to your Discord server.

### 7. **Screen Session Not Found**  
**Error:**  
```
There is no screen to be resumed matching discord-bot.
```  
**Solution:** Ensure that you’ve started a screen session correctly by running:
```bash
screen -S discord-bot
```  
To see all active screen sessions, run:
```bash
screen -ls
```
Then, reattach to the correct session:
```bash
screen -r <session-id>
```

## References

- [Discord.py Documentation](https://discordpy.readthedocs.io/en/stable/): The official documentation for the `discord.py` library, which is used for building the Discord bot.
- [AWS EC2 Documentation](https://docs.aws.amazon.com/ec2/): The official Amazon EC2 documentation for setting up and managing EC2 instances.

## Acknowledgements

Special thanks to my mentor, Isaeus Guiang, for provisioning the IAM accounts necessary for the EC2 instance and for his support and guidance throughout the development process.
