# Python ALarm clock

import datetime
import time
import pygame
                        # pip = pythoin package manager/installer (pip install pygame)
                        # Arch linux blocks pip - installs to prevent accidental breaking of OS's python dependencies , so i had to use "sudo pacman -S python-pygame"

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "chipi_chapa.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP !")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)         # load the music file (ready to play)
            pygame.mixer.music.play()                   # plays all the loaded files

            while pygame.mixer.music.get_busy():        # checks if the mixer is still busy (i.e., music is still playing)
                time.sleep(1)

            is_running = False

        time.sleep(1)


if __name__ == '__main__':
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)

