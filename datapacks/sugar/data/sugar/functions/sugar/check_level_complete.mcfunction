execute positioned 125 27 100 run scoreboard players set global remaining_sugar_required_to_progress 0
execute positioned 125 27 100 run scoreboard players operation global remaining_sugar_required_to_progress += @e[tag=cup_counter,distance=..30] sugar_needed_in_cup
execute if score global remaining_sugar_required_to_progress matches 0 run function sugar:sugar/nested_functions/nested_function30
