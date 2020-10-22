import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime
import sys
import os

path = os.path.dirname(os.path.realpath(__file__))

def check_video_status():
    if pyautogui.locateOnScreen(os.path.join(path, 'stop_video.png'), grayscale=True, confidence=0.9):
        stop_video_btn = pyautogui.locateCenterOnScreen('stop_video.png', grayscale=True, confidence=0.9)
        pyautogui.moveTo(stop_video_btn)
        pyautogui.click()
        print(f'Video turned off at {datetime.now()}')

    if pyautogui.locateOnScreen(os.join.path(path, 'mute.png'), grayscale=True, confidence=0.9):
        mute_btn = pyautogui.locateCenterOnScreen('mute.png', grayscale=True, confidence=0.9)
        pyautogui.moveTo(mute_btn)
        pyautogui.click()
        print(f'Audio turned off at {datetime.now()}')


def check_sucessful():
    if pyautogui.locateOnScreen(os.join.path(path, 'leave_btn.png'), grayscale=True, confidence=0.9):
        return True
    elif pyautogui.locateOnScreen(os.join.path(path, 'waiting_for_host.png'), grayscale=True, confidence=0.9):
        exit_btn = pyautogui.locateCenterOnScreen('exit.png', grayscale=True, confidence=0.9)
        pyautogui.moveTo(exit_btn)
        pyautogui.click()
        time.sleep(60)
        return False
    elif pyautogui.locateOnScreen(os.join.path(path, 'unable_to_join.png'), grayscale=True, confidence=0.9):
        okay_btn = pyautogui.locateCenterOnScreen('okay.png', grayscale=True, confidence=0.9)
        pyautogui.moveTo(okay_btn)
        pyautogui.click()
        raise Exception("Unable to join meeting!")
    else:
        return False


def sign_in(meetingid, pswd):
    # Opens up the zoom app
    subprocess.call(["/usr/bin/open", "/Applications/zoom.us.app"])

    time.sleep(5)

    # clicks the join button
    join_btn = pyautogui.locateCenterOnScreen(os.path.join(path, 'join_button.png'), grayscale=True, confidence=0.9)
    # fixed retina doubling issue, see https://github.com/asweigart/pyautogui/issues/33
    pyautogui.moveTo(join_btn)
    pyautogui.click()

    # Type the meeting ID
    pyautogui.write(str(meetingid))

    # Disables both the camera and the mic
    # media_btn = pyautogui.locateAllOnScreen('media_btn.png', grayscale=True, confidence=0.9)
    # for btn in media_btn:
    #     center = pyautogui.center(btn)
    #     pyautogui.moveTo(center)
    #     pyautogui.click()
    #     time.sleep(1)

    # Hits the join button
    pyautogui.press('enter')
    time.sleep(1)

    # Types the password and hits enter
    pyautogui.write(pswd)
    pyautogui.press('enter')
    time.sleep(10)


if __name__ == "__main__":
    m_id = int(sys.argv[1])
    m_pswd = str(sys.argv[2])

    sign_in(m_id, m_pswd)
    if check_sucessful() is True:
        print(f'Sucessfully signed in at {datetime.now()}')
