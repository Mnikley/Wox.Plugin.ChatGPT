# ChatGPT Plugin for Wox
![chatgpt](https://user-images.githubusercontent.com/75040444/221224882-a5297b4e-dd01-42af-a9fa-1556cc0842aa.png)

A simple wrapper written in Python, HTML and CSS to utilize the OpenAI API that can be used as a Plugin for the awesome [Wox launcher](https://github.com/Wox-launcher/Wox). Uses Flask to display the results in a ChatGPT-themed webpage.

## Screenshots
![chatgpt_wox_plugin](https://user-images.githubusercontent.com/75040444/221225355-8c28b5bc-f390-4bcf-905d-fec023554623.gif)

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
 6. Run queries by entering `gpt [QUERY]`, e.g. `gpt what is love`

Alternatively you can run the script directly via `python app.py [QUERY]`

## Configuration
 - `api_key:` Your OpenAI API key
 - `model:` Used model (default: `text-davinci-003`, check https://platform.openai.com/docs/models/)
 - `max_tokens:` Maximum amount of returned tokens (longer = more expensive; default: `32`)
 - `temperature:` Increase randomness (default: `0.15`)
 - `stream:`: Stream response or wait for entire processed text (default: `True`)
 - `price_per_token:` Used for estimating costs (default: `0.1200 / 1000` based on text-davinci-003)

## Next steps
- add Markdown support
