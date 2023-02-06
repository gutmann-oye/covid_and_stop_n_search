# -*- coding: utf-8 -*-
"""
GUI

@author: UTHMAN
"""
from pathlib import Path
import tkinter as tk
import os

window = tk.Tk()
window.title("COVID and Stop & Search Data Analysis")
window.geometry("600x400")

first_Label = tk.Label(window, text="Click any of the following MAIN programs you wish to run")
first_Label.pack()

    
def covid_data_analysis_file():
    program_file = Path(__file__).with_name('covid_data_analysis.ipynb')
    os.system('"%s"' % program_file)    # To cater for when there is space in the file location
    
def stop_and_search_data_analysis_file():
    program_file = Path(__file__).with_name('stop_and_search_data_analysis.ipynb')
    os.system('"%s"' % program_file)    
    
def covid_preprocess_file():
    program_file = Path(__file__).with_name('covid_data_preprocessing.ipynb')
    os.system('"%s"' % program_file)    
    
def stop_search_preprocess_file():
    program_file = Path(__file__).with_name('stop_search_data_preprocessing.ipynb')
    os.system('"%s"' % program_file) 



button_covid_data_analysis = tk.Button(window, text="COVID Data Analysis", command=covid_data_analysis_file)
button_covid_data_analysis.pack(pady=20)

button_stop_and_search_data_analysis = tk.Button(window, text="Stop and Search Data Analysis", command=stop_and_search_data_analysis_file)
button_stop_and_search_data_analysis.pack(pady=20)

second_Label = tk.Label(window, text="There are also these OTHER programs to run")
second_Label.pack()

button_covid_preprocess = tk.Button(window, text="COVID Data Preprocessing", command=covid_preprocess_file)
button_covid_preprocess.pack(pady=20)

button_stop_search_preprocess = tk.Button(window, text="Stop and Search Data Preprocessing", command=stop_search_preprocess_file)
button_stop_search_preprocess.pack(pady=20)

window.mainloop()
