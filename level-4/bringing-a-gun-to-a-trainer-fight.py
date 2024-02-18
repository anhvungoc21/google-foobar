from math import ceil, atan2

def solution(dimensions, your_position, trainer_position, distance):
    player_x, player_y = your_position

    # Determine hits on all possible reflections
    hits = {}
    for reflection in get_reflections(dimensions, your_position, trainer_position, distance):
        x, y, is_guard = reflection
        
        # Distance that shot travels
        travel = (abs(x - player_x) ** 2 + abs(y - player_y) ** 2) ** 0.5
        
        # Direction/Angle at which shot travels
        bearing = atan2(player_x - x, player_y - y)

        # Ignore hits which have insufficient distance
        if (travel > distance) or (bearing in hits and travel > abs(hits[bearing])):
            continue
            
        # Mark hits by seen angle
        hits[bearing] = travel * (-1 if is_guard == 0 else 1)

    return len([1 for travel in hits.values() if travel > 0])

# Generates all possible and reachable directions of both player and guard
def get_reflections(room_dims, player, guard, distance):
    # Unpack coordinates
    room_x, room_y = room_dims
    player_x, player_y = player

    # Generate reflections...
    new_coords = []
    
    # (1) In all 4 quadrants...
    for quadrant in [(1, 1), (-1, 1), (-1, -1), (1, -1)]:
        quad_x, quad_y = quadrant

        #  (2) In the x-direction...
        for x_mult in range(1, int(ceil(float(player_x + distance) / room_x)) + 1):

            # (3) In the y-direction...
            for y_mult in range(1, int(ceil(float(player_y + distance) / room_y)) + 1):

                # (4) For both entities.
                for is_guard, entity in enumerate([player, guard]):
                    entity_x, entity_y = entity

                    new_coords.append([
                        get_reflected_coord(room_x, entity_x, x_mult, quad_x),
                        get_reflected_coord(room_y, entity_y, y_mult, quad_y),
                        is_guard
                    ])

    return new_coords


# Gets a reflection of a coordinate
def get_reflected_coord(room_dim, entity_dim, reflect_mult, quadrant_mult):
    even_reflection = room_dim * reflect_mult - entity_dim
    odd_reflection = room_dim * reflect_mult - (room_dim - entity_dim)
    return (even_reflection if (reflect_mult % 2 == 0) else odd_reflection) * quadrant_mult

print(solution([3,2], [1,1], [2,1], 4))
