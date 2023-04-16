from telethon import TelegramClient, events
import asyncio
from twilio.rest import Client
account_sid = "ACfb96e1ecdda7dc86b5ad936a80c1e95c"
auth_token = "ead7e9ca9b3a4fef47839b22287b920f"
client1 = Client(account_sid, auth_token)

api_id= 25987704
api_hash="7f542b8c63fab4d36f7f274ffad48d01"
client = TelegramClient('anon', api_id, api_hash) 
client.start()
@client.on(events.NewMessage(chats=[-1001567966058,6146456582,-887686977]))
async def handler(event):
    # Respond whenever someone says "Hello" and something else
    messages= event.message.text
    if "2023" in messages:
        print(messages)
        message = client1.messages.create(
        body="VISA INTERVIEW date khulyo hare"+messages,
        from_="+16205429208",
        to="+9779842538253")
    # await asyncio.sleep(5)

with client:
    client.run_until_disconnected()