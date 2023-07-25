import os
import shutil
import tkinter
#Importing Modules That Will Be Used





# Set the list of extensions to search for
# ? Add Extensions That You Want To Search For (They Will Be On "OTHER Files" Folder)
extensions = ['.txt', '.pdf', '.docx', ".png", ".jpg", ".jpeg", ".mp4", ".rtf", ".html", '.mp3', '.wav']



#Starting Search Function
def START():
    


    #Create Folders If They Do Not Exist
    folders = ["Results", "VIDEO Files", "AUDIO Files", "TEXT Files", "PHOTO Files", "OTHER Files"]
    for folder in folders:
        folder_path = os.path.join(inputBOX2.get(), folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        else:
            print(f"Folder '{folder}' already exists at '{folder_path}'")

    
    #Show User To Wait
    loadLabel.config(text='Please Wait!')

    #Write The Beginning Of Result (index.html) File
    file = None
    results_page = inputBOX2.get() + '/Results/index.html'
    with open (results_page, 'w') as file:
        file.write('<!DOCTYPE html>\n<html lang=en>\n<head>\n<meta charset=UTF-8>\n<meta name=viewport, initial-scale=1.0>\n<title>Merdium - Results</title>\n<link rel=\"stylesheet\" href=\"stylesheet.css\">\n</head>\n<body>\n<div class=\"files\">\n')

    #Get Every Target Path
    # ! Do Not Add Spaces Between Paths Or Commas
    inputText = inputBOX.get()
    wordsList = []
    word = ""
    for i in inputText:
        if(i == ','):
            wordsList.append(word)
            word = ""
        else:
            word += i
    
    wordsList.append(word)

    # * Start Searching : 
    target_dir = inputBOX2.get()
    for start_dir in wordsList:
        # Get Every File One By One
        for dirpath, dirnames, filenames in os.walk(start_dir):
            for filename in filenames:
                # Check If File Extensions Is Searched Or Not
                if any(filename.endswith(ext) for ext in extensions):
                    # Print File's Path 
                    # TODO: Remove If You Do Not Want To See Debug Messages
                    print(os.path.join(dirpath, filename))
                    # * Copy Files To Directory
                    try:
                        # Check Which Type Of File This is : 
                        if filename.endswith('.txt') or filename.endswith('.docx') or filename.endswith('.rtf'):
                            shutil.copy(os.path.join(dirpath, filename), target_dir + '/TEXT Files')
                        elif filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
                            shutil.copy(os.path.join(dirpath, filename), target_dir + '/PHOTO Files')
                        elif filename.endswith('.mp4'):
                            shutil.copy(os.path.join(dirpath, filename), target_dir + '/VIDEO Files')
                        elif filename.endswith('.wav') or filename.endswith('.mp3'):
                            shutil.copy(os.path.join(dirpath, filename), target_dir + '/AUDIO Files')
                        else:
                            shutil.copy(os.path.join(dirpath, filename), target_dir + '/OTHER Files')
                        with open (results_page, 'a') as file:
                            file.write(dirpath + filename + '<br>')
                    # If There's No Permission
                    except PermissionError:
                        # ! Permission Error (Can Happen In System/Root Files Mostly)
                        # TODO: Remove If You Don't Want To See Debug Messages
                        with open (results_page, 'a') as file:
                            file.write(dirpath + filename + " Permission Error : Access Denied - Skipping File" + '<br>')
                        print("Permission Error : Access Denied - Skipping File")
                        continue
                    except Exception as E:
                        # ! Any Other Error That Could Happen
                        # TODO: Remove If You Don't Want To See Debug Messages
                        print('Access Denied : ')
                        print(E)
                        with open (results_page, 'a') as file:
                            file.write(dirpath + filename + " Unknown Error : Access Denied - Skipping File" + '<br>')
                        continue
    loadLabel.config(text='Finish!')
    





        




# * Designing GUI For App

window = tkinter.Tk()
window.title('Merdium')
mainLabel = tkinter.Label(window, text="MERDIUM")
helpLabel = tkinter.Label(window, text="Separate Paths By Comma(,)")
inputBOX = tkinter.Entry(window)
label2 = tkinter.Label(window, text="Enter Targets Path")
inputBOX2 = tkinter.Entry(window)
startBTN = tkinter.Button(window, command=START, text="START")
loadLabel = tkinter.Label(window, text="Press Start And Wait Until FINISH!")

window.config(bg="#101010")
window.resizable(False, False)
mainLabel.config(bg="#101010", fg="#AABBCC", font=('Consolas', 40))
helpLabel.config(bg="#101010", fg="#AABBCC", font=('Consolas', 20))
inputBOX.config(bg="#101010", fg="#AABBCC", font=('Consolas', 20))
label2.config(bg="#101010", fg="#AABBCC", font=('Consolas', 20))
inputBOX2.config(bg="#101010", fg="#AABBCC", font=('Consolas', 20))
startBTN.config(bg="#101010", fg="#AABBCC", font=('Consolas', 20))
loadLabel.config(bg='#101010', fg="#AABBCC", font=('Consolas', 15))


mainLabel.pack()
helpLabel.pack()
inputBOX.pack()
label2.pack()
inputBOX2.pack()
startBTN.pack()
loadLabel.pack()
window.mainloop()
# * Start The App