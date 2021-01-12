#!/usr/bin/env pyton 3

# Created by Larry nkengbeza
# Created on December 2020
# This is program is the space aliens program on the pybadge
import random
import ugame
import stage
import constants
import time

def splash_scene():
    # this function is the splash scene
    
    # get sound ready
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)
    
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    
    # sets background to image 0 in image Bank
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_X,
                            constants.SCREEN_Y)
  # used this program to split the image into tile: 
    #   https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white
    
    # create a stage for the background to show up on
    #   and set frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers, items show up in order
    game.layers = [background]
    # render the background and initial location of sprite list
    # most likely you will only render backgorund once per scene
    game.render_block()
    
    # repeat forever, game loop
    while True:
        # wait 2 seconds
        time.sleep(2.0)
        menu_scene()

def menu_scene():
    # this function is the menu scene
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # add text objects
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT GAME STUDIOS")
    text.append(text1)
    
    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)
    # sets background to image 0 in image Bank
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_X,
                            constants.SCREEN_Y)
    # create a stage for the background to show up on
    #   and set frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and initial location of sprite list
    # most likely you will only render backgorund once per scene
    game.render_block()
    
    # repeat forever, game loop
    while True:
        # get user input
        keys  = ugame.buttons.get_pressed()
        
        # start button selected
        if keys and ugame.K_START != 0:
            menu_scene()
            
        # update game logic
        game.tick() # wait till refresh rate finishes
def game_scene():
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    # sets the background to image 0 in the image Bank
    # and the size (10x8 tiles of size 16x16)
    #buttons that you want to keep state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]
    # get sound ready
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop
    sound.mute(False)
    background = stage.Grid(image_bank_background, constants.SCREEN_X,
                            constants.SCREEN_Y)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(1, 3)
            background.tile(x_location, y_location, tile_picked)
    
    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))
    
    alien = stage.Sprite(image_bank_sprites, 9,
                     int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
                     16)
    lasers = []
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.Sprite(image_bank_sprites, 10,
                                      constants.OFF_SCREEN_X,
                                      constants.OFF_SCREEN_Y)
        lasers.append(a_single_laser)
    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers, items show up in order
    game.layers = lasers + ([ship] + [alien]) + [background]
    # render the background and initial location of sprite list
    # most likely you will render background once per scene
    game.render_block()
    # repeat forever, or you turn it off!
    while True:
        # will get user input
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_O != 0:
             if a_button == constants.button_state["button_up"]:
                 a_button = constants.button_state["button_just_pressed"]
             elif a_button == constants.button_state["button_just_pressed"]:
                 a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button  == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
        # B button
        if keys & ugame.K_X != 0:
            pass
        if keys & ugame.K_START != 0:
            print("Start")
        if keys & ugame.K_SELECT != 0:
            print("Select")
        if keys & ugame.K_RIGHT != 0:
            if ship.x < (constants.SCREEN_X- constants.SPRITE_SIZE):
                ship.move((ship.x + constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move((constants.SCREEN_X - constants.SPRITE_SIZE), ship.y)
        if keys & ugame.K_LEFT != 0:
            if ship.x > 0:
                ship.move((ship.x - constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_UP != 0:
            pass
        if keys & ugame.K_DOWN != 0:
            pass
        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_RIGHT:
            if ship.x <= constants.SCREEN_X:
                ship.move(ship.x +1, ship.y)
            else:
                ship.move(constants.SCREEN_X, ship.y)
        if keys & ugame.K_LEFT:
            if ship.x >= 0:
                ship.move(ship.x -1, ship.y)
            else:
                ship.move(0, ship.y)

        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass
        if a_button == constants.button_state["button_just_pressed"]:
            for laser_number in range(len(lasers)):
                if lasers [laser_number].x < 0:
                    lasers[laser_number].move(ship.x, ship.y)
                    sound.play(pew_sound)
                    break
        # each frame move the lasers that have been fired
        for laser_number in rang(len(lasers)):
            if lasers[laser_number].x > 0:
                lasers [laser_number].move(lasers[laser_number].x,
                                           lasers[laser_number].y -
                                             constants.LASER_SPEED)
                if lasers [laser_number].y < constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(constants.OFF_SCREEN_X,
                                              constants.OFF_SCREEN_Y)
        # update game logic
        # redraw Sprites
        game.render_sprites(lasers + [ship] + [alien])
        game.tick()
if __name__ == "__main__":
    splash_scene()
