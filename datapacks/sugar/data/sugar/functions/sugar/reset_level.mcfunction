function sugar:sugar/remove_all_sugar
kill @e[type=!player]
function sugar:sugar/place_wall
function sugar:sugar/place_title
function sugar:sugar/reset_scores
function sugar:sugar/place_level_contents
scoreboard players set @e[tag=cup_counter] sugar_needed_in_cup 100
schedule clear sugar:sugar/delayed_code/delayed_code_id1
schedule clear sugar:sugar/delayed_code/delayed_code_id2
