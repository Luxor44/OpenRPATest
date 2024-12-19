from MasterClass import MasterClass
import subprocess
from time import sleep
import os
import logging
import uuid
import re
import sys
import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import *
import json
import socket
from datetime import datetime, timedelta
from logging.handlers import RotatingFileHandler
from selenium.common.exceptions import NoSuchWindowException, StaleElementReferenceException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
logging.info(f'we are starting')
BrowserUrl = "google.com"
Chromeoptions = self.webdriver.ChromeOptions() 
DownloadOptions = {
"download.default_directory": self.DownloadDir, 
"download.prompt_for_download": False, 
"download.directory_upgrade": True,
"plugins.always_open_pdf_externally": True,
"profile.default_content_setting_values.automatic_downloads": 1
}
Chromeoptions.add_argument("--disable-search-engine-choice-screen")
Chromeoptions.add_argument("--disable-features=UseTensorFlowLite")
Chromeoptions.add_argument("--disable-features=UseXNNPACK")
Chromeoptions.add_experimental_option("prefs",DownloadOptions)

self.Browser = self.webdriver.Chrome(options=Chromeoptions)
self.OriginalWindow = self.Browser.current_window_handle



