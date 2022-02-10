import discord
from yttranscript import summarizer
#to load bot_token
from dotenv import load_dotenv
import os

#BOT CREDENTIALS
load_dotenv('.env')



class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        global video_link
        # we do not want the bot to reply to itself

        if message.author.id == self.user.id:
            return

        if message.content.startswith('!help '):
            await message.channel.send('1.  !summarize <youtube-video-link> ---  to summarize transcript of youtube video provided.')

        if message.content.startswith('!summarize '):
            s = message.content.split()
            video_link = s[1]
            print(video_link)
            await message.channel.send('Hello, {0.author.mention}! summarizing youtube video...'.format(message))
            StringFormContent = ""
            for i in summarizer(video_link):
                StringFormContent += i
            
            if len(StringFormContent) < 2000:
                await message.channel.send(StringFormContent)
            
            else:
                await message.channel.send(StringFormContent[:len(StringFormContent)//2])
                await message.channel.send(StringFormContent[len(StringFormContent//2):])



client = MyClient()
client.run(os.getenv('BOT_TOKEN'))