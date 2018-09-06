from configparser import ConfigParser
import json
import re

configfilename = "./CTF-PhaserQuest.cfg"
configinfo = ConfigParser()
configinfo.read(configfilename)
try:
    configinfo.read(configfilename)
except:
    print("Unable to read config file")
    exit(1)

phaserquestdb = "./assets/json/db.json"
phaserquestdb_json = open(phaserquestdb, "r")
phaserquestdb_json = json.load(phaserquestdb_json)


def modify_npc_diaglogue(json_data, character_name, dialogue):
    dialogue_items = re.findall(r'\"(.+?)\"', dialogue)
    json_data["npc"][character_name]["dialogue"] = dialogue_items


def save_modified_json(json_data, outputfile):
    outputfile = open(outputfile, "w+")
    json.dump(json_data, outputfile, sort_keys=True, indent=4)

npc_dialogues = configinfo["npc-dialogue"]
for entry in npc_dialogues:
    dialogue_to_insert = npc_dialogues[entry]
    modify_npc_diaglogue(phaserquestdb_json, entry, dialogue_to_insert)

save_modified_json(phaserquestdb_json, phaserquestdb)
