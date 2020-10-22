import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime
import cv2

def sign_in(meetingid, pswd):
    #Opens up the zoom app
    subprocess.call(["/usr/bin/open", "/Applications/zoom.us.app"])

    time.sleep(10)

    #clicks the join button
    x,y = pyautogui.locateCenterOnScreen('join_button.png', grayscale=True)
    join_btn = x*.5, y*.5  # don't know why it is off by a factor of 2
    pyautogui.moveTo(join_btn)
    pyautogui.click()

    # Type the meeting ID
    # x,y =  pyautogui.locateCenterOnScreen('meeting_id_button.png', grayscale=True)
    # meeting_id_btn = x*.5, y*.5
    # pyautogui.moveTo(meeting_id_btn)
    # pyautogui.click()
    pyautogui.write(meetingid)

    # Disables both the camera and the mic
    # x,y = pyautogui.locateAllOnScreen('media_btn.png', grayscale=True)
    # media_btn = x*.5, y*.5
    # for btn in media_btn:
    #     pyautogui.moveTo(btn)
    #     pyautogui.click()
    #     time.sleep(2)

    # Hits the join button
    pyautogui.press('enter')
    # x,y = pyautogui.locateCenterOnScreen('join_btn.png', grayscale=True)
    # join_btn = x*.5, y*.5
    # pyautogui.moveTo(join_btn)
    # pyautogui.click()

    time.sleep(2)
    #Types the password and hits enter
    # x,y = pyautogui.locateCenterOnScreen('meeting_pswd.png', grayscale=True)
    # meeting_pswd_btn = x*.5, y*.5
    # pyautogui.moveTo(meeting_pswd_btn)
    # pyautogui.click()
    pyautogui.write(pswd)
    pyautogui.press('enter')

# Reading the file
df = pd.read_csv('timings.csv')

while True:
    # checking of the current time exists in our csv file
    now = datetime.now().strftime("%H:%M")
    if now in str(df['timings']):

       row = df.loc[df['timings'] == now]
       m_id = str(row.iloc[0,1])
       m_pswd = str(row.iloc[0,2])

       sign_in(m_id, m_pswd)
       time.sleep(40)
       print('signed in')
