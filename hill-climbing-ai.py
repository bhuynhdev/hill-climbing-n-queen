import re
import random
from dataclasses import dataclass, field
from typing import Tuple, List, NamedTuple, Optional

# Classes to organize data
class Position(NamedTuple):
  row: int
  column: int

@dataclass
class State:
    # Total conflicts of this state
    conflict_count: int
    # Positions of all queens on the board
    positions: Tuple[Position]
    # id/index of the queen that just moved to get to this state, will help to determine conflict_count more effectively
    queen_who_just_moved: int
    # Dict to quickly check if a queen is on a certain position
    is_queen: dict[Position, int] = field(repr=False)

# %%
# Process inputs

def convert_string_to_Position(s):
  """
  Accept string in format of "1, 2" and convert to tuples of int
  """
  return Position(*[int(n.strip()) for n in s.split(",")])

inp = "10 6 (1, 7), (2, 4), (2, 5), (3, 8), (4, 1), (4,6), (5, 5), (6, 2), (7,2),(8,3)"

q_count, reach, positions_input = inp.split(" ", 2)
q_count = int(q_count.strip())
reach = int(reach.strip())

# Use regular expression to capture content inside parentheses
pattern = re.compile(r"\((.*?)\)")
position_strings = re.findall(pattern, positions_input.strip()) # array of strings like this ['1, 2', '2, 3', '5, 6']
POSITIONS = tuple(convert_string_to_Position(s) for s in position_strings)

# %%
# Assuming the board's numbering is like a Catersian Coordinate plane:
# x (column) increases from left to right, y (row) increases from bottom to top
UP = (1, 0)
DOWN = (-1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)
# Generate all the directions since a queen can move up to 7 spaces on the board
DIRECTIONS = [
    *((UP[0] * i, UP[1]) for i in range (1, 8)),
    *((DOWN[0] * i, UP[1]) for i in range (1, 8)),
    *((RIGHT[0], RIGHT[1] * i) for i in range(1, 8)),
    *((LEFT[0], LEFT[1] * i) for i in range(1, 8))
]
REACH = reach

# Optimize: Prevent from going back to already examined states
# Since each state's position is a TUPLE, it is hashable
# So we maintain a set of visited state to remove redundant checks and loop back
VISTED = set()

# Core functions


def is_position_in_bound(position: Position):
    """
    Check that the position is not out of bound
    """
    return 1 <= position.row <= 8 and 1 <= position.column <= 8


def calculate_conflicts_of_single_queen(positions: Tuple[Position], queen_index: int, is_queen: dict[Position, int]) -> int:
    result_conflicts = 0
    curr_pos = positions[queen_index]

    # Horizontal checks
    # Horizontal pass 1: Advance to the right
    for i in range(1, REACH + 1):
        new_pos = Position(curr_pos.row + RIGHT[0], curr_pos.column + RIGHT[1]*i)
        if not is_position_in_bound(new_pos):
            break  # Have reached edge of board, should not advance any more
        if new_pos in is_queen:
            result_conflicts += 1

    # Horizontal pass 2: Advance to the left
    for i in range(1, REACH + 1):
        new_pos = Position(curr_pos.row + LEFT[0], curr_pos.column + LEFT[1]*i)
        if not is_position_in_bound(new_pos):
            break  # Have reached edge of board, should not advance any more
        if new_pos in is_queen:
            result_conflicts += 1

    # Vertical checks
    # Vertical pass 1: Advance upward
    for i in range(1, REACH + 1):
        new_pos = Position(curr_pos.row + UP[0]*i, curr_pos.column + UP[1])
        if not is_position_in_bound(new_pos):
            break  # Have reached edge of board, should not advance any more
        if new_pos in is_queen:
            result_conflicts += 1

    # Vertical pass 2: Advance downward
    for i in range(1, REACH + 1):
        new_pos = Position(curr_pos.row + DOWN[0]*i, curr_pos.column + DOWN[1])
        if not is_position_in_bound(new_pos):
            break  # Have reached edge of board, should not advance any more
        if new_pos in is_queen:
            result_conflicts += 1

    # Diagonal checks
    # Diagonal pass 1: Advance UpRight
    for i in range(1, REACH + 1):
        new_pos = Position(curr_pos.row + UP[0]*i, curr_pos.column + RIGHT[1]*i)
        if not is_position_in_bound(new_pos):
            break  # Have reached edge of board, should not advance any more
        if new_pos in is_queen:
            result_conflicts += 1

    # Diagonal pass 2: Advance UpLeft
    for i in range(1, REACH + 1):
        new_pos = Position(curr_pos.row + UP[0]*i, curr_pos.column + LEFT[1]*i)
        if not is_position_in_bound(new_pos):
            break  # Have reached edge of board, should not advance any more
        if new_pos in is_queen:
            result_conflicts += 1

    # Diagonal pass 3: Advance DownRight
    for i in range(1, REACH + 1):
        new_pos = Position(curr_pos.row + DOWN[0]*i, curr_pos.column + RIGHT[1]*i)
        if not is_position_in_bound(new_pos):
            break  # Have reached edge of board, should not advance any more
        if new_pos in is_queen:
            result_conflicts += 1

    # Diagonal pass 4: Advance DownLeft
    for i in range(1, REACH + 1):
        new_pos = Position(curr_pos.row + DOWN[0]*i, curr_pos.column + LEFT[1]*i)
        if not is_position_in_bound(new_pos):
            break  # Have reached edge of board, should not advance any more
        if new_pos in is_queen:
            result_conflicts += 1

    return result_conflicts


