def game_loop():
    while True:
        global dragon
        dragon = Dragon() #call class
        flames = Flames()
        mario = Mario()
        add_new_flame_counter = 0 #intial value of counter
        global SCORE
        SCORE = 0
        global HIGH_SCORE
        flames_list = []

        while True:
            canvas.fill(BLACK)
            check_level(SCORE)
            dragon.update()
            add_new_flame_counter += 1 #update flame counter

            if add_new_flame_counter == ADD_NEW_FLAME_RATE: #check previous
                add_new_flame_counter = 0
                new_flame = Flames()
                flames_list.append(new_flame) #update flamelist
            for f in flames_list:
                if f.flames_img_rect.left <= 0: #check it hits mario or pass
                    flames_list.remove(f)     #remove this flame from flame array
                    SCORE += 1 #add score
                f.update()

                for event in pygame.event.get(): #builtin function to check leaving game
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN: #mario keydown
                        if event.key == pygame.K_UP:
                            mario.up = True
                            mario.down = False
                        elif event.key == pygame.K_DOWN:
                            mario.down = True
                            mario.up = False
                    if event.type == pygame.KEYUP: #mario up
                        if event.key == pygame.K_UP:
                            mario.up = False
                            mario.down = True
                        elif event.key == pygame.K_DOWN:
                            mario.down = True
                            mario.up = False
