<br>
<p align="center">
  <img alt="HackUPC" src="https://github.com/hackupc/frontend/raw/master/src/images/hackupc-ogimage@2x.png" width="620"/>
</p>
<br>

# Biene bot

## Overview
HackUPC Slack helper bot implemented in Python and using LUIS by Microsoft for making IA interaction easier.

## Requirements
1. Python 3.5+
2. docker-ce (as provided by docker package repos)
3. docker-compose (as provided by PyPI)

## Recommendations
Usage of [virtualenv](https://realpython.com/blog/python/python-virtual-environments-a-primer/) is recommended for package library / runtime isolation.

## Usage
To run the server locally, please execute the following from the root directory:

1. Setup virtual environment
```bash
mkvirtualenv -p python3 biene-bot
```

2. Install dependencies
```bash
pip3 install -r requirements.txt
```

3. Copy `__init__.template.py` to `__init__.py` with correct values

4. Run Startup server as python module
```bash
python3 -m hackupc.bienebot
```

## Deploy locally

via docker-compose
```bash
docker-compose up -d --build
```

## Restart locally

```bash
sh restart.sh
```

## Log

Run logs from docker-compose once it's up and running
```bash
docker-compose logs -f --timestamps bienebot
```

## Production

Inspired on this [tutorial](https://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/) to understand and set it up as in our server.

Needs: Systemd.

- Edit this file `/lib/systemd/system/biene-bot.service`
- Add this content

    ```
    [Unit]
    Description=Biene bot
    After=multi-user.target
    
    [Service]
    Type=idle
    WorkingDirectory=/home/user/project_folder
    ExecStart=/home/user/project_folder/env/bin/python -m hackupc.bienebot
    
    [Install]
    WantedBy=multi-user.target
    ```

- Replace `project_folder` by the name of the folder where the project is located
- Create and enable service:

    ```bash
    sudo systemctl start biene-bot && sudo systemctl enable biene-bot
    ```

## Documentation

This bot is implemented in `Python` for all the backend stuff. `LUIS` from Microsoft is being used as a library for making the AI easier. This library allows you to classify the topics, called `Intents` by LUIS, that bot can answer. These are the available topics in Biene Bot:

### Activities

> Intent: `Indication.Activity`

Topic related to the activities during the weekend.

#### Sub-intents
- Help: Tell what can you ask to the bot.
- What: Explanation of a given activity.
- When: Time schedule of a given activity.
- Where: Location of a given activity.
- Which: List all activities.

### Error

> Intent: `None`

Topic used when the bot does not understand the question.

### HackUPC

> Intent: `HackUPC`

Topic related to general questions about the event.

#### Sub-intents
- When: Dates of the hackathon.
- Where: Hackathon location.
- Schedule: Full agenda of the event.
- Next: Get the following event in HackUPC.

### Hardware Lab

> Intent: `HardwareLab`

Topic related to Hardware Lab stuff.

#### Sub-intents
- Exist: Existence of the HW Lab.
- Help: Tell what can you ask to the bot.
- How: Functioning explanation.
- List: All available HW Lab.

### Logistics

> Intent: `Logistics`

Topic related to all Logistics matters.

#### Sub-intents
- How: Explanation about the functioning of a given logistics item.
- When: Time schedule of a given logistics item.
- Where: Location of a given logistics item.

### Meals

> Intent: `Meals`

Topic related to all meals.

#### Sub-intents
- Coffee: Coffee information.
- Help: Tell what can you ask to the bot.
- Schedule: Full meals schedule.
- Snacks: Snacks information.
- Special: Special meals for vegan/vegetarian, intolerant...
- Where: Meals location.
- Which: Detail information about meals.

### Mentor

> Intent: `Mentor`

Topic related to HackUPC Mentors.

#### Sub-intents
- Help: Explanation about mentors functioning.

### Places

> Intent: `Indication.Place`

Topic related to venue information.

#### Sub-intents
- Help: Tell what can you ask to the bot.
- When: Time schedule of a given venue item.
- Where: Location of a given venue item.

### Projects

> Intent: `Project`

Topic related to project information.

#### Sub-intents
- Build: Tell what can you build in HackUPC.
- Demo: Tell how the project demonstration works.
- Deploy: Tell how to deploy your hack.
- Five: Sub-topic about overflow on team size.
- Help: Tell what can you ask to the bot.
- NoTeam: Tell what to do without team.
- Prizes: Prizes information.
- Requisites: Project requirements.
- Team: Sub-topic about team size.

### Random

> Intent: `Smalltalk`

Topic related to random stuff.

#### Sub-intents
- DifLanguage: Tell to talk in English.
- Goodbye: Just say bye.
- Hello: Just say hi.
- Help: Tell what can you ask to the bot.
- HowAreYou: Just asking how are you.
- Joke: Jokes for fun.
- Nice: Cool, awesome, great...
- ProjectIdea: Random and maybe useful project ideas.
- Thanks: Biene bot is a gentle woman
- Tip: Tips are always useful.
- NotJoke: Not joking answers.
- WhoAreYou: Just asking who are you.
- Father: Who knows he is her father.
- BeClever: Clever answers.
- IsClever: For sure she's clever.
- Age: Good question, her age.
- IsFunny: Because she's funny.
- AnswerGood: When she hits the correct answer.
- Single: Do want to date with her?

### Sponsors

> Intent: `Sponsors`

Topic related to sponsor information.

#### Sub-intents
- AllChallenges: List all challenges from sponsors.
- Challenge: Information about challenge of a given sponsor.
- Contact: Information about how to contact to a given sponsor.
- Help: Tell what can you ask to the bot.
- Where: Information about location of a given sponsor.
- Which: List all sponsors.

### Support

> Intent: `Support`

Topic related to organization support.

#### Sub-intents
- Contact: How to find an organizer.
- Problem: What to do in an urgent and/or serious issue.

## License

MIT © Hackers@UPC