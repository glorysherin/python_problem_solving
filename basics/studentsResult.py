# write a program to calculate a student's result based on  two examinations, 1 sports event, and 3 activities conducted.The weightage of activities = 30 percent, sports = 20 percent,and examination  = 50 percent.
exam_weightage=30.0
sports_weightage=20.0
activity_weightage=50.0

exam_total=200.0
sports_total = 50.0
activity_total = 60.0

exam1= int(input("Enter the mark of first exam (out of 100): "))
exam2= int(input("Enter the mark of second exam (out of 100): "))
sport= int(input("Enter the mark of sports (out of 50): "))
activity1= int(input("Enter the mark of first activity (out of 20) : "))
activity2= int(input("Enter the mark of second activity (out of 20): "))
activity3= int(input("Enter the mark of third activity (out of 20): "))

exam_percent =exam1+exam2
sport_percent=sport
activity_percent = activity1+activity2+activity3

exam_result= float(exam_percent*exam_weightage/exam_total)
sports_result= float(sport_percent*sports_weightage/sports_total)
activity_result= float(activity_percent*activity_weightage/activity_total)
print("-----Result------")
print("Total percentage in examination is : ",exam_result)
print("Total percentage in sports is : ",sports_result)
print("Total percentage in activity is : ",activity_result)