def count_new_conflicts(old_state: State,
                                 new_positions: List[Position],
                                 queen_who_just_moved: int,
                                 new_is_queen: dict[Position, int]) -> int:
    """
    Calculate current_state conflict count based on the prev_state's conflicts
    """
    # New_conflict_count = old_conflict_count
    #                      - old_conflict of queen_who_just_moved
    #                      + new_conflict of queen_who_just_moved
    # Credit: https://youtu.be/7fjmGWkv-sY?t=322
    old_queen_conflict = calculate_conflicts_of_single_queen(
        old_state.positions, queen_who_just_moved, old_state.is_queen)
    new_queen_conflict = calculate_conflicts_of_single_queen(
        new_positions, queen_who_just_moved, new_is_queen)

    result = old_state.conflict_count - old_queen_conflict + new_queen_conflict
    return result


def generate_neighbor_states(current_state: State) -> List[State]:
    old_positions = current_state.positions
    neighbor_states: List[State] = []
    # For each current queen position, move that queen horizontally or vertically
    VISTED.add(old_positions)
    for index, old_position in enumerate(old_positions):
        for direction in DIRECTIONS:
            new_r, new_c = old_position.row + direction[0], old_position.column + direction[1]
            new_pos = Position(new_r, new_c)
            if is_position_in_bound(new_pos) and new_pos not in current_state.is_queen:
                # Create new_positions based on old_positions, and just changing the single position that changed
                new_positions = old_positions[0:index] + (new_pos,) + old_positions[index + 1:]
                if new_positions in VISTED:
                    continue
                # Efficiently calcualte the new is_queen
                new_is_queen = current_state.is_queen.copy()
                new_is_queen[new_pos] = index
                new_is_queen.pop(old_position, None)
                # Create neighbor state
                new_state = State(
                    queen_who_just_moved=index,
                    positions=new_positions,
                    conflict_count=count_new_conflicts(
                        current_state, new_positions, index, new_is_queen),
                    is_queen=new_is_queen
                )
                neighbor_states.append(new_state)

    return neighbor_states


def choose_best_neighbor_states(neighbor_states: List[State], current_conflict_count: int) -> Optional[State]:
    best_states = []
    min_conflict = 999
    for state in neighbor_states:
        if state.conflict_count < min_conflict:
            best_states = [state]
            min_conflict = state.conflict_count
        elif state.conflict_count == min_conflict:
            best_states.append(state)
        
    return random.choice(best_states) if len(best_states) > 0 else None


# %%
def create_initial_state(positions: List[Position]) -> State:
  initial_conflict_count = 0
    # Create a dict to quickly check if a queen is on a certain position
  is_queen: dict[Position, int] = {}
  for queen_index, queen_position in enumerate(positions):
      is_queen[queen_position] = queen_index

  for queen_index in range(len(positions)):
    # Sum the conflict of each queen
    initial_conflict_count += calculate_conflicts_of_single_queen(
        positions, queen_index, is_queen=is_queen)

  # Since each conflict was counted twice, divide by 2 to get true number of conflicts
  initial_conflict_count = initial_conflict_count // 2

  return State(queen_who_just_moved=0, conflict_count=initial_conflict_count, positions=positions, is_queen=is_queen)


def hill_climbing(start_positions: Tuple[Position]):
  curr_state = create_initial_state(start_positions)
  print("Init state", curr_state)
  neightbor_state_count = 0
  MAX_TRANSITIONS = 9999  # Max 60 steps
  for step in range(MAX_TRANSITIONS):
    if curr_state.conflict_count == 0:
      print(f"Found solution in {step} steps")
      print(f"{neightbor_state_count} neighbor states were examined")
      return curr_state

    neighbors = generate_neighbor_states(curr_state)
    neightbor_state_count += len(neighbors)
    best_next_state = choose_best_neighbor_states(neighbors, curr_state.conflict_count)
    print("Chose neighbor", best_next_state)
    if not best_next_state:
      print(f"{neightbor_state_count} neighbor states were examined")
      print(f"Local Minimum is reached at step {step}; all neighbor states are worse than current")
      return curr_state
    curr_state = best_next_state
  
  print(f"{MAX_TRANSITIONS} transitions occured; no solution found")
  print(f"{neightbor_state_count} neighbor states were examined")

  return curr_state

hill_climbing(POSITIONS)


