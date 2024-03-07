"""
    Name: Luke Runnels
    Lab time: 3/8/2024
"""

def courseGrade():
    
    filename = input()
    midterm1Avg = 0
    midterm2Avg = 0
    finalAvg = 0
    grades = []

    with open(filename, "r") as file:
        rows = file.readlines()

        for row in rows:
            row = row.strip("\n") 
            nameAndGrade = row.split("\t")

            firstName = ''
            lastName = ''
            midterm1 = 0
            midterm2 = 0
            final = 0

            if (nameAndGrade[1].isnumeric()):
                firstAndLastName = nameAndGrade[0].split(" ")
                firstName = firstAndLastName[0]
                lastName = firstAndLastName[len(firstAndLastName)-1]
                midterm1 = int(nameAndGrade[1])
                midterm2 = int(nameAndGrade[2])
                final = int(nameAndGrade[3])
            else:
                firstName = nameAndGrade[0]
                lastName = nameAndGrade[1]
                midterm1 = int(nameAndGrade[2])
                midterm2 = int(nameAndGrade[3])
                final = int(nameAndGrade[4])

            grades.append([
                firstName, 
                lastName,
                midterm1, 
                midterm2, 
                final, 
                calculateGrade(midterm1, midterm2, final)
            ])
            midterm1Avg += midterm1
            midterm2Avg += midterm2
            finalAvg += final

        midterm1Avg /= len(rows)
        midterm2Avg /= len(rows)
        finalAvg /= len(rows)

    reportNumber = extractNumberFromFileName(filename)
    with open(f'./Problem 3/report{reportNumber}.txt', "w") as file:
        for grade in grades:
            firstName = grade[0]
            lastName = grade[1]
            midterm1Score = grade[2]
            midterm2Score = grade[3]
            finalScore = grade[4]
            gradeLetter = grade[5]  
            file.write(f'{firstName}\t{lastName}\t{midterm1Score}\t{midterm2Score}\t{finalScore}\t{gradeLetter}\n')
        
        file.write(f'Averages: midterm1 {midterm1Avg:.2f}, midterm2 {midterm2Avg:.2f}, final {finalAvg:.2f}')

def calculateGrade(midterm1, midterm2, final):
    gradeAvg = (midterm1 + midterm2 + final) / 3
    if (90 <= gradeAvg):
        return 'A'
    elif (80 <= gradeAvg and gradeAvg < 90):
        return 'B'
    elif (70 <= gradeAvg and gradeAvg < 80):
        return 'C'
    elif (60 <= gradeAvg and gradeAvg < 70):
        return 'D'
    else:
        return 'F'

def extractNumberFromFileName(filename):
    if filename[-5].isnumeric():
        return filename[-5]
    
    return ""

if __name__ == "__main__":
    courseGrade()
    
    