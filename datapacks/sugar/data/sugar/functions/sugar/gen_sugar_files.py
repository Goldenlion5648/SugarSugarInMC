import itertools as it
import os
import sys
sys.path.insert(0, r'C:\Users\cobou\Documents\Curse\Minecraft\Instances\CommandCreations1_19_2\python_helpers')
from helper_functions import *
import helper_functions
setup = OutputFile("setup")
helper_update = OutputFile("update")
helper_functions.UPDATE_JSON_FILE = f"{os.path.dirname(__file__)}\\..\\..\\..\\minecraft\\tags\\functions\\tick.json"
# print(sys.path)
class Tags(Enum):
    # CARD_OUTLINE_TAG = "card_outline"

    def __str__(self):
        return str(self.value)
    
game_corner = (100, 0, 100)
wall_dims = (50, 55, 0)
offset_corner = (50, 55, -3)
game_height = wall_dims[1]
background_block = "red_concrete"
painting_block = "light_blue_concrete"
sugar_block = "white_concrete"
platform_block = "stone"
sugar_for_current_level_score = "sugar_for_current_level"
create_scoreboard(sugar_for_current_level_score)
spawn_sugar_cooldown_score = "spawn_sugar_cooldown"
sugar_in_cup_score = "sugar_in_cup"
sugar_needed_in_cup_score = "sugar_needed_in_cup"
create_scoreboard(sugar_in_cup_score)
cup_counter_tag = "cup_counter"
random_decider_tag = "random_decider"

# cup_opening_block = "quartz_block"
color_to_cup_opening = {
    "white_concrete": "quartz_block",
    "orange_concrete": "waxed_copper_block",
}

platform_center = (125, 24, 65)
high_corner = element_wise(wall_dims, game_corner)

place_wall = OutputFile("place_wall")
place_wall.extend(
    fill(element_wise(game_corner, element_wise(offset_corner, (20, 20, -10))), game_corner, "air") +
    fill(game_corner, high_corner, background_block) +
    border(element_wise(game_corner, (0,0,-1)), element_wise(element_wise(wall_dims, (0,0,-1)), game_corner), "dark_oak_wood")
    # fill(element_wise(game_corner, (0,0,-1)), element_wise(element_wise(wall_dims, (0,0,-1)), game_corner), 'black_concrete', 'outline')
)


# place_sugar = OutputFile("place_sugar")

# place_sugar.extend(
#     execute_as_at(at_a(), anchored_eyes=True,to_run=
#         execute_if_block_matches("~ ~-2 ~", platform_block,
#             execute_if_block_matches("^ ^ ^", platform_block,

#             )
#         )
#     )
# )




paint_brush_tag = "paint_brush"
# shoot_testing = OutputFile("shoot_testing")
# shoot_testing.extend(
#     shoot_facing(moving_entity='marker', bullet_label_tag=paint_brush_tag, step=1, code_to_run_after_step=
#         execute_if_block_matches("~ ~ ~", background_block,
#             setblock("^ ^ ^-1", painting_block, mode="keep") +
#             kill(at_s())
#         ), repeats_per_tick=100
#     )
# )

replace_around_bullet = OutputFile("replace_around_bullet")
replace_around_bullet.extend(
    execute_as_at(at_e(tag=paint_brush_tag), 
        execute_if_block_matches("~ ~ ~", background_block,
            setblock("^ ^ ^-1", painting_block) +
            kill(at_s())
        )
    )
)


hacky_shoot_facing = OutputFile("hacky_shoot_facing")
positions = ["^ ^ ^-1",
"^ ^1 ^-1",
"^ ^-1 ^-1",
"^1 ^ ^-1",
"^-1 ^ ^-1"]
brush_replaceable_tag = BlockTag("brush_replaceable", 
'air')
brush_replaceable_tag.extend(color_to_cup_opening.keys())
hacky_shoot_facing.extend(
    it.chain.from_iterable(
        execute_at(f"^ ^ ^{offset}",
            execute_if_block_matches("~ ~ ~1", background_block,
                [
                    setblock_filtered(f"~{x_off} ~{y_off + 1} ~", painting_block,brush_replaceable_tag)[0] 
                    for x_off in [0]
                    for y_off in [0]
                    # for x_off in range(-1, 2)
                    # for y_off in range(-1, 2)
                ]
                # setblock("^ ^ ^-1", painting_block, mode='keep') +
                # setblock("^ ^1 ^-1", painting_block, mode='keep') +
                # setblock("^ ^-1 ^-1", painting_block, mode='keep') +
                # setblock("^1 ^ ^-1", painting_block, mode='keep') +
                # setblock("^-1 ^ ^-1", painting_block, mode='keep')
            ), anchored_eyes=True
        ) for offset in range(1, 70)
    )
)

