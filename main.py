#############################################################
########### Bears Are Back Bot Discord Bot ###########
###############################################

import os
import discord
import random


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        msg = message.content.lower()

        print(msg)
        # Ignore messages from the bot itself
        if message.author == client.user:
            return
        # Respond to any message that contains "Bears" and "suck" and does not contain "not" or DONT
        if JF in msg or JF1 in msg or BEARS in msg or JUSTIN in msg or FIELDS in msg or JUSTIN_FIELDS in msg:
            if BACK in msg:
                if NOT in msg:
                    await message.channel.send("WRONG! Bears are back!")
                else:
                    await message.channel.send("Bears are back!")
            if (SUCK in msg or ASS in msg or STINK in msg) and DONT not in msg and DO_NOT not in msg:
                await message.channel.send(random.choice(RESPONSES))
        if "packers" in msg:
            await message.channel.send("Fuck the Packers")
        if "back?" == msg:
            await message.channel.send("Bears are back!")


#    @client.event
#	async def on_member_join(member):
#    	print("Recognised that a member called " + member.name + " joined")
#    	try:
#        	await client.send_message(member, newUserMessage)
#        	print("Sent message to " + member.name)
#    	except:
#        	print("Couldn't message " + member.name)
#    	embed=discord.Embed(
#        	title="Welcome "+member.name+"!"
#        	description="We're so glad you're here!"
#        	color=discord.Color.green()
#    	)

token = "MTA1MDYxNDY4MDMwMjkzMjA0OA.Gkk6H7.mjEvhDKDsXLWIHjz6BINmdgvucRURL7YK1U_lQ"
# Dictionary of Words
BEARS = "bears"
NOT_BACK = "not back"
BACK = "back"
SUCK = "suck"
STINK = "stink"
NOT = "not"
DONT = "dont"
DO_NOT = "do not"
ASS = "ass"
JF = "jf"
JF1 = "jf1"
JUSTIN = "justin"
JUSTIN_FIELDS = "justin fields"
FIELDS = "fields"
BEARS_JF_WORDS = [BEARS, JF, JF1, JUSTIN, FIELDS, JUSTIN_FIELDS]
bears_are_not_back_arr = [BEARS, NOT, BACK]
RESPONSES = ["Fuck you", "Hey, be nice", "That is not true", "Bears are BACK!!!", "Ban this douchebag"]

client = MyClient()
client.run(token)