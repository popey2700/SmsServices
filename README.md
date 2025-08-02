# SmsServices

## Setup

1. FastApi

   1. Install Python - this was written using 3.11.2
   2. Create a venv in the root of repo: `python -m venv .venv`
   3. Activate your venv:

      ```bash
      # In cmd.exe
      source .venv\Scripts\activate.bat
      # In PowerShell
      source .venv\Scripts\Activate.ps1
      # In Git Bash
      source .venv/Scripts/activate
      # In Linux or Macos
      source .venv/bin/activate
      ```

   4. Install Python requirements: `pip install -r requirements.txt`
   5. Create a .env file in the root of the repo and obtain the keys from a maintainer.

## Running the app locally

1. Run the app: `fastapi dev app/main.py`
2. To test locally use a ephemeral port like NGROK and set the Twilio webhook to point to the url: `ngrok http http://localhost:8000`

## Deployment

- This App is deployed on a free render server, redeployments occur on pushes to main.
