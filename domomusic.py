import paho.mqtt.client as mqtt
import webbrowser

urltrance = 'https://www.youtube.com/watch?v=RJWsPsmYvR0&ab_channel=MrSuicideSheep'
urltrance2 = 'https://www.youtube.com/watch?v=hJJSGVMs-3s&ab_channel=MrSuicideSheep'
urlhome = 'https://www.youtube.com/watch?v=tdTY6IpIG_g&list=PLeqnCMXayC8hA-93pbEVeInsuUv99cMCN&index=4&t=0s&ab_channel=Lightitup%21'
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("/myTopic")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    #webbrowser.open_new(url)
    if(msg.payload == 'home'):
        webbrowser.open(urlhome, new=1, autoraise=True)
    if(msg.payload == 'trance'):
        webbrowser.open(urltrance, new=1, autoraise=True)
    if(msg.payload == 'trance2'):
        webbrowser.open(urltrance2, new=1, autoraise=True)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("iot.eclipse.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
