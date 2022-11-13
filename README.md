# `hiyorin`

a.k.a. [Izumi Hiyori](https://vndb.org/c87837) (thanks cv6)

a discord bot for home seedbox management

# usage
this is mainly intended for me but if u want to use it how would i stop u
(also you need animebytes account so if u dont have that then sorry can't help)

put this into `config.yaml` and fill in as needed:
```yaml
bot:
  prefix: "hiyorin " # born to shit forced to wipe (born to use slash commands forced to have a prefix lol) 
  token: "" # discord token
  home_base_id: 0 # put a guild id here, by using this we don't have to wait for sync
services:
  animebytes: "" # priv tracker passkey
  animebytes_username: "" # needed in api request
transmission:
  host: "127.0.0.1"
  port: 9091
  username: "transmission"
  password: "" # rpc password
```

run a `pipenv sync` then `pipenv run python bot.py` and you're good to go hopefully

# license
mit