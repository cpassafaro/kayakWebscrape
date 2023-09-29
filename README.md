# kayakWebscrape
scrape the internet for best deals on whitewater kayaks
test

to run in the terminal you must have python installed and run python3 then directory to kayak.py
### Example python3 .vscode/kayak.py

## Requirement File
Displays all the requirements to run this application. To create a requirement file in an application go into the file directory in the terminal with the project at the root and run the following
``` pip freeze > requirements.txt

### Run as an api
This application is using Python language with FastApi library to create a lightweight and versitile api for kayak browsing. The server is hoster by uvicorn.
To run locally ensure that both of FastApi and Uvicorn are installed locally. Then in terminal provide the path to uvicorn and then the command
For Example:
```
/home/christinapassafaro/.local/bin/uvicorn main:app --reload