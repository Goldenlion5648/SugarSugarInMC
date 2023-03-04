execute as @e[tag=sugar] at @s run tag @s add has_not_moved
execute as @e[tag=sugar,tag=has_not_moved] at @s run execute if block ~0 ~0.4875 ~ air run tag @s add should_move
execute as @e[tag=should_move] at @s run setblock ~ ~2 ~ air replace
execute as @e[tag=should_move] at @s run tp @s ~0 ~-1 ~
execute as @e[tag=should_move] at @s run setblock ~ ~2 ~ white_concrete replace
execute as @e[tag=should_move] at @s run tag @s remove has_not_moved
execute as @e[tag=should_move] at @s run tag @s remove should_move
execute as @e[tag=sugar,tag=has_not_moved] at @s run execute if block ~-1 ~0.4875 ~ air run tag @s add should_move
execute as @e[tag=should_move] at @s run setblock ~ ~2 ~ air replace
execute as @e[tag=should_move] at @s run tp @s ~-1 ~-1 ~
execute as @e[tag=should_move] at @s run setblock ~ ~2 ~ white_concrete replace
execute as @e[tag=should_move] at @s run tag @s remove has_not_moved
execute as @e[tag=should_move] at @s run tag @s remove should_move
execute as @e[tag=sugar,tag=has_not_moved] at @s run execute if block ~1 ~0.4875 ~ air run tag @s add should_move
execute as @e[tag=should_move] at @s run setblock ~ ~2 ~ air replace
execute as @e[tag=should_move] at @s run tp @s ~1 ~-1 ~
execute as @e[tag=should_move] at @s run setblock ~ ~2 ~ white_concrete replace
execute as @e[tag=should_move] at @s run tag @s remove has_not_moved
execute as @e[tag=should_move] at @s run tag @s remove should_move
