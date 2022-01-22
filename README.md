# ccserver
A server and client for passing data between computercraft computers/turtles across dimensions or even servers.

```pastebin get zUnE5N0v client```

```lua
os.loadAPI("client")
client.put("computer1", "computer2", somedata) --send somedata from computer1 to computer2
client.get("computer2", "computer1") --receive data from computer1 to computer2
```
There is a queue for each computer pair, so you can put multiple times before having to get
