from channels.routing import route


channel_routing = [
    route("ws.socket", "pootle_ws.consumers.ws_message"),
]
