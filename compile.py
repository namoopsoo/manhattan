import yaml

from pathlib import Path



def read_world():

    with open('world.yml', 'r') as file
        world = yaml.safe_load(file)

    template = Path("location.template").read_text()
    for occupant in world:
        friend = occupant["friend"]
        friend_location = world[]
        data = {}
    output = Template(template).render(
            # occupant="HiImAnOccupant",
            # friend="Im a Friend"
            )
    return output
    # print(output)

read_world()
