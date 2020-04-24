# chat link channel
CHAT_LINK_CHANNEL = 688125129456484366

# define the channel id's for the different channels it wants to mention
welcome = 611184121024086016
how_to_apply = 677626692335960064
self_roles = 611188046339244032
server_rules_and_info = 611184197041651718
general_chat = 611184705693417472
introduce_yourself = 635534011325743111

seed = '-8558479263656096884'

ips = {'survival': '',
       'creative': '',
       'flatworld': '',
       'flatworld2': '',
       'test': ''}

server_locations = {'spawn': '1, 1',
                    'end portal': '273, -21',
                    'vindicate': '224, -352',
                    'community island': '80, -7',
                    'halloween district': '-1221, -1060',
                    'ghast farm': '80, -191',
                    'gold farm': '192, -9',
                    'sand farm old': '-239, -360',
                    'sand farm new': '-1088, 2045',
                    'witch farm': '245, 53',
                    'flower farm': '63, -112',
                    'slime farm': '-873, 1512',
                    'gravel mining 1': '-328, -102',
                    'gravel mining 2': '614, 8',
                    'gravel mining 3': '-128, -574',
                    'gravel mining 4': '442, 650',
                    'mining mesa': '-789, 60',
                    'mesa quarry': '1804, 1783',
                    'diamond mining north entrance': '351, -1628',
                    'diamond mining south entrance': '353, -1496',
                    'diamond mining north end portal': '470, -1673',
                    'diamond mining south end portal': '250, -1330',
                    'wither killer': '51, 26',
                    'gravel farm': '-1201, 1809',
                    'project chicken': '-836, 16'}

whitelist = '../mscs/worlds/survival/whitelist.json'

scoreboard_path = '../mscs/worlds/survival/survival/data/scoreboard.dat'
stat_directory = '../mscs/worlds/survival/survival/stats'

console_in = "../mscs/worlds/{}/console.in"
console_out = "../mscs/worlds/{}/console.out"

# map the commands to the  JSON file stat.json containing the built in scoreboards
JSON_objectives = {'play_minutes': ('minecraft:play_one_minute', 'minecraft:custom'),
                   'deaths': ('minecraft:deaths', 'minecraft:custom'),
                   'time_since_death_minutes': ('minecraft:time_since_death', 'minecraft:custom'),
                   'time_since_death_hours': ('minecraft:time_since_death', 'minecraft:custom'),
                   'open_shulker': ('minecraft:open_shulker_box', 'minecraft:custom'),
                   'mobs_killed': ('minecraft:mob_kills', 'minecraft:custom'),
                   'traded': ('minecraft:traded_with_villager', 'minecraft:custom'),
                   'distance_flown_m': ('minecraft:fly_one_cm', 'minecraft:custom'),
                   'distance_walked_m': ('minecraft:fly_one_cm', 'minecraft:custom'),
                   'distance_flown_km': ('minecraft:fly_one_cm', 'minecraft:custom'),
                   'distance_walked_km': ('minecraft:fly_one_cm', 'minecraft:custom'),

                   'hoe_uses': ('minecraft:diamond_hoe', 'minecraft:used'),
                   'axe_uses': ('minecraft:diamond_axe', 'minecraft:used'),
                   'shovel_uses': ('minecraft:diamond_shovel', 'minecraft:used'),
                   'sponges_placed': ('minecraft:sponge', 'minecraft:used'),
                   'slime_placed': ('minecraft:slime_block', 'minecraft:used'),
                   'stone_placed': ('minecraft:stone', 'minecraft:used'),
                   'grass_placed': ('minecraft:grass_block', 'minecraft:used'),
                   'rails_placed': ('minecraft:rail', 'minecraft:used'),
                   'dragon_egg_placed': ('minecraft:dragon_egg', 'minecraft:used'),

                   'redstone_torches_crafted': ('minecraft:redstone_torch', 'minecraft:crafted'),
                   'repeaters_crafted': ('minecraft:repeater', 'minecraft:crafted'),
                   'pistons_crafted': ('minecraft:piston', 'minecraft:crafted'),
                   'comparators_crafted': ('minecraft:comparator', 'minecraft:crafted'),
                   'observers_crafted': ('minecraft:observer', 'minecraft:crafted'),
                   'droppers_crafted': ('minecraft:dropper', 'minecraft:crafted'),

                   'quartz_mined': ('minecraft:nether_quartz_ore', 'minecraft:mined'),
                   'diamonds_mined': ('minecraft:diamond_ore', 'minecraft:mined'),
                   'obsidian_mined': ('minecraft:obsidian', 'minecraft:mined')}

# map the commands to the NBT file scoreboard.dat containing the custom scoreboards
NBT_objectives = {'slime_peri': 'BlocksMinedPeri',
                  'witch_peri': 'PeriBlocksMined',
                  'project_chicken': 'ProjectChicken',
                  'pick_uses': 'DiamondPickUses'}

# objectives that need value conversions for the scoreboard
objectives_m = ['distance_flown_m', 'distance_walked_m']
objectives_km = ['distance_flown_km', 'distance_walked_km']

servers = ['survival', 'creative', 'flatworld']

# death messages to sent death messages to chat
death_messages = ['was shot by arrow', 'was shot by ', 'was pricked to death', 'hugged a cactus',
                  'walked into a cactus while trying to escape', 'was stabbed to death',
                  'drowned whilst trying to escape', 'experienced kinetic energy', 'removed an elytra while flying',
                  'blew up', 'was blown up by', 'hit the ground too hard', 'fell from a high place',
                  'fell off a ladder', 'fell off some vines', 'fell out of the water', 'fell into a patch of fire',
                  'fell into a patch of cacti', 'was doomed to fall by', 'was shot off some vines by',
                  'was shot off a ladder by', 'was blown from a high place by', 'was squashed by a falling anvil',
                  'was squashed by a falling block', 'went up in flames', 'burned to death',
                  'was burnt to a crisp whilst fighting', 'walked into a fire whilst fighting', 'went off with a bang',
                  'tried to swim in lava', 'tried to swim in lava while trying to escape', 'was struck by lightning',
                  'Magma Block', 'discovered floor was lava', 'was slain by', 'got finished off by', 'was fireba',
                  'was killed by magic', 'was killed by', 'starved to death', 'Suffocation', 'suffocated in a wall',
                  'was squished too much', 'was killed while trying to hurt', 'fell out of the world',
                  'fell from a high place and fell out of the world', 'withered away', 'was pummeled by', 'died']

server_mappings = {'CMP': 'creative',
                   'SMP': 'survival',
                   'FMP': 'flatworld'}