hacky_shoot_facing.extend(
    raw('''advancement revoke @a only sugar:using_painting_item''')
)

#  execute_if_score_other_score(score1 : str, op: str, score2: str, to_run : list, owner1: str=GLOBAL_VAR_HOLDER, owner2: str=GLOBAL_VAR_HOLDER, if_or_unless='if'):

is_painting_score = "is_painting"
old_is_painting_score = "old_is_painting"
# create_scoreboard(old_is_painting_score, -1, at_a())

activate_painting = OutputFile("activate_painting", is_update_file=True)
activate_painting.extend(
    execute_as_at(at_a(),
        execute_unless_score_equals_score(is_painting_score, old_is_painting_score, owner1=at_s(), owner2=at_s(), to_run=
            call_function(hacky_shoot_facing) + 
            operation(old_is_painting_score, '=', is_painting_score, at_s(), at_s())
        )
    )
)

sugar_tag = "sugar"
sugar_maker = OutputFile("sugar_maker")
sugar_maker.extend(
    raw('summon marker ~ ~ ~ {NoGravity:1b,Silent:1b,Marker:1b,Invisible:1b,NoBasePlate:1b,PersistenceRequired:1b,Motion:[0.0,0.0,0.0],Tags:["__sugar_tag__"],ArmorItems:[{},{},{},{id:"minecraft:white_concrete",Count:1b}]}'.replace("__sugar_tag__", sugar_tag)) + 
    setblock("~ ~ ~", sugar_block)
)

def convert_to_color():
    z_off_set = 1
    converter_to_block = {
        "orange_wool" : "orange_concrete"
    }
    return list(it.chain.from_iterable(
        execute_as_at(at_e(tags=[sugar_tag]), to_run=
            execute_if_block(f"~{x_off} ~ ~{z_off_set}", converter, 
                setblock(HERE, to_block)
            )
        ) for x_off in range(-1, 2) for converter, to_block in converter_to_block.items()
    ))

def enter_cup(x_off, y_off1, y_off2):
    return \
        list(it.chain.from_iterable([
            execute_if_block(HERE, sugar_block, 
                execute_if_block(f"~{x_off} ~{y_off1} ~", cup_opening, 
                    execute_if_block(f"~{x_off} ~{y_off2} ~", cup_opening, 
                    # TODO: check sugar color against cup color
                        execute_if_score(sugar_needed_in_cup_score, 'matches 1..',
                            owner=at_e(tag=cup_counter_tag,sort='nearest',limit=1,distance="..4"),
                            to_run=
                            decrement_with_bound(sugar_needed_in_cup_score, 0, at_e(tag=cup_counter_tag,sort='nearest',limit=1,distance="..4")) +
                            setblock("~ ~ ~", AIR) +
                            kill(at_s())
                        )
                    )
                )
            )
            for sugar_block, cup_opening in color_to_cup_opening.items()
        ]))

def movement_code(y_dir=-1):
    return list(it.chain.from_iterable(
        execute_as_at(at_e(tags=[sugar_tag, has_not_moved_tag],sort='furthest'), to_run=
            enter_cup(x_off, y_off1, y_off2)
        ) +
        execute_as_at(at_e(tags=[sugar_tag, has_not_moved_tag],sort='furthest'), to_run=
            execute_if_block(f"~{x_off} ~{y_off1} ~", AIR, 
                execute_if_block(f"~{x_off} ~{y_off2} ~", AIR, 
                    add_tag(at_s(), should_move_tag)
                )
            )
        ) +
        execute_as_at(at_e(tag=should_move_tag,sort='furthest'), 
            clone(HERE, HERE, f"~{x_off} ~{y_dir} ~") +
            setblock("~ ~ ~", AIR) +
            tp(at_s(), f"~{x_off} ~{y_dir} ~") +
            # setblock("~ ~ ~", sugar_block) +
            remove_tag(at_s(), has_not_moved_tag) +
            remove_tag(at_s(), should_move_tag)
        ) for x_off, (y_off1, y_off2) in [
            (0, (y_dir, y_dir)), 
            (-1, (0, y_dir)), 
            (1, (0, y_dir))
        ]
    ))

    

