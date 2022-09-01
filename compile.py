import yaml

from pathlib import Path
from glom import glom
from copy import deepcopy
from jinja2 import Template


def read_world():
    with open("world.yaml", "r") as file:
        world = yaml.safe_load(file)
    
    occupants = {glom(x, "occupant.name"): x for x in world["occupants"]}
    template = Path("location.template").read_text()
    for record in world["occupants"]:
        friend = glom(record, "occupant.friend")
        friend_location = occupants[friend]["location"]
        friend_favorite_number = occupants[friend]["occupant"]["favorite_number"]
        data = deepcopy(record)
        data["friend_location"] = friend_location
        data["friend_favorite_number"] = friend_favorite_number
        data["occupant"]["name_snake"] = glom(record, "occupant.name").replace(" ", "_").lower()
        print(data)

        output = Template(template).render(
                data
                # occupant="HiImAnOccupant",
                # friend="Im a Friend"
                )
        print(output)
        break
    #return twee
        # print(output)

