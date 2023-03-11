scoreboard players operation @e[tag=cup_counter,limit=1,distance=..4,sort=nearest] sugar_needed_in_cup -= const1 const
scoreboard players operation @e[tag=cup_counter,limit=1,distance=..4,sort=nearest] sugar_needed_in_cup > const0 const
setblock ~ ~ ~ air replace
kill @s
