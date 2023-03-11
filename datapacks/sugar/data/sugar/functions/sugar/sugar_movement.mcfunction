execute if score global spawn_sugar_cooldown matches 0 run function sugar:sugar/nested_functions/nested_function28
execute as @e[tag=sugar] at @s run execute if block ~-1 ~ ~1 orange_wool run setblock ~ ~ ~ orange_concrete replace
execute as @e[tag=sugar] at @s run execute if block ~0 ~ ~1 orange_wool run setblock ~ ~ ~ orange_concrete replace
execute as @e[tag=sugar] at @s run execute if block ~1 ~ ~1 orange_wool run setblock ~ ~ ~ orange_concrete replace
