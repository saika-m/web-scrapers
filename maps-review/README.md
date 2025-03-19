# Google Maps Reviews Scraper

*When you want to find out a places review*

## Note: This will only give you the reviews with comments, cuz that's all I need

## Usage
```
python3 -m venv venv
```
```
source venv/bin/activate
```
### Open the Google Maps Page of the place desired, go to the FULL review section, scroll through to make sure all is loaded
### Open inspect on google maps web,
### Find and Copy the title of the most inner layer that contains all the reviews (That should copy all enclosed)
### Put it in input.txt
```
python main.py
```
### Read from output.md
``
If you are in vscode, "control + shift + p", and find "Markdown: Open Preview to the side" for better viewing experience
``
