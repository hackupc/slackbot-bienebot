import re
from io import BytesIO
from os import listdir
from os.path import isfile, join
from PIL import Image

import requests


def set_profile(message, client, user):
    mention = re.findall('\<(.*?)\>', message)
    if mention:
        user = mention[0].replace(' ', '').replace('@', '')
    path = 'hackupc/bienebot/slack/commands/profile_filters'
    filter_type = None
    for file in listdir(path):
        if isfile(join(path, file)) and file.replace('.png', '') in message:
            filter_type = file
    filter_photo = Image.open(join(path, filter_type)).convert("RGBA")
    user = user.upper()
    response = client.users_info(user=user)
    url = response.data['user']['profile']['image_original']
    response = requests.get(url)
    profile = Image.open(BytesIO(response.content)).resize((512, 512)).convert("RGBA")
    profile.paste(filter_photo, (0, 0), filter_photo)
    result = BytesIO()
    profile.save(result, 'PNG')
    response = client.conversations_open(users=user)
    client.files_upload(file=result.getvalue(), filename='profile.png', filetype='png',
                        channels=response.data['channel']['id'])
    return True
