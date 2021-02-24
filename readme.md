# **Discord Bot Documentation**

A bot that allows only links to be posted in channels. Whenever someone posts a non-link message, this bot deletes the message.
<br>
Has additional features which utilize some of the free Public APIs listed @ https://github.com/public-apis/public-apis

## Contents
* List of Available commands
* Try Running it yourself !

### List of available commands
I added some additional features to this bot as well ! Type the following commands in the chat to get a response from the bot !
* ```$greet``` - Greets the user and redirects to this repo.
![greet response](https://github.com/Kabiirk/discord_bots/blob/main/src/greet.png)
<br>

* ```$inspire``` - The bot sends randomly retreived Inspirational quotes fetched from [here](https://zenquotes.io/).
![inspire response](https://github.com/Kabiirk/discord_bots/blob/main/src/Inspire.png)
<br>

* ```$xkcd number``` - The bot sends randomly retreived Inspirational quotes fetched from [here](https://xkcd.com/).
![xkcd response](https://github.com/Kabiirk/discord_bots/blob/main/src/xkcd.png)
<br>

* ```$joke``` - The bot sends randomly retreived Inspirational quotes fetched from [here](https://official-joke-api.appspot.com/jokes/random).
![joke response](https://github.com/Kabiirk/discord_bots/blob/main/src/joke.png)

---

### Try Running it yourself
* **Install requirements**
    This can be done by navigating to the directory having requirments.txt and running the following in the terminal:
    ```
    pip install -r requirements.txt
    ```

* **Create your Discord own bot and generate it's Token**
    * You'll need to have a [Discord](https://discord.com/) account and make sure you have access to their [developer portal](https://discord.com/developers/docs/intro).
    * [Create a bot](https://discordpy.readthedocs.io/en/latest/discord.html#) and then generate a token and copy it.
    * [Add the bot to your Discord Server](https://discordpy.readthedocs.io/en/latest/discord.html#inviting-your-bot)
 
* **Run the project**
    * In the **first_bot.py** file, put your copied token in the ```client.run()``` function at the end as a string.
    * All that's left to do now is run the Project ! you can do so by :
```
python first_bot.py
``` 
or
```
python3 first_bot.py
```
The script has run successfully and your bot is functional if you see the following in the terminal :
```
The bot has started.
<BOT username>#number
```

## All Done :sparkles: