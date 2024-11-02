# Project

Script that Organizes Files into Directories.

# Description

Create a Python script that organizes files in a directory into folders based on file type.

For example, all .txt files go into a "Text Files" folder,
all .jpg and .png files go into an "Images" folder, and so on.

# How the Project Works

Here are what the script should do step by step:

    1. **Use** glob **to Find Files**:

        - Use the glob module to find all files in the target directory with specific patterns (like .txt for text files).

    2. **Create Folders Based on File Type:**

        - For each file type, create a corresponding folder (e.g., "Text Files", "Images").

    3. **Move Files to the Appropriate Folder:**

        - Move the files into the appropriate folder based on their extension using shutil.move().

# Prerequisites

Required Libraries: glob

Required Files: No additional files are required.

# License

 <p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/WildZarek/PortfolioPy">PortfolioPy</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/WildZarek">WildZarek</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1" alt=""></a></p>