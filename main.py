import subprocess
import pyautogui
import time
from datetime import datetime
import sys
import os

path = os.path.dirname(os.path.realpath(__file__))


class Zoom:
    """A class for zoom meetings."""

    def __init__(self, meetingid, pswd=None):
        self.meeting_id = meetingid
        self.password = pswd

    def check_video_status():
        """Checks to see if audio is muted and video is turned off."""

        if pyautogui.locateOnScreen(os.path.join(path, 'stop_video.png'), grayscale=True, confidence=0.9):
            stop_video_btn = pyautogui.locateCenterOnScreen('stop_video.png', grayscale=True, confidence=0.9)
            pyautogui.moveTo(stop_video_btn)
            pyautogui.click()
            print(f'Video turned off at {datetime.now()}')

        if pyautogui.locateOnScreen(os.path.join(path, 'mute.png'), grayscale=True, confidence=0.9):
            mute_btn = pyautogui.locateCenterOnScreen('mute.png', grayscale=True, confidence=0.9)
            pyautogui.moveTo(mute_btn)
            pyautogui.click()
            print(f'Audio turned off at {datetime.now()}')

    def in_meeting():
        """Checks to see if you are currently in a Zoom meeting."""

        if pyautogui.locateOnScreen(os.path.join(path, 'leave_btn.png'), grayscale=True, confidence=0.9):
            return True
        elif pyautogui.locateOnScreen(os.path.join(path, 'end_btn.png'), grayscale=True, confidence=0.9):
            return True
        elif pyautogui.locateOnScreen(os.path.join(path, 'waiting_for_host.png'), grayscale=True, confidence=0.9):
            exit_btn = pyautogui.locateCenterOnScreen('exit.png', grayscale=True, confidence=0.9)
            pyautogui.moveTo(exit_btn)
            pyautogui.click()
            print(f'Waiting for host to start meeting.')
            return False
        elif pyautogui.locateOnScreen(os.path.join(path, 'unable_to_join.png'), grayscale=True, confidence=0.9):
            okay_btn = pyautogui.locateCenterOnScreen('okay.png', grayscale=True, confidence=0.9)
            pyautogui.moveTo(okay_btn)
            pyautogui.click()
            raise Exception("Unable to join meeting!")
        else:
            return False

    def sign_out(end_time=None):
        """Leaves a zoom meeting."""

        if pyautogui.locateOnScreen('leave_btn.png', grayscale=True, confidence=0.9):
            leave_btn = pyautogui.locateCenterOnScreen('leave_btn.png', grayscale=True, confidence=0.9)
            pyautogui.moveTo(leave_btn)
            pyautogui.click()
        elif pyautogui.locateOnScreen('end_btn.png', grayscale=True, confidence=0.9):
            end_btn = pyautogui.locateCenterOnScreen('end_btn.png', grayscale=True, confidence=0.9)
            pyautogui.moveTo(end_btn)
            pyautogui.click()
            end_all_btn = pyautogui.locateCenterOnScreen('end_mtg_btn.png', grayscale=True, confidence=0.9)
            pyautogui.moveTo(end_all_btn)
            pyautogui.click()

    def sign_in(meetingid, pswd=None):
        """
        Sign into a zoom meeting.

        meetingid is the 10 digit meeting code
        pswd is the password, if applicable
        """

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

        if pswd:
            # Types the password and hits enter
            pyautogui.write(pswd)
            pyautogui.press('enter')
            time.sleep(10)


if __name__ == "__main__":
    m_id = int(sys.argv[1])

    try:  # todo: this might not be the best way to implement this
        m_pswd = str(sys.argv[2])
    except:
        m_pswd = None

    Zoom(m_id, pswd=m_pswd).sign_in()

    if Zoom.in_meeting() is True:
        print(f'Successful sign in at {datetime.now()}')

    while Zoom.in_meeting() is False:
        print(f'Failed attempt to join meeting at {datetime.now()}')
        time.sleep(60)
        Zoom.sign_in(m_id, pswd=m_pswd)
        Zoom.in_meeting()
