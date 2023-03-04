execute as @a at @s run execute unless score @s is_painting = @s old_is_painting run function sugar:sugar/hacky_shoot_facing
execute as @a at @s run execute unless score @s is_painting = @s old_is_painting run scoreboard players operation @s old_is_painting = @s is_painting
