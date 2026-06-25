#'Hours Studied', 
##'Previous Scores', 
# 'Extracurricular Activities',
#'Sleep Hours'
#'Sample Question Papers Practiced', 
#'Performance Index'
import pickle

studyhour = int(input("enter hour studie::"))
PreviousScores = int(input("enter Previous Scores::"))
ExtracurricularActivities= int(input("enter  actvivitie::"))
SleepHours= int(input("enter  SleepHours::"))
SampleQuestion= int(input("enter solved  questions")) 

with open("C:\\Users\\User\\Desktop\\python\\ml\\student_performance", "rb") as file:
    model = pickle.load(file)

predication = model.predict([[studyhour,  PreviousScores , ExtracurricularActivities , SleepHours , SampleQuestion]])[0]
print("your scores is:: " , predication)
