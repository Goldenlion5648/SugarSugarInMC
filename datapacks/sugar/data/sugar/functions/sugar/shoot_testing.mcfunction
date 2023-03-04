summon marker 0 0 0 {Tags:["not_adjusted", "step_size1", "paint_brush"]}
tp @e[tag=not_adjusted] @s
execute as @e[tag=not_adjusted] at @s run tp @s ~ ~1 ~
tag @e[tag=not_adjusted] remove not_adjusted
