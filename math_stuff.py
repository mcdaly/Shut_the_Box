# Calculating random math things

def total_addends(total, tiles, prev_tile):
    # Only care about addends still in tiles list
    final_addends = []
    row = 0
    # Trim tiles down to all tiles below the total or below the previous tile
    if prev_tile == 0 or total < prev_tile:
        trimmed_tiles = [x for x in tiles if x <= total]
    else:
        trimmed_tiles = [x for x in tiles if x < prev_tile]

    for tile in reversed(trimmed_tiles):
        total_to_reach = total - tile
        # Determine if current tile matches total and no other combos need to be found
        if total_to_reach == 0:
            final_addends.insert(row, [tile])
            row += 1
        elif total_to_reach <= tile:
            # Need to recursively find tiles that can add up to remainder
            returned_addends = total_addends(total_to_reach, trimmed_tiles, tile)
            if returned_addends:
                # if prev_tile:
                #     for found_addends in returned_addends:
                #         final_addends.insert(row, [tile])
                #         final_addends[row].extend(found_addends)
                #
                #         row += 1
                # else:
                for found_addends in returned_addends:
                    final_addends.insert(row, [tile])
                    if isinstance(found_addends, int):
                        final_addends[row].extend([found_addends])
                    else:
                        final_addends[row].extend(found_addends)
                    row += 1
    return final_addends
