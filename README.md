# Jasper Tracker API
This is being used to read data from the postgresql database for the Rasa tracker store and then has api calls to only give back the ones that were out of scope aka failed intents.

Still dealing with an issue where the data column is coming back as text and not actual json formatted.

# Running
To run this you need to setup your venv:

`python3 -m venv .venv`

Activate it:

`source .venv/bin/activate`

Install dependencies:

`pip install -r requirements.txt`

Run the app:

`doppler run -- uvicorn tracker_events.main:app --reload`