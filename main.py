def on_overlap_tile(sprite, location):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player, myTiles.tile2, on_overlap_tile)

def on_overlap_tile2(sprite, location):
    game.over(True)
scene.on_overlap_tile(SpriteKind.player, myTiles.tile4, on_overlap_tile2)

def on_a_pressed():
    thePlayer.vy = -200
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    otherSprite.destroy()
    if sprite.bottom < otherSprite.y:
        sprite.vy = -100
    else:
        info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

newEnemy: Sprite = None
thePlayer: Sprite = None
scene.set_background_color(11)
thePlayer = sprites.create(img("""
    3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
    3 1 1 1 1 1 1 1 1 1 1 1 1 1 1 3
    3 1 3 3 3 3 3 3 3 3 3 3 3 3 1 3
    3 1 3 3 3 3 3 3 3 3 3 3 3 3 1 3
    3 1 3 3 3 3 3 3 3 3 3 3 3 3 1 3
    3 1 3 3 1 1 1 3 3 3 1 3 3 3 1 3
    3 1 3 3 1 3 3 1 3 1 1 3 3 3 1 3
    3 1 3 3 1 3 3 1 3 3 1 3 3 3 1 3
    3 1 3 3 1 1 1 3 3 3 1 3 3 3 1 3
    3 1 3 3 1 3 3 3 3 3 1 3 3 3 1 3
    3 1 3 3 1 3 3 3 3 1 1 1 3 3 1 3
    3 1 3 3 3 3 3 3 3 3 3 3 3 3 1 3
    3 1 3 3 3 3 3 3 3 3 3 3 3 3 1 3
    3 1 3 3 3 3 3 3 3 3 3 3 3 3 1 3
    3 1 1 1 1 1 1 1 1 1 1 1 1 1 1 3
    3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
"""),
    SpriteKind.player)
thePlayer.ay = 500
controller.move_sprite(thePlayer, 100, 0)
tiles.set_tilemap(tilemap("""
    level
"""))
scene.camera_follow_sprite(thePlayer)
tiles.place_on_random_tile(thePlayer, myTiles.tile3)
info.set_life(3)
for value in tiles.get_tiles_by_type(myTiles.tile5):
    newEnemy = sprites.create(img("""
            . . . . . . b b b b . . . . . . 
                    . . . . . . b 4 4 4 b . . . . . 
                    . . . . . . b b 4 4 4 b . . . . 
                    . . . . . b 4 b b b 4 4 b . . . 
                    . . . . b d 5 5 5 4 b 4 4 b . . 
                    . . . . b 3 2 3 5 5 4 e 4 4 b . 
                    . . . b d 2 2 2 5 7 5 4 e 4 4 e 
                    . . . b 5 3 2 3 5 5 5 5 e e e e 
                    . . b d 7 5 5 5 3 2 3 5 5 e e e 
                    . . b 5 5 5 5 5 2 2 2 5 5 d e e 
                    . b 3 2 3 5 7 5 3 2 3 5 d d e 4 
                    . b 2 2 2 5 5 5 5 5 5 d d e 4 . 
                    b d 3 2 d 5 5 5 d d d 4 4 . . . 
                    b 5 5 5 5 d d 4 4 4 4 . . . . . 
                    4 d d d 4 4 4 . . . . . . . . . 
                    4 4 4 4 . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    tiles.place_on_tile(newEnemy, value)
    newEnemy.follow(thePlayer, 30)