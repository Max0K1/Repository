 
# factory.py

class TetrisPiece:
    def draw(self):
        pass

class SquarePiece(TetrisPiece):
    def draw(self):
        return "Drawing a square piece"

class TPiece(TetrisPiece):
    def draw(self):
        return "Drawing a T piece"

class LPiece(TetrisPiece):
    def draw(self):
        return "Drawing an L piece"

class TetrisPieceFactory:
    def create_piece(self, piece_type):
        if piece_type == "square":
            return SquarePiece()
        elif piece_type == "t":
            return TPiece()
        elif piece_type == "l":
            return LPiece()
        else:
            raise ValueError("Invalid piece type")

if __name__ == "__main__":
    factory = TetrisPieceFactory()

    square_piece = factory.create_piece("square")
    t_piece = factory.create_piece("t")
    l_piece = factory.create_piece("l")

    print(square_piece.draw())
    print(t_piece.draw())
    print(l_piece.draw())