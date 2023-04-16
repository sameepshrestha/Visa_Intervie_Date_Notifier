from telethon import TelegramClient
import os
# from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure
api_id= 25987704
api_hash="7f542b8c63fab4d36f7f274ffad48d01"
client = TelegramClient('anon', api_id, api_hash) 
async def main():
    # Getting information about yourself
    me = await client.get_me()
    # "me" is a user object. You can pretty-print
    async for dialog in client.iter_dialogs(): 
    #extract id for each chat in the telegram
        print(dialog.name, 'has ID', dialog.id)
    messages = await client.get_messages(-1001567966058,3)
    # print(message)
    for m in messages:
        m.text

with client:
    client.loop.run_until_complete(main())
