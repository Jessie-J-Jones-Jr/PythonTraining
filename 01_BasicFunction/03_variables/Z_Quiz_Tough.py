import random

# List of 50 questions
questions = [
    {"question": "What is the type of 10?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "a", "type_check": "print(type(10))"},
    {"question": "What is the type of 3.14?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "b", "type_check": "print(type(3.14))"},
    {"question": "What is the type of 'Hello'?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "c", "type_check": "print(type('Hello'))"},
    {"question": "What is the type of True?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "d", "type_check": "print(type(True))"},
    {"question": "What is the type of [1, 2, 3]?", "options": ["a) list", "b) tuple", "c) dict", "d) set"], "correct_answer": "a", "type_check": "print(type([1, 2, 3]))"},
    {"question": "What is the type of (1, 2, 3)?", "options": ["a) list", "b) tuple", "c) dict", "d) set"], "correct_answer": "b", "type_check": "print(type((1, 2, 3)))"},
    {"question": "What is the type of {'a': 1, 'b': 2}?", "options": ["a) list", "b) tuple", "c) dict", "d) set"], "correct_answer": "c", "type_check": "print(type({'a': 1, 'b': 2}))"},
    {"question": "What is the type of {1, 2, 3}?", "options": ["a) list", "b) tuple", "c) dict", "d) set"], "correct_answer": "d", "type_check": "print(type({1, 2, 3}))"},
    {"question": "What is the type of 0.5?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "b", "type_check": "print(type(0.5))"},
    {"question": "What is the type of 'True'?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "c", "type_check": "print(type('True'))"},
    {"question": "What is the type of 5 + 5.0?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "b", "type_check": "print(type(5 + 5.0))"},
    {"question": "What is the type of None?", "options": ["a) int", "b) float", "c) str", "d) NoneType"], "correct_answer": "d", "type_check": "print(type(None))"},
    {"question": "What is the type of '10'?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "c", "type_check": "print(type('10'))"},
    {"question": "What is the type of {}?", "options": ["a) list", "b) tuple", "c) dict", "d) set"], "correct_answer": "c", "type_check": "print(type({}))"},
    {"question": "What is the type of {1, 2, 3}?", "options": ["a) list", "b) tuple", "c) dict", "d) set"], "correct_answer": "d", "type_check": "print(type({1, 2, 3}))"},
    {"question": "What is the type of 10/2?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "b", "type_check": "print(type(10/2))"},
    {"question": "What is the type of '3' + '4'?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "c", "type_check": "print(type('3' + '4'))"},
    {"question": "What is the type of len('Hello')?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "a", "type_check": "print(type(len('Hello'))"},
    {"question": "What is the type of str(10)?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "c", "type_check": "print(type(str(10)))"},
    {"question": "What is the type of True and False?", "options": ["a) int", "b) float", "c) bool", "d) NoneType"], "correct_answer": "c", "type_check": "print(type(True and False))"},
    # ... Continue with more questions, until there are 50 total
]
questions.extend([
    {"question": "What is the type of 42 + 3.0?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "b", "type_check": "print(type(42 + 3.0))"},
    {"question": "What is the type of {1: 'a', 2: 'b'}?", "options": ["a) list", "b) tuple", "c) dict", "d) set"], "correct_answer": "c", "type_check": "print(type({1: 'a', 2: 'b'}))"},
    {"question": "What is the type of range(5)?", "options": ["a) list", "b) tuple", "c) dict", "d) range"], "correct_answer": "d", "type_check": "print(type(range(5)))"},
    {"question": "What is the type of open('file.txt', 'r')?", "options": ["a) file", "b) io.TextIOWrapper", "c) str", "d) bool"], "correct_answer": "b", "type_check": "print(type(open('file.txt', 'r'))))"},
    {"question": "What is the type of (1 + 2j)?", "options": ["a) int", "b) float", "c) complex", "d) str"], "correct_answer": "c", "type_check": "print(type(1 + 2j))"},
    {"question": "What is the type of {1, 2, 3} | {2, 3, 4}?", "options": ["a) list", "b) tuple", "c) dict", "d) set"], "correct_answer": "d", "type_check": "print(type({1, 2, 3} | {2, 3, 4}))"},
    {"question": "What is the type of [1, 2] + [3, 4]?", "options": ["a) list", "b) tuple", "c) dict", "d) set"], "correct_answer": "a", "type_check": "print(type([1, 2] + [3, 4]))"},
    {"question": "What is the type of 10 // 3?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "a", "type_check": "print(type(10 // 3))"},
    {"question": "What is the type of [x for x in range(5)]?", "options": ["a) list", "b) tuple", "c) dict", "d) set"], "correct_answer": "a", "type_check": "print(type([x for x in range(5)]))"},
    {"question": "What is the type of [1, 2, 3] * 2?", "options": ["a) list", "b) tuple", "c) dict", "d) set"], "correct_answer": "a", "type_check": "print(type([1, 2, 3] * 2))"},
    {"question": "What is the type of 'a' * 3?", "options": ["a) str", "b) int", "c) list", "d) bool"], "correct_answer": "a", "type_check": "print(type('a' * 3))"},
    {"question": "What is the type of {'name': 'Alice', 'age': 30}['name']?", "options": ["a) list", "b) tuple", "c) str", "d) dict"], "correct_answer": "c", "type_check": "print(type({'name': 'Alice', 'age': 30}['name']))"},
    {"question": "What is the type of {1: 'a', 2: 'b'}[1]?", "options": ["a) list", "b) tuple", "c) str", "d) dict"], "correct_answer": "c", "type_check": "print(type({1: 'a', 2: 'b'}[1]))"},
    {"question": "What is the type of frozenset([1, 2, 3])?", "options": ["a) set", "b) frozenset", "c) list", "d) tuple"], "correct_answer": "b", "type_check": "print(type(frozenset([1, 2, 3])))"},
    {"question": "What is the type of 2 ** 3?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "a", "type_check": "print(type(2 ** 3))"},
    {"question": "What is the type of 'abc'.find('b')?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "a", "type_check": "print(type('abc'.find('b'))"},
    {"question": "What is the type of [1, 2, 3] == [1, 2, 3]?", "options": ["a) bool", "b) int", "c) str", "d) list"], "correct_answer": "a", "type_check": "print(type([1, 2, 3] == [1, 2, 3]))"},
    {"question": "What is the type of [1, 2, 3] != [1, 2, 3]?", "options": ["a) bool", "b) int", "c) str", "d) list"], "correct_answer": "a", "type_check": "print(type([1, 2, 3] != [1, 2, 3]))"},
    {"question": "What is the type of zip([1, 2], ['a', 'b'])?", "options": ["a) list", "b) tuple", "c) dict", "d) zip"], "correct_answer": "d", "type_check": "print(type(zip([1, 2], ['a', 'b'])))"},
    {"question": "What is the type of max([1, 2, 3])?", "options": ["a) int", "b) float", "c) str", "d) list"], "correct_answer": "a", "type_check": "print(type(max([1, 2, 3])))"},
    {"question": "What is the type of round(3.14159, 2)?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "b", "type_check": "print(type(round(3.14159, 2)))"},
    {"question": "What is the type of 'hello'.upper()?", "options": ["a) str", "b) int", "c) list", "d) bool"], "correct_answer": "a", "type_check": "print(type('hello'.upper()))"},
    {"question": "What is the type of isinstance(10, int)?", "options": ["a) bool", "b) int", "c) str", "d) float"], "correct_answer": "a", "type_check": "print(type(isinstance(10, int)))"},
    {"question": "What is the type of ord('A')?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "a", "type_check": "print(type(ord('A'))"},
    {"question": "What is the type of abs(-10)?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "a", "type_check": "print(type(abs(-10)))"}
])

questions.extend([
    # Implicit type conversions
    {"question": "TOUGH: What is the type of 1 + '1'?", "options": ["a) int", "b) str", "c) float", "d) TypeError"], "correct_answer": "d", "type_check": "print(type(1 + '1'))",
     "explanation": "In Python, adding an integer (1) to a string ('1') results in a TypeError because Python cannot implicitly convert between these types. The operation is invalid and will raise an error."},

    # Complex number handling
    {"question": "TOUGH: What is the type of 2j + 2?", "options": ["a) int", "b) float", "c) complex", "d) str"], "correct_answer": "c", "type_check": "print(type(2j + 2))",
     "explanation": "2j is a complex number. When adding a complex number (2j) to an integer (2), Python produces a complex result. The type of 2j + 2 is 'complex'."},

    # Set and dictionary confusion
    {"question": "TOUGH: What is the type of {'a': 1, 'b': 2} | {'b': 3, 'c': 4}?", "options": ["a) dict", "b) set", "c) frozenset", "d) list"], "correct_answer": "a", "type_check": "print(type({'a': 1, 'b': 2} | {'b': 3, 'c': 4}))",
     "explanation": "In Python 3.9 and above, the union operator (|) is supported for dictionaries, resulting in a merged dictionary. This operation will return a 'dict'."},

    # Mutable and immutable types
    {"question": "TOUGH: What is the type of id([1, 2, 3])?", "options": ["a) int", "b) str", "c) list", "d) NoneType"], "correct_answer": "a", "type_check": "print(type(id([1, 2, 3])))",
     "explanation": "The 'id()' function returns a unique integer identifier for an object in memory. The type of the result is always 'int', as it is a memory address."},

    # Negative indexing on strings
    {"question": "TOUGH: What is the type of 'Python'[-1]?", "options": ["a) int", "b) str", "c) list", "d) char"], "correct_answer": "b", "type_check": "print(type('Python'[-1]))",
     "explanation": "In Python, negative indexing returns elements from the end of a sequence. Here, 'Python'[-1] refers to the last character 'n', which is of type 'str'."},

    # Nested list indexing
    {"question": "TOUGH: What is the type of [[1, 2], [3, 4]][0][1]?", "options": ["a) int", "b) list", "c) tuple", "d) str"], "correct_answer": "a", "type_check": "print(type([[1, 2], [3, 4]][0][1]))",
     "explanation": "The expression [[1, 2], [3, 4]][0][1] accesses the first list [1, 2] and retrieves the element at index 1, which is the integer 2. Hence, the type is 'int'."},

    # String representation of a complex expression
    {"question": "TOUGH: What is the type of str(3 + 5 * 2)?", "options": ["a) int", "b) str", "c) float", "d) bool"], "correct_answer": "b", "type_check": "print(type(str(3 + 5 * 2)))",
     "explanation": "The expression 3 + 5 * 2 evaluates to 13, which is converted into a string by the str() function. Therefore, the result is of type 'str'."},

    # The behavior of the float type
    {"question": "TOUGH: What is the type of 0.1 + 0.2 == 0.3?", "options": ["a) bool", "b) int", "c) float", "d) str"], "correct_answer": "a", "type_check": "print(type(0.1 + 0.2 == 0.3))",
     "explanation": "The expression 0.1 + 0.2 results in a floating-point precision issue and does not exactly equal 0.3. As a result, the expression evaluates to 'False', which is of type 'bool'."},

    # Comparing lists and tuples
    {"question": "TOUGH: What is the type of [1, 2] == (1, 2)?", "options": ["a) bool", "b) list", "c) tuple", "d) TypeError"], "correct_answer": "a", "type_check": "print(type([1, 2] == (1, 2)))",
     "explanation": "The expression [1, 2] == (1, 2) compares a list and a tuple, which are different types, resulting in a boolean 'False'. Thus, the type of the comparison is 'bool'."},

    # Edge case with `None`
    {"question": "TOUGH: What is the type of None == None?", "options": ["a) bool", "b) NoneType", "c) int", "d) TypeError"], "correct_answer": "a", "type_check": "print(type(None == None))",
     "explanation": "In Python, 'None' is a singleton object representing the absence of a value. Comparing None to None results in 'True', and the type of this comparison is 'bool'."},

    # `is` operator with integers
    {"question": "TOUGH: What is the type of 1000 is 1000?", "options": ["a) bool", "b) int", "c) str", "d) TypeError"], "correct_answer": "a", "type_check": "print(type(1000 is 1000))",
     "explanation": "The 'is' operator compares object identity. For small integers (like 1000), Python may cache the value, making the comparison return 'True' of type 'bool'."},

    # Complex `is` operator behavior with mutable objects
    {"question": "TOUGH: What is the type of [1] is [1]?", "options": ["a) bool", "b) list", "c) int", "d) TypeError"], "correct_answer": "a", "type_check": "print(type([1] is [1]))",
     "explanation": "Lists are mutable, so even if two lists contain the same elements, they are different objects in memory. Hence, the 'is' comparison returns 'False' of type 'bool'."},

    # Edge case with `set`
    {"question": "TOUGH: What is the type of set([1, 2, 2, 3])?", "options": ["a) list", "b) set", "c) tuple", "d) dict"], "correct_answer": "b", "type_check": "print(type(set([1, 2, 2, 3])))",
     "explanation": "The 'set' function removes duplicates from the input list and creates a set. The result will be a set type containing {1, 2, 3}."},

    # List with mixed types
    {"question": "TOUGH: What is the type of [1, '2', 3.0]?", "options": ["a) list", "b) tuple", "c) dict", "d) str"], "correct_answer": "a", "type_check": "print(type([1, '2', 3.0]))",
     "explanation": "A list can contain elements of different types, such as integers, strings, and floats. The type of this mixed list is 'list'."},

    # Negative behavior with floating point precision
    {"question": "TOUGH: What is the type of 0.1 + 0.2?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "b", "type_check": "print(type(0.1 + 0.2))",
     "explanation": "Floating-point precision issues occur in Python when dealing with certain decimal values like 0.1 + 0.2. The result is a float, despite its apparent imprecision."},

    # Mutable object identity
    {"question": "TOUGH: What is the type of id([]) == id([])?", "options": ["a) bool", "b) int", "c) str", "d) TypeError"], "correct_answer": "a", "type_check": "print(type(id([]) == id([])))",
     "explanation": "The 'id()' function returns a unique identifier for each object. Comparing two different lists with 'id()' will always return False, and the result of the comparison is a boolean ('bool')."},

    # Multiple assignment
    {"question": "TOUGH: What is the type of x, y = 5, 'Hello'?", "options": ["a) tuple", "b) int", "c) str", "d) list"], "correct_answer": "a", "type_check": "print(type(x, y = 5, 'Hello'))",
     "explanation": "The multiple assignment x, y = 5, 'Hello' creates a tuple (5, 'Hello') with two elements. The type of the result is 'tuple'."},
])

# Function to run the quiz
def run_quiz():
    score = 0
    num_questions = 10  # We'll ask 10 random questions

    # Shuffle the questions and select 10 random ones
    random.shuffle(questions)
    selected_questions = questions[:num_questions]

    # Loop through the selected questions and ask the user
    for q in selected_questions:
        print(q["type_check"])  # Display the type check print statement
        print(q["question"])
        for option in q["options"]:
            print(option)

        # Get the user's answer
        answer = input("Your answer (a/b/c/d): ").lower()

        # Check if the answer is correct
        if answer == q["correct_answer"]:
            score += 1

    # Calculate and print the result
    percentage = (score / num_questions) * 100
    print(f"\nQuiz complete! You got {score} out of {num_questions} correct.")
    print(f"Your score: {percentage:.2f}%")

# Run the quiz
if __name__ == "__main__":
    run_quiz()
