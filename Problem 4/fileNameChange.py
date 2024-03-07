"""
    Name: Luke Runnels
    Lab time: 3/8/2024
"""

def fileNameChange():
    #type your code here
    filepath = input()
    
    with open(filepath, "r") as file:
        photoFileNames = file.readlines()
        for photoFileName in photoFileNames:
            photoFileName_Parts = photoFileName.split('_')
            photoName = photoFileName_Parts[0]
            print(f'{photoName}_info.txt')
    return

if __name__ == '__main__':
    fileNameChange()