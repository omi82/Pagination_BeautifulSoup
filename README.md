# Movie Scripts Scraper

This Python script scrapes movie scripts from the [SubsLikeScript](https://subslikescript.com) website. The script navigates through multiple pages to extract links to individual movie scripts and saves the scripts as text files.

## Features

- Scrapes movie script links from the first two pages of the "movies_letter-A" section.
- Extracts and saves the title and transcript of each movie script.
- Handles pagination to navigate through multiple pages.
- Includes error handling for missing articles and non-functional links.

## Requirements

- Python 
- `requests` library
- `beautifulsoup4` library
- `lxml` parser
