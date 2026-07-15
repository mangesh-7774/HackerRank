# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.


if __name__ == '__main__':
    students=[]
    grades = []
    for _ in range(int(input())):
        
        name = input()
        score = float(input())
        
        students.append([name,score])
        
    grades = sorted(set(score for name,score in students))
    secondLowest = grades[1]
   
    
    final_names = []
    
    for name,score in students :
        if score == secondLowest :
            final_names.append(name)
            
    final_names.sort()
    
    for names in sorted(final_names) :
        print(names)
        