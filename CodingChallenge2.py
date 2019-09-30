student_score= []
score_list= []
x=int(input("Please enter the number of students"))
i=0
for i in range(x):
    name= input("Enter the student's name:")
    score= float(input("Input the test grade:"))
    grades = grade + [[name,score]]
    score_list = score_list + [score]

x= sorted(score_list)

for a,c in range (sorted(grades)):
    if c==b:
        print (a)

