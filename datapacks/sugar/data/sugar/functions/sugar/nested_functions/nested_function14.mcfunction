execute as @e[tag=sugar,tag=has_not_moved,sort=furthest] at @s run function sugar:sugar/nested_functions/nested_function4
execute as @e[tag=sugar,tag=has_not_moved,sort=furthest] at @s run execute if block ~0 ~-1 ~ air run execute if block ~0 ~-1 ~ air run tag @s add should_move
execute as @e[tag=should_move,sort=furthest] at @s run function sugar:sugar/nested_functions/nested_function5
execute as @e[tag=sugar,tag=has_not_moved,sort=furthest] at @s run function sugar:sugar/nested_functions/nested_function8
execute as @e[tag=sugar,tag=has_not_moved,sort=furthest] at @s run execute if block ~-1 ~0 ~ air run execute if block ~-1 ~-1 ~ air run tag @s add should_move
execute as @e[tag=should_move,sort=furthest] at @s run function sugar:sugar/nested_functions/nested_function9
execute as @e[tag=sugar,tag=has_not_moved,sort=furthest] at @s run function sugar:sugar/nested_functions/nested_function12
execute as @e[tag=sugar,tag=has_not_moved,sort=furthest] at @s run execute if block ~1 ~0 ~ air run execute if block ~1 ~-1 ~ air run tag @s add should_move
execute as @e[tag=should_move,sort=furthest] at @s run function sugar:sugar/nested_functions/nested_function13
