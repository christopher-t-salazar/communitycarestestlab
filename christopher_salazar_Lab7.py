# christopher_salazar_Lab7.py
# Name: Christopher Salazar
# Date: 3/25/2015
# This program will grade students answers against the test bank.
# Program will tell student the correct/incorrect answers.


#Global Constants
testBank= ['B','D','A','A','C','A','B','A','C','D','B','C','D','A','D','C','C','B','D','A']

#Global Variables/List
stuAnswers=[None]*20
list_MissedQuestions=[]
cor_ANSWER=0
inc_ANSWER=0


# Main Function
def main():
    studentKey()
    testKey()
    grade()
     
    exit()
def studentKey():
    "This function will read the student.txt file and read the lines."
    global stuAnswers
    try:
        stuFile=open('StudentAnswer.txt', 'r')
        for a in range(len(stuAnswers)):
            stuAnswers[a]=stuFile.readline().rstrip('\n')
        stuFile.close()

        print('These are the Student\'s Answers:', stuAnswers)
    except IOError:
        print('An error occured trying to read the file.')

def testKey():
    "This function will compare student's answer to the test bank"
    global stuAnswers
    global list_MissedQuestions
    global cor_ANSWER
    global inc_ANSWER
    
    try:
        for i in range(len(testBank)):
            if testBank[i]==stuAnswers[i]:
                cor_ANSWER+=1
            else:
                inc_ANSWER+=1
                list_MissedQuestions.append(i+1)
    except ValueError:
        print('Incorrect values on Student exam.')
    except Exception as err:
        print(err)
    

def grade():
    "This function states whether the student has passed."
    try:
        if cor_ANSWER>=15:
            print('Student has PASSED the exam.')
        else:
            print('Student has FAILED the exam.')

        print('Student has answered',cor_ANSWER,'questions CORRECTLY.')
        print('Student has answered',inc_ANSWER,'questions INCORRECTLY')
        if inc_ANSWER>0:
            print('Question Numbers MISSED: ',list_MissedQuestions)
        else:
            print('Student has no missed questions!')

    except Exception as err:
        print(err)

# Call Main Function
main()
