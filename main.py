# -*- coding: utf-8 -*-
from wox import Wox
import subprocess


class ChatGPTPlugin(Wox):

    # query is default function to receive realtime keystrokes from wox launcher
    def query(self, query):
        results = []
        results.append({
            "Title": "ChatGPT",
            "SubTitle": "Query: {}".format(query),
            "IcoPath": "Images/chatgpt_green.png",
            "ContextData": "ctxData",
            "JsonRPCAction": {
                'method': 'take_action',
                'parameters': ["{}".format(query)],
                'dontHideAfterAction': False
            }
        })
        return results

    def take_action(self, query):
        subprocess.Popen(["python", "app.py", query]).wait()


if __name__ == "__main__":
    ChatGPTPlugin()
