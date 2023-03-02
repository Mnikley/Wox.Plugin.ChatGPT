# Wox launcher ChatGPT Plugin
![logo2](https://user-images.githubusercontent.com/75040444/221229322-f9f4ad07-befb-46aa-b442-720c2ac5e6ca.jpeg)

A simple wrapper written in Python, HTML and CSS to utilize the OpenAI API that can be used as a Plugin for the awesome [Wox launcher](https://github.com/Wox-launcher/Wox). Uses Flask to display the results in a ChatGPT-themed locally-hosted webpage. Only tested on Windows with Python 3.10.

## Screenshots
![chatgpt_wox_plugin](https://user-images.githubusercontent.com/75040444/222425839-d88ef5a7-9074-473c-8cb1-12b42700f905.gif)


## Quickstart
 1. Clone the repo: `git clone https://www.github.com/Mnikley/Wox.Plugin.ChatGPT`
 2. Install requirements: `pip install -r requirements.txt`
 3. Get an OpenAI API key: https://platform.openai.com/account/api-keys
 4. Open and edit `app.py` to enter your API key:
   ```
   config = {
       "api_key": "place-your-api-key-here",
       ..
   }
   ```
 5. Copy the entire folder `Wox.Plugin.ChatGPT` to your Wox `Plugins` folder (per default: `C:\Users\MNikley\AppData\Local\Wox\app-1.4.1196\Plugins`) and make sure the plugin is enabled. Restart Wox afterwards
 6. Run queries by entering `gpt [QUERY]` in your Wox launcher prompt, e.g. `gpt what is love`

Alternatively you can run the script directly via `python app.py [QUERY]`

## Configuration
 - `api_key:` Your OpenAI API key
 - `model:` Used model (default: `gpt-3.5-turbo`, check https://platform.openai.com/docs/models/)
 - `max_tokens:` Maximum amount of returned tokens (longer = more expensive; default: `32`)
 - `temperature:` Increase randomness (default: `0.15`)
 - `stream:`: Stream response or wait for entire processed text (default: `True`)
 - `price_per_token:` Used for estimating costs (default: `0.002 / 1000` based on gpt-3.5-turbo)

## Run via command line
  1. Run app:
   ```
   python app.py
   ```
  2. Send queries via API endpoint `/openai_call/QUERY`, e.g.:
  ```
  http://127.0.0.1:5000/openai_call/how%20much%20is%20the%20fish
  ```
