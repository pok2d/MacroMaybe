from pynput import keyboard

currenlogpress = ''
with keyboard.Events() as events:
    for event in events:
        if event.key == keyboard.Key.esc:
            print(currenlogpress)
            break
        else:
            curletter = str(format(event))
            if curletter.find('P') == 0:
                if curletter.find("'") == 10:
                    currenlogpress += curletter[11]
                    #print('Letter added')
                elif curletter[14] == 's':
                    if curletter[15] == 'p':
                        currenlogpress += ' '
                        #print('Space')
                elif curletter[14] == 'b':
                    if curletter[15] == 'a':
                        currenlognumero = len(currenlogpress)
                        currenlogpress = currenlogpress[:currenlognumero-1]
                        #print('Backspace')



