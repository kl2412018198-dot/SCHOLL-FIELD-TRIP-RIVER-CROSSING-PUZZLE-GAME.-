def check_rules(game):
    if game.studentA.side == game.supplies.side and game.teacher.side != game.studentA.side:
        game.game_over = True

    if all(c.side=="right" for c in game.characters):
        game.win=True