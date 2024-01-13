# Reddit Comment Scraper

## Description
This project is a Reddit comment scraper developed in Python. It allows users to enter the ID of a Reddit post and extract all comments and their replies, saving the data to a JSON file.

## Features
- Graphical user interface for ease of use.
- Extraction of all comments and replies from a specified Reddit post.
- Display of the total number of comments and replies after scraping.
- Ability to save the data to a JSON file.

## Technologies Used
- Python
- Tkinter for the graphical interface
- PRAW (Python Reddit API Wrapper) for accessing Reddit data: https://www.reddit.com/prefs/apps

## How to Use
1. Clone the repository to your local machine.
2. Install the necessary dependencies, including `praw` and `tkinter`.
3. Run the Python script.
4. Enter the ID of the Reddit post in the graphical interface.
5. Click "Scrape" to start extracting comments.
6. Upon completion, a summary of the total comments and replies will be displayed.
7. Click "Save" to save the data to a JSON file.

## Installation
Ensure you have Python installed on your computer. Then, install the required dependencies:

```bash
pip install praw
