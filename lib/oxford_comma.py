def oxford_comma(items):
    if len(items) > 1:
        items[-1] = "and " + items[-1]

    if len(items) > 2:
        return ', '.join(items)
# Module oxford_comma.py adds commas plus a final "and" when given a 3-element list - 
#   AssertionError: assert None == 'kiwi, durian, and starfruit'

# Module oxford_comma.py correctly formats lists of lengths greater than three - 
#   AssertionError: assert None == 'kiwi, durian, starfruit, mangos, and dragon fruits'
    else:
        return ' '.join(items)

# Module oxford_comma.py returns a string without any additional formatting when given a 1-element list - 
#   AssertionError: assert None == 'kiwi'

# Module oxford_comma.py adds "and" between elements when given a 2-element list - 
#   AssertionError: assert None == 'kiwi and durian'

#NOTES FOR ME 
# this piece of Python code is a function called oxford_comma. 
# A function is like a set of instructions that the computer follows to do a specific task. In this case, the task is related to organizing a list of items.
# The function takes a list of items as input. A list is like a collection of things, like a shopping list or a list of your favorite animals. 
# The function wants to organize this list in a specific way.
# First, the function checks if there are more than one item in the list by using the len(items) > 1 condition. 
# If there is more than one item, it means there are multiple things in the list. The function then adds the word "and" before the last item in the list. So, if the list had items like "apples, bananas, and oranges," the function would add the "and" before "oranges."
# Next, the function checks if there are more than two items in the list by using the len(items) > 2 condition. 
# If there are more than two items, it means there are at least three things in the list. In this case, the function joins the items together using commas (,) between each item. So, if the list had items like "apples, bananas, and oranges," the function would join them as "apples, bananas, and oranges" with commas separating each item.
# If there are only two items in the list, the function skips the previous step and instead joins the items together using a space. So, if the list had items like "apples and oranges," the function would join them as "apples and oranges" with a space between them.

# The function helps organize a list of items by adding the word "and" and using commas to separate the items, 
# depending on how many items are in the list.