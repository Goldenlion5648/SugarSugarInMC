execute as @e[tag=paint_brush] at @s run execute if block ~ ~ ~ red_concrete run setblock ^ ^ ^-1 light_blue_concrete replace
execute as @e[tag=paint_brush] at @s run execute if block ~ ~ ~ red_concrete run kill @s
