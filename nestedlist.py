# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.


if __name__ == '__main__':
    students=[]
    grades = []
    for _ in range(int(input())):
        
        name = input()
        score = float(input())
        
        students.append([name,score])
    
    for stud in students:
        grades.append(stud[1])
        
    grades.sort()
    
    secondLowest = grades[1]
    
    final_names = []
    
    for stud in students :
        if secondLowest == stud[1] :
            final_names.append(stud[0])
            
    final_names.sort()
    
    for stud in final_names :
        print(stud)
        
    
        
    
        
        