# ROSQuery

Basic script to pull data from osquery over SSH using keypair auth.

## To Do

* Build list of queries
  * query list based on target host
* Authorization process

## Input

```
./main ~/.ssh/gnome-king gking@172.17.243.163 "osqueryi --json \"select * from os_version;\""
```

## Example
```json
[

  {
      "build":"",
      "codename":"bionic",
      "major":"18",
      "minor":"4",
      "name":"Ubuntu",
      "patch":"0",
      "platform":"ubuntu",
      "platform_like":"debian",
      "version":"18.04.4 LTS (Bionic Beaver)"
      }

]
```
```json
[
  {
    "description": "Paul",
    "directory": "/home/paul",
    "gid": "1000",
    "gid_signed": "1000",
    "shell": "/bin/bash",
    "uid": "1000",
    "uid_signed": "1000",
    "username": "paul",
    "uuid": ""
  }
]
```
