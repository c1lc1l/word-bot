# Word Bot

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
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

This is a simple Discord bot that responds to user commands. It was created using `discord.py` and can be deployed on an EC2 instance. This bot is designed for beginners to learn about deploying a bot on AWS.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Git** installed on your local machine or EC2 instance.
- **Python 3** installed on your EC2 instance.
- A **Discord account** and a bot created in the [Discord Developer Portal](https://discord.com/developers/applications).
- **AWS account** with access to EC2.

## Installation

To set up this project on your local machine or EC2 instance:

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/word-bot.git
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

2. Install necessary Python packages:
    ```bash
    pip3 install discord.py python-dotenv
    ```

### Clone the Repository

1. Install Git:
    ```bash
    sudo yum install git -y
    ```

2. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/word-bot.git
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

Once the bot is running, it will listen for messages in your Discord server. You can interact with the bot based on the commands you’ve set up in the code.