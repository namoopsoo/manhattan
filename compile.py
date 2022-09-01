import yaml

from pathlib import Path
from glom import glom
from copy import deepcopy
from jinja2 import Template


def read_world():
    with open("world.yaml", "r") as file:
        world = yaml.safe_load(file)

    twee = ""

    begin_passage = make_begin_passage(world)
    twee += begin_passage

    map_passage = make_map_passage(world)
    twee += map_passage
    
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
        data["location_snake"] = snake(record["location"])
        print(data)

        output = Template(template).render(data)
        twee += output

    return twee
def snake(x):
    return x.replace(" ", "_").lower()

def make_begin_passage(world):
    """
    (set: $visited_west_village to false)
    (set: $secret_correct_west_village to false)
    (set: $favorite_number_dolphin_lewis to "876243")
    """
    lines = [ ]
    for record in world["occupants"]:
        location_snake = snake(record["location"])

        line = f"(set: $visited_{location_snake} to false)"
        lines.append(line)

        line = f"(set: $secret_correct_{location_snake} to false)"
        lines.append(line)

        snake_name = snake(record["occupant"]["name"])
        favorite_number = snake(record["occupant"]["favorite_number"])
        line = f"(set: $favorite_number_{snake_name} to \"{favorite_number}\")"
        lines.append(line)


    preamble = """:: Start
Welcome to the Manhattan Story !
(link: "Ready for adventure?")[==
[[go to map ->map]]

:: StoryTitle
A Manhattan story.

"""

    return preamble + "\n".join(lines)

def make_map_passage(world):

    preamble = """
:: map
the map
"""

    lines = [ ]
    for record in world["occupants"]:
        location = record["location"]
        line = f"[[{location}]]"
        lines.append(line)

    footer = """
<img src="assets/map.jpg" width="50%">
"""

    return preamble + "\n".join(lines) + footer


def save_twee(twee, location):
    with open(location, "w") as fd:
        fd.write(twee)
