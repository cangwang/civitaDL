

from modules.custom.downloader.scripts.ch_lib import model_action_civitai
import json

list = [{"url": "https://civitai.com/api/download/models/107366", "model_type": "lora", "subfolder_str": "\\"},
        {"url": "https://civitai.com/api/download/models/130090", "model_type": "ckp", "subfolder_str": "\\"}]

def download(reset=False):
    data = json.loads(json.dumps(list))
    for item in data:
        model_action_civitai.download(item['url'], item['model_type'], item['subfolder_str'], reset)