# -*- coding: utf-8 -*-
"""
File with some utility fcts...
"""
import logging
import xml.etree.ElementTree as ET
import cv2

import numpy as np
from PIL import ImageGrab


import io
import sys
import os
import contextlib


recording = False



# Read parameters from XML
def read_xml_config():
    param_path = resource_path("param.xml")  # Use the resource_path function here
    tree = ET.parse(param_path)
    root = tree.getroot()
    config = {}
    for child in root:
        config[child.tag] = child.text
    return config



# Initialize logging
def initialize_logger():
    logging.basicConfig(filename='execution.log', level=logging.INFO)
    return logging.getLogger()


"""
def record_window(title, out_filename='output_video.mp4'):
    global recording
    recording = True

    window = [window for window in getWindowsWithTitle(title) if title.lower() in window.title.lower()]
    
    if window:
        rect = window[0]._rect
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        recorder = cv2.VideoWriter(out_filename, fourcc, 20.0, (rect.width, rect.height))

        while recording:
            screenshot = ImageGrab.grab(bbox=(rect.left, rect.top, rect.left + rect.width, rect.top + rect.height))
            frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2RGB)
            recorder.write(frame)

        recorder.release()
    else:
        print("No window found with given title.")
"""

# New function to record the full screen
def record_full_screen(out_filename='output_video.mp4'):
    global recording
    recording = True

    # Screen dimensions can be dynamic based on your needs
    screen_size = (1920, 1080)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    recorder = cv2.VideoWriter(out_filename, fourcc, 20.0, screen_size)

    while recording:
        screenshot = ImageGrab.grab(bbox=(0, 0, screen_size[0], screen_size[1]))
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2RGB)
        recorder.write(frame)

    recorder.release()
def stop_recording():
    global recording
    recording = False
    
    




# Function to get the path of bundled files
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



"""
redirect logs to file (from lackey etc)
"""
    
@contextlib.contextmanager
def capture_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

