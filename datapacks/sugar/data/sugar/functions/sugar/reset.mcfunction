say Reload has completed
scoreboard objectives add const dummy
scoreboard objectives add remainder dummy
scoreboard players set const0 const 0
scoreboard players set const1 const 1
scoreboard players set const2 const 2
scoreboard players set const3 const 3
scoreboard players set const4 const 4
scoreboard players set const5 const 5
scoreboard players set const6 const 6
scoreboard players set const7 const 7
scoreboard players set const8 const 8
scoreboard players set const9 const 9
scoreboard players set const10 const 10
scoreboard players set const11 const 11
scoreboard players set const12 const 12
scoreboard players set const13 const 13
scoreboard players set const14 const 14
scoreboard players set const15 const 15
scoreboard objectives add sugar_in_cup dummy
scoreboard objectives add old_is_painting dummy
scoreboard players set @s old_is_painting 0
scoreboard objectives add is_painting dummy
scoreboard objectives add sugar_needed_in_cup dummy
scoreboard players set @e[tag=cup_counter,limit=1,distance=..4,sort=nearest] sugar_needed_in_cup 0
scoreboard objectives add gravity_direction_is_down dummy
scoreboard objectives add spawn_sugar_cooldown dummy
scoreboard objectives add remaining_sugar_to_dispense dummy
scoreboard players set global remaining_sugar_to_dispense 30
scoreboard players set global remaining_sugar_to_dispense 0
scoreboard objectives add current_level_num dummy
scoreboard players set global current_level_num 0
scoreboard players set @e[tag=cup_counter] sugar_needed_in_cup 0
scoreboard players set global spawn_sugar_cooldown 0
