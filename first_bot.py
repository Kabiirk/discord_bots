import discord
import requests
import json
from urllib import parse as urlparse

client = discord.Client()

# Functions executed in the program go here
# ======================================================================================================================
def url_check(url):
    # check wether URL format if correct or not
    url_scheme = urlparse.urlparse(url).scheme
    # e.g. of result
    # urlparse.urlparse('https://www.youtube.com/')
    # ParseResult(scheme='https', netloc='www.youtube.com', path='/', params='', query='', fragment='')

    
    if(len(url_scheme)<=0):
        return False, "This is a links-only channel, Kindly only post valid https links only."
        # url_scheme empty for normal text
        # e.g. 
        # urlparse.urlparse('$jokeasgf')
        # ParseResult(scheme='', netloc='', path='', params='', query='', fragment='')
        # scheme for normal strings would be an empty string, exits the function before
        # the below if-else block is even executed so that the funtion doesn't return
        # "This bot only allows links following https scheme." which is also a valid condition
        #  for ftp, http etc links & therefore a different usecase than a normal string.

    # Only allows https URLs with a valid response
    if(url_scheme != 'https'):
        return False, "This bot only allows links following https scheme."

    else:
        try:
            # check wether it's a legit URL with proper response (200 etc.)
            # would filter out stuff like https://www.not_a_url.com
            #
            # RESPONSE CODE RANGES:
            # Informational responses (100–199)
            # Successful responses (200–299)
            # Redirects (300–399)
            # Server & Client Errors => (400-599)
            response = requests.get(url)

            # Put code to handle multiple response codes
            return True, None
        
        except requests.ConnectionError as exception:
            return False, "Seems like the website doesn't exist, try sending another link :)."

def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' -'+json_data[0]['a']
    
    return(quote)

def get_xkcd(comic_id):
    url = "https://xkcd.com/"+str(comic_id)+"/info.0.json"
    response = requests.request("GET", url)
    json_data = json.loads(response.text)
    img_link = json_data['img']
    
    return img_link

def get_joke():
    url = "https://official-joke-api.appspot.com/jokes/random"
    response = requests.request("GET", url)
    json_data = json.loads(response.text)
    joke = json_data['setup'] + '\n\n' + json_data['punchline']
    
    return joke
# ======================================================================================================================

# Main Implementation
@client.event
async def on_ready():
    print("The bot has started.")
    print('{0.user}'.format(client))


@client.event
async def on_message(message):
    # ignore if the message is from the bot itserl client.user reffers to the bot
    # (which is the user in this case)
    if message.author==client.user:
        return
    
    # Take only the first word
    first_word = message.content.split(" ", 1)[0] 

    # boolean, string
    valid_url, error_text = url_check(message.content)
        
    # Don't do anything to the message if it a valid url
    if valid_url:
        pass
    
    else:
        # Functions that the bot performs on the server go here
        if(first_word=='$inspire'):
            quote = get_quote()
            await message.channel.send(quote)
            return
        elif first_word=='$greet':
            await message.channel.send('Hello '+str(message.author)+' !'+'\n'+'You can look up my documentation @ : '+'https://github.com/Kabiirk/discord_bots')
            return
        elif first_word=='$xkcd':
            comic_id = message.content.split(" ",1)[1]
            if(comic_id == '0'):
                await message.channel.send("Comic stip not indexable, try another number")
            else:
                comic_img_link = get_xkcd(comic_id)
                await message.channel.send(comic_img_link)
            return
        elif first_word=='$joke':
            joke = get_joke()
            await message.channel.send(joke)
            return

        # Deletes messages whose first word isn't $inspire, $greet etc. or aren't links
        await message.delete()
        if(error_text != None):
            await message.channel.send(error_text)


client.run('ODEzMDU0NzgwNDQ3OTE2MDYz.YDJuRQ.TFcpadpzKncYsmbs10KNzsGieHo')