import itertools as it
import os
import sys
sys.path.insert(0, r'C:\Users\cobou\Documents\Curse\Minecraft\Instances\CommandCreations1_19_2\python_helpers')
from helper_functions import *
import helper_functions
setup = OutputFile("setup")
helper_update = OutputFile("update")
helper_functions.UPDATE_JSON_FILE = f"{os.path.dirname(__file__)}\\..\\..\\..\\minecraft\\tags\\functions\\tick.json"

class Tags(Enum):
    # CARD_OUTLINE_TAG = "card_outline"

    def __str__(self):
        return str(self.value)
    
game_corner = (100, 0, 100)
wall_dims = (50, 50, 0)
offset_corner = (50, 50, -3)
background_block = "red_concrete"
painting_block = "light_blue_concrete"
platform_block = "stone"

platform_center = (125, 24, 65)

place_wall = OutputFile("place_wall")
place_wall.extend(
    fill(element_wise(game_corner, offset_corner), game_corner, "air") +
    fill(game_corner, element_wise(wall_dims, game_corner), background_block)
)


place_sugar = OutputFile("place_sugar")

# place_sugar.extend(
#     execute_as_at(at_a(), anchored_eyes=True,to_run=
#         execute_if_block_matches("~ ~-2 ~", platform_block,
#             execute_if_block_matches("^ ^ ^", platform_block,

#             )
#         )
#     )
# )

paint_brush_tag = "paint_brush"
shoot_testing = OutputFile("shoot_testing")
shoot_testing.extend(
    shoot_facing(moving_entity='marker', bullet_label_tag=paint_brush_tag, step=1, code_to_run_after_step=
        execute_if_block_matches("~ ~ ~", background_block,
            setblock("^ ^ ^-1", painting_block, mode="keep") +
            kill(at_s())
        ), repeats_per_tick=100
    )
)

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
hacky_shoot_facing.extend(
    it.chain.from_iterable(
        execute_at(f"^ ^ ^{offset}",
            execute_if_block_matches("^ ^ ^", background_block,
                setblock("^ ^ ^-1", painting_block, mode='keep') +
                setblock("^ ^1 ^-1", painting_block, mode='keep') +
                setblock("^ ^-1 ^-1", painting_block, mode='keep') +
                setblock("^1 ^ ^-1", painting_block, mode='keep') +
                setblock("^-1 ^ ^-1", painting_block, mode='keep')
            ), anchored_eyes=True
        ) for offset in range(1, 70)
    )
)

#  execute_if_score_other_score(score1 : str, op: str, score2: str, to_run : list, owner1: str=GLOBAL_VAR_HOLDER, owner2: str=GLOBAL_VAR_HOLDER, if_or_unless='if'):

is_painting_score = "is_painting"
old_is_painting_score = "old_is_painting"
create_scoreboard(old_is_painting_score, -1, at_a())

activate_painting = OutputFile("activate_painting", is_update_file=True)
activate_painting.extend(
    execute_as_at(at_a(),
        execute_unless_score_equals_score(is_painting_score, old_is_painting_score, owner1=at_s(), owner2=at_s(), to_run=
            call_function(hacky_shoot_facing) + 
            operation(old_is_painting_score, '=', is_painting_score, at_s(), at_s())
        )
    )
)