import os
import shutil


# Set the target directory to copy the files to
target_dir = 'build/'

# Set the list of extensions to search for
extensions = ['.txt', '.pdf', '.docx', ".png", ".jpg", ".jpeg", ".mp4", ".rtf", ".html", '.mp3', '.wav']


# Set the directory to start the search in
start_dir = '/'


# Results Page To Change Content
results_page = 'build/Results/index.html'

file = None
with open (results_page, 'w') as file:
    file.write('<!DOCTYPE html>\n<html lang=en>\n<head>\n<meta charset=UTF-8>\n<meta name=viewport, initial-scale=1.0>\n<title>Merdium - Results</title>\n<link rel=\"stylesheet\" href=\"stylesheet.css\">\n</head>\n<body>\n<div id=\"files\">\n')

# Loop through all the files in the directory and its subdirectories
for dirpath, dirnames, filenames in os.walk(start_dir):
    for filename in filenames:
        # Check if the file has one of the extensions we're interested in
        if any(filename.endswith(ext) for ext in extensions):
            # Print the name of the file to the terminal
            print(os.path.join(dirpath, filename))
            # Copy the file to the target directory
            try:
                
                if filename.endswith('.txt') or filename.endswith('.docx') or filename.endswith('.rtf'):
                    shutil.copy(os.path.join(dirpath, filename), target_dir + 'TEXT Files')
                elif filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
                    shutil.copy(os.path.join(dirpath, filename), target_dir + 'PHOTO Files')
                elif filename.endswith('.mp4'):
                    shutil.copy(os.path.join(dirpath, filename), target_dir + 'VIDEO Files')
                elif filename.endswith('.wav') or filename.endswith('.mp3'):
                    shutil.copy(os.path.join(dirpath, filename), target_dir + 'AUDIO Files')
                else:
                    shutil.copy(os.path.join(dirpath, filename), target_dir + 'OTHER Files')
                with open (results_page, 'a') as file:
                    file.write(dirpath + filename + '<br>')

            except PermissionError:
                with open (results_page, 'a') as file:
                    file.write(dirpath + filename + " Permission Error : Acces Denied - Skipping File" + '<br>')
                print("Permission Error : Acces Denied - Skipping File")
                continue
            except Exception as E:
                print('Acces Denied : ')
                print(E)
                with open (results_page, 'a') as file:
                    file.write(dirpath + filename + " Unknown Error : Acces Denied - Skipping File" + '<br>')
                continue




