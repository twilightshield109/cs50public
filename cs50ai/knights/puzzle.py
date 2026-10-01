from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

KB = And(
    Or(AKnight,AKnave),
    Or(BKnight,BKnave),
    Or(CKnight,CKnave),
    Not(And(AKnight,AKnave)),
    Not(And(BKnight,BKnave)),
    Not(And(CKnight,CKnave))

)

# Puzzle 0
# A says "I am both a knight and a knave."
sentence0 = And(AKnight, AKnave)
knowledge0 = And(
    KB,
    Implication(AKnave, Not(sentence0)),
    Implication(AKnight, sentence0)
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
sentence1 = And(AKnave, BKnave)
knowledge1 = And(
    KB,
    Implication(AKnave, Not(sentence1)),
    Implication(AKnight, sentence1)
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
sentence2A = Or(And(AKnight,BKnight), And(AKnave,BKnave))
sentence2B = Or(And(AKnight,BKnave), And(AKnave,BKnight))
knowledge2 = And(
    KB,
    Implication(AKnight,sentence2A),
    Implication(AKnave, Not(sentence2A)),
    Implication(BKnight, sentence2B),
    Implication(BKnave, Not(sentence2B))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
sentence3A = Or(And(AKnight, Not(AKnave)),And(Not(AKnight), AKnave))
sentence3B1 = And(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave)))
sentence3B2 = CKnave
sentence3C = AKnight

knowledge3 = And(
    KB,
    Implication(AKnight,sentence3A),
    Implication(AKnave, Not(sentence3A)),
    Implication(BKnight, sentence3B1),
    Implication(BKnight, sentence3B2),
    Implication(BKnave, Not(sentence3B2)),
    Implication(BKnave, Not(sentence3B2)),
    Implication(CKnight,sentence3C),
    Implication(CKnave, Not(sentence3C))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
