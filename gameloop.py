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

            score_font = font.render('Score:' + str(SCORE), True, GREEN)
            score_font_rect = score_font.get_rect()
            score_font_rect.center = (200, cactus_img_rect.bottom + score_font_rect.height / 2)
            canvas.blit(score_font, score_font_rect)

            level_font = font.render('Level:' + str(LEVEL), True, GREEN)
            level_font_rect = level_font.get_rect()
            level_font_rect.center = (500, cactus_img_rect.bottom + score_font_rect.height / 2)
            canvas.blit(level_font, level_font_rect)

            top_score_font = font.render('Top Score:' + str(topscore.high_score), True, GREEN)
            top_score_font_rect = top_score_font.get_rect()
            top_score_font_rect.center = (800, cactus_img_rect.bottom + score_font_rect.height / 2)
            canvas.blit(top_score_font, top_score_font_rect)

            canvas.blit(cactus_img, cactus_img_rect)
            canvas.blit(fire_img, fire_img_rect)
            mario.update()
            for f in flames_list:
                if f.flames_img_rect.colliderect(mario.mario_img_rect):
                    game_over()
                    if SCORE > mario.mario_score:
                        mario.mario_score = SCORE
            pygame.display.update()
            CLOCK.tick(FPS)