
class SlidingPuzzle:
    def __init__(self):
        # self.puzzle_horizontal = [
        #     [1,8,2],
        #     [4,3,5],
        #     [7,6,0],
        # ]

        self.puzzle_horizontal = [
            [1,2,3],
            [4,5,6],
            [7,0,8],
        ]
        '''
        Easy testing for win condition.
        Replace self.puzzle_horizontal with this one and you have to move only one piece
            self.puzzle_horizontal = [
            [1,2,3],
            [4,5,6],
            [7,8,0],
        ]
        '''

        self.puzzle_vertical = [
            [1,2,3],
            [4,5,6],
            [7,0,8],
        ]
        self.winning_puzzle = [
            [1,2,3],
            [4,5,6],
            [7,8,0],
        ]
        self.score = 0
        self.number_of_moves_per_game = []
        self.moves = 0
        self.user_input_and_choices()

    def print_puzzle(self):
        for item in self.puzzle_horizontal:
            print(item)

    def user_input_and_choices(self):
        self.print_puzzle()
        self.check_if_user_has_won()
        piece_to_be_moved = int(input(f'Please chose which puzzle piece you want to move by typing the number of it: '))
        try:
            if piece_to_be_moved < 1 or piece_to_be_moved > 15:
                self.user_input_and_choices()
        except Exception as e:
            print(e)
        if self.is_valid_move(piece_to_be_moved, self.puzzle_horizontal):
            self.moves = self.moves+1
            self.swap_places_horizontal(piece_to_be_moved)
            self.swap_places_vertical(piece_to_be_moved)
            self.user_input_and_choices()
        if self.is_valid_move(piece_to_be_moved, self.puzzle_vertical):
            self.moves = self.moves+1
            self.swap_places_horizontal(piece_to_be_moved)
            self.swap_places_vertical(piece_to_be_moved)
            self.user_input_and_choices()
        else:
            self.user_input_and_choices()

    def check_if_user_has_won(self):
        if self.puzzle_horizontal == self.winning_puzzle:
            self.score = self.score +1
            self.number_of_moves_per_game.append(self.moves)
            print(self.number_of_moves_per_game)
            self.moves=0
            self.puzzle_horizontal = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 0, 8],
            ]
            self.puzzle_vertical = [
            [1,4,7],
            [2,5,0],
            [3,6,8],
            ]
            print(self.number_of_moves_per_game)
            if self.score == 3:
                print('You won the Game!')
                exit()
            else:
                print('You won one point!')
                print('Play another Round')
                self.print_puzzle()


    def is_valid_move(self, piece, puzzle):
        for nested_list in puzzle:
            if piece in nested_list and 0 in nested_list:
                if (nested_list.index(0) - nested_list.index(piece)) == 1 or (nested_list.index(0) - nested_list.index(piece)) == -1:
                    return True
                else:
                    return False
        return False

    def swap_places_horizontal(self, piece):
        count = False
        for outer_index, nested_list in enumerate(self.puzzle_horizontal):
            for inner_index, number in enumerate(nested_list):
                if count:
                    break
                elif number == piece:
                    self.replace_null_horizontal(piece)
                    self.puzzle_horizontal[outer_index][inner_index] = 0
                    count=True
                    break

    def replace_null_horizontal(self, piece):
        for outer_index, nested_list in enumerate(self.puzzle_horizontal):
            for inner_index, number in enumerate(nested_list):
                if number == 0:
                    self.puzzle_horizontal[outer_index][inner_index] = piece
                    break

    def swap_places_vertical(self, piece):
        count = False
        for outer_index, nested_list in enumerate(self.puzzle_vertical):
            for inner_index, number in enumerate(nested_list):
                if count:
                    break
                elif number == piece:
                    self.replace_null_vertical(piece)
                    self.puzzle_vertical[outer_index][inner_index] = 0
                    count=True
                    break

    def replace_null_vertical(self, piece):
        for outer_index, nested_list in enumerate(self.puzzle_vertical):
            for inner_index, number in enumerate(nested_list):
                if number == 0:
                    self.puzzle_vertical[outer_index][inner_index] = piece
                    break

puzzle = SlidingPuzzle()