has_not_moved_tag = "has_not_moved"
sugar_movement = OutputFile("sugar_movement", is_update_file=True)
should_move_tag = 'should_move'

collected_sugar_score = "collected_sugar"
gravity_direction_is_down_score = "gravity_direction_is_down"
sugar_movement.extend(
    execute_if_score_equals(spawn_sugar_cooldown_score, 0,
        execute_as_at(at_e(tags=[sugar_tag]),
            tag_add(at_s(), has_not_moved_tag)
        ) + execute_if_score_equals(gravity_direction_is_down_score, 1,
            movement_code()
        ) + execute_if_score_equals(gravity_direction_is_down_score, 0,
            movement_code(1)
        )
    ) + convert_to_color()
)

sugar_spawner = OutputFile("sugar_spawner", is_update_file=True)
remaining_sugar_to_dispense_score = "remaining_sugar_to_dispense"
create_scoreboard(remaining_sugar_to_dispense_score, 30)
middle_top_of_board = ((high_corner[0] + game_corner[0]) // 2 + .5, high_corner[1] - 7.5, game_corner[2] - .5)
sugar_spawner.extend(
    execute_if_score_matches(remaining_sugar_to_dispense_score, '1..', 
        execute_if_score_equals(spawn_sugar_cooldown_score, 0,
            execute_positioned(middle_top_of_board,
                execute_if_block(HERE, AIR,
                    call_function(sugar_maker) +
                    operation(remaining_sugar_to_dispense_score, '-=', 1)
                )
            )
        )
    )
)

remove_all_sugar = OutputFile("remove_all_sugar")
remove_all_sugar.extend(
    execute_as_at(at_e(tag=sugar_tag),
        setblock("~ ~ ~", AIR)
    ) +
    kill(at_e(tag=sugar_tag))
)

flip_gravity = OutputFile("flip_gravity")
flip_gravity.extend(
    execute_if_score_equals(gravity_direction_is_down_score, 1,
        delay_code_block(
            set_score(gravity_direction_is_down_score, 0),
            1
        )
    ) + execute_if_score_equals(gravity_direction_is_down_score, 0,
        delay_code_block(
            set_score(gravity_direction_is_down_score, 1),
            1
        )
    )
)


reset_scores = OutputFile("reset_scores")
reset_scores.extend(
    set_score_from_other_score(remaining_sugar_to_dispense_score, sugar_for_current_level_score),
    set_score(is_painting_score, 0, at_a()),
    set_score(old_is_painting_score, 0, at_a()),
    set_score(gravity_direction_is_down_score, 1),
    set_score(spawn_sugar_cooldown_score, 100),
)

def place_filter_at(pos):
    pos = element_wise(pos, [0, 0, -1])
    return place("sugar:orange_filter", element_wise(game_corner, pos))
white = 'white'
def place_cup_at(pos_x, pos_y, color=white, upside_down=False):
    structure_name = "cup"
    if color != white:
        structure_name = f"{color}_{structure_name}"
    if upside_down:
        structure_name = "upside_down_" + structure_name
    structure_name = f"sugar:{structure_name}"
    return place(structure_name, element_wise(game_corner, (pos_x, pos_y, -2)))


levels_holder = OutputFile("levels_holder", folder="levels")
# for i in range(5):
board_center = get_center(game_corner, high_corner)
cur_level = levels_holder.add_variant(0)
cur_level.extend(
    set_score(sugar_for_current_level_score, 300),
    place_cup_at(15, 5)
)
cur_level = levels_holder.add_variant(1)
cur_level.extend(
    set_score(sugar_for_current_level_score, 300),
    place_cup_at(10, 5),
    place_cup_at(30, 5)
)

cur_level = levels_holder.add_variant(2)
cur_level.extend(
    set_score(sugar_for_current_level_score, 300),
    place_cup_at(30, 25),
    place_cup_at(5, game_height - 8, upside_down=True)
)

board_center_from_corner = element_wise(board_center, game_corner, op.sub)
cur_level = levels_holder.add_variant()
cur_level.extend(
    set_score(sugar_for_current_level_score, 300),
    place_cup_at(30, 5, 'white'),
    place_filter_at(element_wise(board_center_from_corner, [-8, 0, 0])),
    place_cup_at(5, 5, 'orange')
)

cur_level = levels_holder.add_variant()
cur_level.extend(
    set_score(sugar_for_current_level_score, 700),
    list_chain(
            place_cup_at(x, 25) + place_cup_at(x, 15, upside_down=True)
            for x in range(10, 35, 10)
    )
)

cur_level = levels_holder.add_variant()
cur_level.extend(
    set_score(sugar_for_current_level_score, 1),
    list_chain(
            place_cup_at(x, 25) + place_cup_at(x, 15, upside_down=True)
            for x in range(10, 35, 10)
    )
)

current_level_num = create_scoreboard("current_level_num")
place_level_contents = OutputFile("place_level_contents",
    list_chain(execute_if_score_equals(current_level_num, i, 
        call_function(levels_holder.get_variant(i))
    )
    for i in range(len(levels_holder.variants)))
)

place_white_cup = OutputFile("place_white_cup")
place_white_cup.extend(
    place("sugar:cup", element_wise(game_corner, (5, 5, -2))) + 
    set_score(sugar_needed_in_cup_score, 100, at_e(tag=cup_counter_tag))
)

place_orange_cup = OutputFile("place_orange_cup")
place_orange_cup.extend(
    place("sugar:copper_cup", element_wise(game_corner, (15, 5, -2))) + 
    set_score(sugar_needed_in_cup_score, 100, at_e(tag=cup_counter_tag))
)

place_title = OutputFile("place_title")
place_title.extend(
    execute_at(element_wise(middle_top_of_board, (0,1,-2)),
        raw('''execute summon text_display run data merge entity @s {billboard:"fixed",Rotation:[-180F,0F],transformation:{scale:[16f,16f,16f]},text:'{"text":"Sugar, Sugar"}'}''')
    )
)

cup_update = OutputFile("cup_update", is_update_file=True)
cup_update.extend(
    raw('''execute as @e[type=minecraft:text_display,tag=cup_text] run data merge entity @s {text:'{"score":{"name":"@e[tag=cup_counter,sort=nearest,limit=1]","objective":"sugar_needed_in_cup"}}'}''') +
    set_to_max(sugar_needed_in_cup_score, 0, at_e(tag=cup_counter_tag))
)

# place_filter = OutputFile("place_filter")
# place_filter.extend(
# )
place_random_deciders = OutputFile("place_random_deciders",
    summon_marker(game_corner, tag=random_decider_tag),
    summon_marker(game_corner, tag=random_decider_tag)
)
reset_level = OutputFile("reset_level")
reset_level.extend(
    call_function(remove_all_sugar),
    kill(at_e(type='!player')),
    call_function(place_random_deciders),
    call_function(place_wall),
    call_function(place_title),
    call_function(reset_scores),
    call_function(place_level_contents),
    # call_function(place_white_cup),
    # call_function(place_orange_cup),
    # call_function(place_filter),
    set_score(sugar_needed_in_cup_score, 100, at_e(tag=cup_counter_tag)),
    clear_scheduled_functions()
)

remaining_sugar_required_to_progress_score = create_scoreboard("remaining_sugar_required_to_progress", 0)

check_level_complete = OutputFile("check_level_complete", is_update_file=True)
check_level_complete.extend(
    execute_positioned(board_center, 
        set_score_to_total_of_other_scores(remaining_sugar_required_to_progress_score, sugar_needed_in_cup_score, at_e(tag=cup_counter_tag, distance='..30'))
    ),
    execute_if_score_equals(remaining_sugar_required_to_progress_score, 0,
        increment(current_level_num) +
        call_function(reset_level)
    )
)

end_of_tick_code.extend(
    operation(spawn_sugar_cooldown_score, '-=', 1),
    operation(spawn_sugar_cooldown_score, '>', 0)
)