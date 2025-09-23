#Python Alaram Clock 
import time 
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "alarm_sound.mp3"  # Ensure you have an alarm sound file in the same directory
    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current time: {current_time}", end="\r")
        if current_time == alarm_time:
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            pygame.mixer.quit()
            print("Wake up! Alarm ringing...")
            is_running = False
        time.sleep(1)

# Example usage:            


if __name__ == "__main__":
    alarm_time = input("Enter the alarm time in (HH:MM:SS) format (24-hour): ")
    set_alarm(alarm_time)