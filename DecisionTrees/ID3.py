import math
#Training Data from the video
training_data = [
    ['Green', 3, 'Sour', 'Apple'],
    ['Yellow', 3, 'Sweet', 'Apple'],
    ['Red', 1, 'Sweet', 'Grape'],
    ['Red', 1, 'Sweet', 'Grape'],
    ['Yellow', 3, 'Sour', 'Lemon'],
    ['Red', 3, 'Sweet', 'Apple'],
    ['Green', 2, 'Sour', 'Lime'],
    ['Orange', 3, 'Sweet', 'Orange'],
    ['Purple', 1, 'Sweet', 'Grape'],
]

#Our goal will be to predict a fruit based on sie and colour and whether its sweet or sour.

#print unique_values
def unique_vals(rows,col):
    return set([row[col] for row in rows])

#Showcases unique values in the colour column 1 would be size , 2 would be sweet/sour and 3 would be label 
print(unique_vals(training_data,0))

def class_counts(rows):
    #counts the number of each type of example in the dataset
    counts = {}
    for row in rows:
        #the label is always the last column for our dataset format
        label = row[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] +=1
        
    return counts

print(class_counts(training_data))


#Implementing ID3 - before it can make decisions - the algorithm need a function to calculate the score
def entropy(rows):
    counts = class_counts(rows)
    impurity = 0
    total_rows = float(len(rows))
    #Go through each fruit type to calculate the math
    for label in counts:
        prob = counts[label] / total_rows #this is probability
        impurity -= prob * math.log2(prob) #this is -p * log(2p)

def partition(rows,question):
    #partitions a dataset (given in the name)
    true_rows, false_rows = [],[]
    for row in rows:
        if row[question.column] == question.value:
            true_rows.append(row)
        else:
            false_rows.append(row)
    return true_rows,false_rows

def info_gain(left,right,current_uncertainity):
    #info gain calculation
    p = float(len(left)) / (len(left) + len(right))
    return current_uncertainity - p * entropy(left) - (1-p) * entropy(right)

def find_best_split(rows)
    current_uncertainity = entropy(rows) #calculate starting score
    best_gain = 0
    best_question = None
    n_features = len(rows[0] - 1)

    for col in range(n_features):
        values = set([row[col] for row in rows])
        for val in values:
            question = Question(col, val)
            true_rows, false_rows = partition(rows, question)
            
            if len(true_rows) == 0 or len(false_rows) == 0:
                continue

            gain = info_gain(true_rows, false_rows, current_uncertainity)

            if gain >= best_gain:
                best_gain, best_question = gain, question

    return best_gain, best_question

# Define Classes that we are using 
class Question:
    #A question is used to partition a dataset
    def __init__(self,column,value):
        self.column = column
        self.value = value
    
    def match(self,example):
        val = example[self.column]
        return val == self.value
    
    def __repr__(self):
        condition = "=="
        return "Is %s %s %s?" % (header[self.column],condition,str(self.value))

class LeafNode:
    def __init__(self,rows):
        self.predictions = class_counts(rows)

class DecisionNode:
    def __init__(self,question,true_branch,false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch

##TREE BUILDING TIME

def build_tree(rows)
    #USES RECURSION TO BUILD TREES
    gain, question  = find_best_split(rows)

    if gain == 0:
        return LeafNode(rows)
    
    true_rows , false_rows = partition(rows,question)
    true_branch = build_tree(true_rows)
    false_branch = build_tree(false_rows)

    return DecisionNode(question,true_branch,false_branch)
    
    
