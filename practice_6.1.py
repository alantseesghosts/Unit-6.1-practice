import csv
import math

def find_alice(filename):
    """
    Function that returns the number of times the word
    "Alice" appears in the story, 'Alice and Wonderland'.

    See Assignment 6.1 for requirement details.
    """
    with open(filename) as user_file:
        user_word = "Alice"
        #lower = user_word.lower()
        #found_the_word = False
        count = 0
        count = int(count)
        for every_line in user_file:
            
            for word in every_line.split():
                #print(word)
                if word == user_word:
                    #found_the_word = True
                    count = count + 1
                    
        return count
        """
        if not found_the_word:
            print("Didn't find the word")
            return None
"""


def calculate_average (record, start_col, count):
    """
    Function to calculate the average of count fields
    in a record, starting at start_col.

    Update to handle issues that might occur. Refer to 
    Assignment 6.1 for more details.
    """
    sum = 0
    
    count = int(count) 
    for index in range (start_col, start_col + count):
        number = record [index]
        try:
            sum += int (number)
        except ValueError:
            try:
                number = float(number)
            except ValueError:
                number = 0

            number = round(number)

            sum += (number)
        
        sum = int(sum)

    try:
        average = sum / count
    except ZeroDivisionError:
        return 0
    average = float(round(average,2))

    return average



def deans_list (filename, min_grade):
    """
    Function that prints the names of all students
    that are above the specified minimum grade average
    for all of their assignment.

    See Assignment 6.1 for requirement details.
    """
    with open(filename) as user_file:
        csv_reader = csv.reader(user_file)
        next(csv_reader)
        
        for record in csv_reader:
            print(record[0])
            i = 3
            #min_grade = float(min_grade)
            while i < 30:
                try:
                    record[i] = float(record[i])
                except ValueError:
                    record[i] = 0
                if record[i] > min_grade :  
                    print(record[i],sep = " ")
                i+=1

def main ():
    # Simple find_alice test
    #find_alice("data/alice.txt")
    #print ("Found Alice", find_alice ("data/alice.txt"), "times.")
    # Sample records that can be used to test calculate_avearge
    #clean_record = 'Student,80,68,75,81,85,93'.split (',')
    #dirty_record = 'Student,80,97.8,75,,85.4,a'.split (',')

    # calculate_average tests
    #print (calculate_average (clean_record, 1, 6)) # 80.3333333333
    #print (calculate_average (dirty_record, 1, 6)) # 56.3333333333

    # Test for deans_list
    deans_list ("data/full_grades_999.csv", 89)

if __name__ == "__main__":
    main ()