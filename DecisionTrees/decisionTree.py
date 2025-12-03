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

#Implementing ID3
