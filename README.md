# Directory Organizer

Directory Organizer is a simple python script that allows you to organize files in a directory based on your preference of file extensions and folder namings from a simple configuration file.


# Requirements

**Here are the required modules to run it:**

    os
    shutil
    argparse
    configparser

# How to use it?

The configuration file is accessed by opening **config.ini** in any text editor.

![How config.ini looks like](https://i.ibb.co/k5hmnNV/Screenshot-815.png)

### Now let's discuss each section
#### Supported Extensions
To the left of the assignment is where you put your extension type and to the right is what it is categorized as.
#### Folder Mapping
To the left of the assignment is a "category" name, it has to be equivalent to one of the categories you used on the **right-hand** of the assignment in the **extensions section** and to the right of the assignment is the **Folder name** that these categorized images will be moved to in the end.
#### Settings
Each setting is a boolean either True or False, current settings are for showing final stats about how many files were moved and so on. The **collapse** setting is for grouping all created folders into 1 folder called **Directory Manager** to avoid overlapping of similar folders already existing in the pre-organised directory

## Launching

    python main.py -p "Path to directory here"
    
   Example:
   
   ![Example](https://i.ibb.co/wJJgQTf/Screenshot-816.png)


# Suggestions

I'm always open to suggestions to improve this script, so contact me anytime =)
