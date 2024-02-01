import PyRPAFramework as PyRPA
from dotenv import load_dotenv
import os

load_dotenv()

config = PyRPA.InitAllSettings()

try:
    print('===> Happy python automation :) Your code here <===')
except Exception as e:
    print(f"General Exception Handling error detected: {str(e.args)}")