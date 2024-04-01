# coding=utf-8
import re

from mcdreforged.api.event import LiteralEvent

PLUGIN_METADATA = {
    'id': 'death_api',
    'version': '0.0.1',
    'name': 'MCDR-death-api',
    'description': '玩家死亡事件',
    'author': 'Geniucker',
    'link': 'https://github.com',
    'dependencies': {
        'mcdreforged': '>=2.0.0',
    }
}

def on_info(server, info):
    death_message: str = info.content
    for i in DEATH_MESSAGES:
        if re.fullmatch(i, death_message):
            server.dispatch_event(
                LiteralEvent("death_api.on_death_message"),
                (death_message,)
            )
            break

DEATH_MESSAGES = (
    # Arrows
  "\\w{1,16} was shot by .+",
  # Snowballs
  "\\w{1,16} was pummeled by .+",
  # Cactus
  "\\w{1,16} was pricked to death",
  "\\w{1,16} walked into a cactus whilst trying to escape .+",
  # Drowning
  "\\w{1,16} drowned",
  "\\w{1,16} drowned whilst trying to escape .+",
  # Elytra
  "\\w{1,16} experienced kinetic energy",
  "\\w{1,16} experienced kinetic energy whilst trying to escape .+",
  # Explosions
  "\\w{1,16} blew up",
  "\\w{1,16} was blown up by .+",
  "\\w{1,16} was killed by [Intentional Game Design]",
  # Falling
  "\\w{1,16} hit the ground too hard",
  "\\w{1,16} hit the ground too hard whilst trying to escape .+",
  "\\w{1,16} fell from a high place",
  "\\w{1,16} fell off a ladder",
  "\\w{1,16} fell off some vines",
  "\\w{1,16} fell off some weeping vines",
  "\\w{1,16} fell off some twisting vines",
  "\\w{1,16} fell off scaffolding",
  "\\w{1,16} fell while climbing",
  "death.fell.accident.water",
  "\\w{1,16} was impaled on a stalagmite",
  "\\w{1,16} was impaled on a stalagmite whilst fighting .+",
  # Falling blocks
  "\\w{1,16} was squashed by a falling anvil",
  "\\w{1,16} was squashed by a falling anvil whilst fighting .+",
  "\\w{1,16} was squashed by a falling block",
  "\\w{1,16} was squashed by a falling block whilst fighting .+",
  "\\w{1,16} was skewered by a falling stalactite",
  "\\w{1,16} was skewered by a falling stalactite whilst fighting .+",
  # Fire
  "\\w{1,16} went up in flames",
  "\\w{1,16} walked into fire whilst fighting .+",
  "\\w{1,16} burned to death",
  "\\w{1,16} was burnt to a crisp whilst fighting .+",
  # Firework rockets
  "\\w{1,16} went off with a bang",
  "\\w{1,16} went off with a bang due to a firework fired from .+",
  # Lava
  "\\w{1,16} tried to swim in lava",
  "\\w{1,16} tried to swim in lava to escape .+",
  # Lightning
  "\\w{1,16} was struck by lightning",
  "\\w{1,16} was struck by lightning whilst fighting .+",
  # Magma Block
  "\\w{1,16} discovered the floor was lava",
  "\\w{1,16} walked into danger zone due to .+",
  # Magic
  "\\w{1,16} was killed by magic",
  "\\w{1,16} was killed by magic whilst trying to escape .+",
  "\\w{1,16} was killed by .+",
  # Powder Snow
  "\\w{1,16} froze to death",
  "\\w{1,16} was frozen to death by .+",
  # Players and mobs
  "\\w{1,16} was slain by .+",
  "\\w{1,16} was fireballed by .+",
  "\\w{1,16} was stung to death",
  "death.attack.sting.item",
  "\\w{1,16} was shot by a skull from .+",
  "death.attack.witherSkull.item",
  # Starving
  "\\w{1,16} starved to death",
  "\\w{1,16} starved to death whilst fighting .+",
  # Suffocation
  "\\w{1,16} suffocated in a wall",
  "\\w{1,16} suffocated in a wall whilst fighting .+",
  "\\w{1,16} was squished too much",
  "\\w{1,16} was squashed by .+",
  # Sweet Berry Bushes
  "\\w{1,16} was poked to death by a sweet berry bush",
  "\\w{1,16} was poked to death by a sweet berry bush whilst trying to escape .+",
  # Thorns enchantment
  "\\w{1,16} was killed trying to hurt .+",
  "\\w{1,16} was killed by .+",
  # Trident
  "\\w{1,16} was impaled by .+",
  # Void
  "\\w{1,16} fell out of the world",
  "\\w{1,16} didn't want to live in the same world as .+",
  # Wither effect
  "\\w{1,16} withered away",
  "\\w{1,16} withered away whilst fighting .+",
  # Drying out
  "\\w{1,16} died from dehydration",
  "\\w{1,16} died from dehydration whilst trying to escape .+",
  # Generic death
  "\\w{1,16} died",
  "\\w{1,16} died because of .+",
  # Unsendable death messages
  "\\w{1,16} was roasted in dragon breath",
  "\\w{1,16} was roasted in dragon breath by .+",
  # Unused death messages
  "\\w{1,16} was doomed to fall",
  "\\w{1,16} was doomed to fall by .+",
  "\\w{1,16} fell too far and was finished by .+",
  "\\w{1,16} was stung to death by .+",
  "\\w{1,16} went off with a bang whilst fighting .+",
  "\\w{1,16} was killed by even more magic",
  # Temporary
  "\\w{1,16} was too soft for this world",
  "\\w{1,16} was too soft for this world .+",

  "\\w{1,16} was killed"
)