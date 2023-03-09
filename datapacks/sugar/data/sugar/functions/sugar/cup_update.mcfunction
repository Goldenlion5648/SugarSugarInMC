execute as @e[type=minecraft:text_display,tag=cup_text] run data merge entity @s {text:'{"score":{"name":"@e[tag=cup_counter,sort=nearest,limit=1]","objective":"sugar_needed_in_cup"}}'}
scoreboard players operation @e[tag=cup_counter] sugar_needed_in_cup > const0 const
