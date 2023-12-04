import functions as func  # imports functions.py module as func for main.py

# Call the functions with appropriate arguments
book_title = func.favorite_book("Will you still love me ")
print(book_title)

shirt_result = func.make_shirt(size="Small", message="I love food")
print(shirt_result)

car = func.cars("Jeep", "Rubicon", year=2023, color="Red")
print(car)

result = func.sum_and_sort_numbers(8, 4.6)
print(result)
