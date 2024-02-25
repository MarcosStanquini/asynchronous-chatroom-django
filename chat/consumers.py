from channels.generic.websocket import AsyncWebscoketConsumer
import json

class ChatRoomConsumer(AsyncWebscoketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_grupo_name = 'chat_%s' % self.room_name
        
        await self.channel_layer.group_add(
            self.room_grupo_name,
            self.channel_name

        )

        await self.channel_layer.group_send(
            self.room_grupo_name,
            {
                'type': 'tester_message', 
                'tester': 'tester',
            }
        )

    async def tester_message(self, event):
        tester = event['tester']

        await self.send(text_data=json.dumps({
               'tester': tester,

           })) 


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_grupo_name,
            self.channel_name
        )    
    pass