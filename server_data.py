CHAT_LINK_CHANNEL = 688125129456484366

seed = '-8558479263656096884'

ips = {'survival': '158.69.122.191',
      'creative': '158.69.122.191:25564',
      'flatworld': '158.69.122.191:25567',
      'creative2': '109.247.2.239',
      'survival2': '158.69.122.191:25575'}

server_locations = {'spawn': '1 1',
                    'end_portal': '273 -21',
                    'vindicate': '224 -352',
                    'community_island': '80 -7',
                    'halloween district': '-1221 -1060'}

# whitelist = '../mscs/worlds/survival/whitelist.json'
whitelist = 'whitelist.json'
# scoreboard_path = '../mscs/worlds/survival/survival/data/scoreboard.dat'
scoreboard_path = 'scoreboard.dat'
stat_directory = '../mscs/worlds/survival/survival/stats'

console_in = "../mscs/worlds/survival/console.in"
console_out = "../mscs/worlds/survival/console.out"

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

                   'pick_uses': ('minecraft:diamond_pickaxe', 'minecraft:used'),
                   'hoe_uses': ('minecraft:diamond_hoe', 'minecraft:used'),
                   'axe_uses': ('minecraft:diamond_axe', 'minecraft:used'),
                   'shovel_uses': ('minecraft:diamond_shovel', 'minecraft:used'),
                   'sponges_placed': ('minecraft:sponge', 'minecraft:used'),
                   'slime_placed': ('minecraft:slime_block', 'minecraft:used'),
                   'stone_placed': ('minecraft:stone', 'minecraft:used'),
                   'grass_placed': ('minecraft:grass_block', 'minecraft:used'),
                   'rails_placed': ('minecraft:rail', 'minecraft:used'),

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
                  'witch_peri': 'PeriBlocksMined'}

objectives_m = ['distance_flown_m', 'distance_walked_m']
objectives_km = ['distance_flown_km', 'distance_walked_km']
