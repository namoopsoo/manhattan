import yaml

from pathlib import Path



def read_world():

    with open('world.yml', 'r') as file
        world = yaml.safe_load(file)

    template = Path("location.template").read_text()
    output = Template(template).render(occupant="HiImAnOccupant", friend="Im a Friend")
    print(output)

read_world()
