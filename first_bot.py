import discord
import requests
import json
from urllib import parse as urlparse

client = discord.Client()

# Functions executed in the program go here
def url_check(url):
    if urlparse.urlparse(url).scheme:
        return True
    else:
        return False

def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' -'+json_data[0]['a']
    
    return(quote)


# Main Implementation
@client.event
async def on_ready():
    print("The bot has started.")
    print('{0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author==client.user:
        return
        
    if url_check(message.content):
        pass
    
    else:
        # Functions that the bot performs on the server go here

        # ignore if the message is from the bot itserl client.user reffers to the bot
        # (which is the user in this case)
        if message.author==client.user:
            return
        elif message.content.startswith('$inspire'):
            quote = get_quote()
            await message.channel.send(quote)
            return
        elif message.content.startswith('$greet'):
            await message.channel.send('Hello '+str(message.author)+' !'+'\n'+'You can look up my documentation @ :'+'LINK')
            return
        # END

        # Deletes messages if they don't begin with $inspire or $greet or don't contain links
        await message.delete()
        await message.channel.send("This is a Links-only Channel ! Kindly post valid Links only.")


client.run('Paste your token Here')