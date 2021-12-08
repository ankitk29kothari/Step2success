
raise NameError('HiThere')
raise ValueError  # shorthand for 'raise ValueError()

IOError: if the file can’t be opened
KeyboardInterrupt: when an unrequired key is pressed by the user
ValueError: when built-in function receives a wrong argument
EOFError: if End-Of-File is hit without reading any data
ImportError: if it is unable to find the module


raise RuntimeError('Failed to open database')