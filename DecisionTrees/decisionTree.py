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
def unique_vals(rows,cols):
    return set([row[col] for row in rows])

print(unique_vals(training_data,0))