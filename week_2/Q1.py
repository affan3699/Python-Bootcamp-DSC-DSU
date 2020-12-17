import os

filesList = []
dictionary = []

def displayAllFiles():
    filePath = input("Enter Path: ")
    filesList = os.listdir(path=filePath)

    for fileName in filesList:
        file_stats = os.stat(filePath + "/" + fileName)
        fileSize = file_stats.st_size
        dictionary.append({"FileName":fileName, "FileSize":fileSize})
    
    print("\nThe Files printed sorted by size in descending order: \n")
    
    for i in sorted(dictionary, key = lambda i: i['FileSize'],reverse=True):
        print(i["FileName"], end=' = ')
        print(i["FileSize"])

displayAllFiles()