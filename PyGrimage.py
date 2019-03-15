# import modules
import random
import os
from sys import exit

# list containing right/wrong replies to questions
correct = ['<Correct>\n', '<Right>\n', '<Good!>\n', '<Excellent!>\n', '<True>\n', '<That\'s Right!>\n', '<Great!>\n']

incorrect = ['-Incorrect-\n', '-Wrong-\n', '-Untrue-\n', '-False-\n', '-Inaccurate-\n', '-Unsound-\n', '-Bogus-\n', '-Wide off the mark-\n']

# "a", "c", "f" = grading user score
a = ['<<< Perfect! >>>\n', '<<< Foolproof! >>>\n', '<<< Impeccable! >>>\n', '<<< Aces! >>>\n', '<<< Beyond Compare! >>>\n', '<<< Faultless! >>>\n', '<<< Flawless Victory! >>>\n']

c = ['<< Acceptable >>\n', '<< Satisfactory>> \n', '<< Sound >>\n', '<< Nice >>\n', '<< OK >>\n', '<< Neat >>\n', '<< Commendable >>\n']

f = ['-Try Harder\n', '-Below Par\n', '-Keep Trying\n', '-You Can Do Better Than That!\n', '-Inadequate\n', '-Malapropos\n']

# prompt
p = ">>> "


def root():
# begin game
    os.system('cls' if os.name == 'nt' else 'clear')
    global user_name
    print "\nHello and welcome to \"PyGrimmage\": a syntactic review of the Python programming language! Please enter your name to continue, or type \"quit\" to return from whence you came:\n"
    user_name = raw_input('ENTER NAME >>> ')
    if user_name.lower().startswith("quit"):
        exit(0)
    else:
        start()


def start():
# start menu - choose where to go next
    
    print "\n%s, would you like to review formatters, keywords, data types, string escape sequences, or operators? (Type \"quit\" to exit)\n" % user_name
    
    next = raw_input(p)

    if next.lower() == "formatters":
        formatters()
    elif next.lower() == "keywords":
        keywords()
    elif next.lower() == "data types":
        data_types()
    elif next.lower() == "string escape sequences":
        string_escape_sequences()
    elif next.lower() == "operators":
        operators()
    elif next.lower().startswith("quit"):
        exit(0)
    else:
        print "\n-Try again-"
        start()


def formatters():
# formatters func
    os.system('cls' if os.name == 'nt' else 'clear')
    score = 0
    print "\nYou have entered \"formatters\". Type the correct formatter to answer each question.\n"
    
# q1
    q1 = raw_input("Signed integer decimal: ")
    if q1 == '%d':
        print random.choice(correct)
        score += 1
    else:
        print random.choice(incorrect)
        print "Correct Answer: %d\n"
        
# q2
    q2 = raw_input("Signed octal value: ")
    if q2 == '%o':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: %o\n"
        
# q3
    q3 = raw_input("Signed hexadecimal (lowercase): ")
    if q3 == '%x':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: %x\n"

# q4    
    q4 = raw_input("Signed hexadecimal (uppercase): ")
    if q4 == '%X':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: %X\n" 
 
 # q5   
    q5 = raw_input("Floating point exponential format (lowercase): ")
    if q5 == '%e':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: %e\n" 

# q6    
    q6 = raw_input("Floating point exponential format (uppercase): ")
    if q6 == '%E':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: %E\n"

# q7
    q7 = raw_input("Floating point decimal format: ")
    if q7 == '%F' or q7 == '%f':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: %F\n"

# q8     
    q8 = raw_input("Floating point format. Uses lowercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise: ")
    if q8 == '%g':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: %g\n"

# q9 
    q9 = raw_input("Floating point format. Uses uppercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise: ")
    if q9 == '%G':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: %G\n"

# q10
    q10 = raw_input("Single character (accepts integer or single character string): ")
    if q10 == '%c':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: %c\n"

# q11
    q11 = raw_input("String (converts any Python object using repr()): ")
    if q11 == '%r':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: %r\n"

# q12
    q12 = raw_input("String (converts any Python object using str()): ")
    if q12 == '%s':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: %s\n"

# q13    
    q13 = raw_input("No argument is converted, results in a '%' character in the result: ")
    if q13 == '%%':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: %%\n"
        
# score        
    print "\n---You answered", str(score) + "/13 correctly", str(user_name)
    if score == 13:
        print random.choice(a)
    elif score > 10:
        print random.choice(c)
    else:
        print random.choice(f)
    
    print "\n###############  - NOW RETURNING TO START MENU - ###############\n\n\n"
    
    start()
        
       
def keywords():
    # keywords func
    os.system('cls' if os.name == 'nt' else 'clear')
    score = 0
    print "\nYou are now in the \"keywords\" section. I was originally going to make this a multiple-choice quiz, but I couldn't dispossess you from the joy of learning. Insert the keyword that matches the following descriptors.\n"

# q1
    q1 = raw_input("Print to console: ")
    if q1 == 'print':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: print\n"

# q2
    q2 = raw_input("Control the flow of the program (loop): ")
    if q2 == 'while':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: while\n"

# q3
    q3 = raw_input("Iterate over items of a collection in order that they appear: ")
    if q3 == 'for':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: for\n"
        
# q4
    q4 = raw_input("Interrupt the (loop) cycle, if needed: ")
    if q4 == 'break':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: break\n"
        
# q5
    q5 = raw_input("Used to interrupt the current cycle, without jumping out of the whole cycle. New cycle will begin: ")
    if q5 == 'continue':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: continue\n"
        
# q6
    q6 = raw_input("Used to determine which statements are going to be executed, creates branch: ")
    if q6 == 'if':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: if\n"
        
# q7
    q7 = raw_input("Stands for else if. If the first test evaluates to False, then it continues with the next one: ")
    if q7 == 'elif':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: elif\n"
        
# q8
    q8 = raw_input("The statement after the else keyword is executed, unless the condition is True: ")
    if q8 == 'else':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: else\n"
        
# q9
    q9 = raw_input("Tests for object identity: ")
    if q9 == 'is':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: is\n"
        
# q10
    q10 = raw_input("Negates a boolean value: ")
    if q10 == 'not':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: not\n"
        
# q11
    q11 = raw_input("All conditions in a boolean expression must be met: ")
    if q11 == 'and':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: and\n"
        
# q12
    q12 = raw_input("At least one condition must be met: ")
    if q12 == 'or':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: or\n"
        
# q13
    q13 = raw_input("Import other modules into a Python script: ")
    if q13 == 'import':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: import\n"
        
# q14
    q14 = raw_input("Gives a module a different alias: ")
    if q14 == 'as':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: as\n"
        
# q15
    q15 = raw_input("Import a specific variable, class or function from a module: ")
    if q15 == 'from':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: from\n"
        
# q16
    q16 = raw_input("Define a user-defined function object: ")
    if q16 == 'def':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: def\n"
        
# q17
    q17 = raw_input("Declare return value of a function: ")
    if q17 == 'return':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: return\n"
        
# q18
    q18 = raw_input("Creates a new anonmyous function: ")
    if q18 == 'lambda':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: lambda\n"
        
# q19
    q19 = raw_input("Access variables defined outside functions: ")
    if q19 == 'global':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: global\n"
        
# q20
    q20 = raw_input("Specifies exception handlers: ")
    if q20 == 'try':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: try\n"
        
# q21
    q21 = raw_input("Catches the exception and executes codes: ")
    if q21 == 'except':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: except\n"
        
# q22
    q22 = raw_input("Is always executed in the end. Used to clean-up resources: ")
    if q22 == 'finally':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: finally\n"
        
# q23
    q23 = raw_input("Create a user-defined exception: ")
    if q23 == 'raise':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: raise\n"
        
# q24
    q24 = raw_input("Deletes objects: ")
    if q24 == 'del':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: def\n"
        
# q25   
    q25 = raw_input("Does nothing: ")
    if q25 == 'pass':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: pass\n"
        
# q26   
    q26 = raw_input("Used for debug purposes: ")
    if q26 == 'assert':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: assert\n"
        
# q27   
    q27 = raw_input("Used to create new user-defined objects: ")
    if q27 == 'class':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: class\n"
        
# q28   
    q28 = raw_input("Executes Python code dynamically: ")
    if q28 == 'exec':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: exec\n"
        
# q29   
    q29 = raw_input("Used with generators: ")
    if q29 == 'yield':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: yield\n"

# score
    print "\n---You answered", str(score) + "/29 correctly", str(user_name)
    if score == 29:
        print random.choice(a)
    elif score > 24:
        print random.choice(c)
    else:
        print random.choice(f)
    
    print "\n###############  - NOW RETURNING TO START MENU - ###############\n\n\n"
    
    start()
        

def data_types():
    # data_type func
    os.system('cls' if os.name == 'nt' else 'clear')
    score = 0
    print "\nThis is the \"Data Types\" category. This section is pretty short. Use a one-word answer for each question. Input the correct data type that goes with its corresponding description:\n"

# q1
    q1 = raw_input("True boolean value: ")
    if q1.lower() == 'true':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: True\n"

# q2
    q2 = raw_input("False boolean value: ")
    if q2.lower() == 'false':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: False\n"
        
# q3
    q3 = raw_input("Data type that means non existent, not known or empty: ")
    if q3.lower() == 'none':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: None\n"
        
# q4
    q4 = raw_input("A data type representing textual data in computer programs: ")
    if q4.lower() == 'strings' or q4.lower() == 'string':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: string\n"
        
# q5
    q5 = raw_input("Fill in the blank - Integer, floating point, and complex ______: ")
    if q5.lower() == 'numbers' or q5.lower() == 'number':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: numbers\n"
        
# q6
    q6 = raw_input("Short for \"floating point number,\" any rational number, usually used with decimals such as 2.8 or 3.14159: ")
    if q6.lower() == 'floats' or q6.lower() == 'float':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: float\n"
        
# q7
    q7 = raw_input("A list without a fixed number of elements. ie x=[1,2,3] note the square brackets, a list: ")
    if q7.lower() == 'lists' or q7.lower() == 'list':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: list\n"

# score
    print "\n---You answered", str(score) + "/7 correctly", str(user_name)
    if score == 7:
        print random.choice(a)
    elif score > 5:
        print random.choice(c)
    else:
        print random.choice(f)
    
    print "\n###############  - NOW RETURNING TO START MENU - ###############\n\n\n"
    
    start()
        

def string_escape_sequences():
    # string_escape_sequence func
    os.system('cls' if os.name == 'nt' else 'clear')
    score = 0
    print "\nWelcome to the \"string escape sequences section\". Type the exact string escape sequence to match the following.\n"
    
# q1
    q1 = raw_input("Backslash (\): ")
    if q1 == '\\\\':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: \\\\ \n"

# q2
    q2 = raw_input("Single quote ('): ")
    if q2 == "\\'":
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: \\' \n"
        
# q3
    q3 = raw_input("Double quote (\"): ")
    if q3 == '\\"':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: \\\" \n"
        
# q4
    q4 = raw_input("ASCII Bell (BEL): ")
    if q4 == '\\a':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: \\a \n"
        
# q5
    q5 = raw_input("ASCII Backspace (BS): ")
    if q5 == '\\b':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: \\b \n"
        
# q6
    q6 = raw_input("ASCII Formfeed (FF): ")
    if q6 == '\\f':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: \\f \n"
        
# q7
    q7 = raw_input("ASCII Linefeed (LF): ")
    if q7 == '\\n':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: \\n \n"
        
# q8
    q8 = raw_input("Character named name in the Unicode database (Unicode only): ")
    if q8 == '\N{name}':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: \\N{name} \n"
        
# q9
    q9 = raw_input("ASCII Carriage Return (CR): ")
    if q9 == '\\r':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: \\r \n"
        
# q10
    q10 = raw_input("ASCII Horizontal Tab (TAB): ")
    if q10 == '\\t':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: \\t \n"
        
# q11
    q11 = raw_input("Character with 16-bit hex value xxxx (Unicode only): ")
    if q11 == '\uxxxx':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: \\uxxxx \n"

# q12
    q12 = raw_input("Character with 32-bit hex value xxxxxxxx (Unicode only: ")
    if q12 == '\Uxxxxxxxx':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: \\Uxxxxxxxx \n"

# q13
    q13 = raw_input("ASCII Vertical Tab (VT): ")
    if q13 == '\\v':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: \\v \n"

# q14
    q14 = raw_input("Character with octal value ooo: ")
    if q14 == '\ooo':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: \\ooo \n"

# q15
    q15 = raw_input("Character with hex value hh: ")
    if q15 == '\\xhh':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: \\xhh \n"
        
# score
    print "\n---You answered", str(score) + "/15 correctly", str(user_name)
    if score == 15:
        print random.choice(a)
    elif score > 11:
        print random.choice(c)
    else:
        print random.choice(f)
    
    print "\n###############  - NOW RETURNING TO START MENU - ###############\n\n\n"
    
    start()
        

def operators():
    # operators func
    os.system('cls' if os.name == 'nt' else 'clear')
    score = 0
    print "\n\"Operators\". Go! Gogogogogo!!!\n"
    
# q1
    q1 = raw_input("addition: ")
    if q1 == '+':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: +\n"

# q2
    q2 = raw_input("subtraction: ")
    if q2 == '-':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: -\n"
# q3
    q3 = raw_input("multiplication: ")
    if q3 == '*':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: *\n"
# q4
    q4 = raw_input("exponentiation: ")
    if q4 == '**':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: **\n"
# q5
    q5 = raw_input("division: ")
    if q5 == '/':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: /\n"
# q6
    q6 = raw_input("divide with integral result (discard remainder): ")
    if q6 == '//':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: //\n"
# q7
    q7 = raw_input("modulus: ")
    if q7 == '%':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: %\n"
# q8
    q8 = raw_input("less than: ")
    if q8 == '<':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: <\n"
# q9
    q9 = raw_input("greater than: ")
    if q9 == '>':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: >\n"
# q10
    q10 = raw_input("less than equal: ")
    if q10 == '<=':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: <=\n"
# q11
    q11 = raw_input("greater than equal: ")
    if q11 == '>=':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: >=\n"
# q12
    q12 = raw_input("equal to: ")
    if q12 == '==':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: ==\n"
# q13
    q13 = raw_input("not equal: ")
    if q13 == '!=':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: !=\n"

# q14
    q14 = raw_input("decorator: ")
    if q14 == '@':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: @\n"
# q15
    q15 = raw_input("separate list items: ")
    if q15 == ',':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: ,\n"

# q16
    q16 = raw_input("assignment: ")
    if q16 == '=':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: =\n"

# q17
    q17 = raw_input("increment by addition operator): ")
    if q17 == '+=':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: +=\n"
        
# q18
    q18 = raw_input("increment by subtraction operator): ")
    if q18 == '-=':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: -=\n"
        
# q19
    q19 = raw_input("increment by multiplication operator: ")
    if q19 == '*=':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: *=\n"
        
# q20
    q20 = raw_input("increment by division operator: ")
    if q20 == '/=':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: /=\n"
        
# q21
    q21 = raw_input("increment by division with integral result operator: ")
    if q21 == '//=':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: //=\n"

# q22
    q22 = raw_input("increment by exponentiation  operator: ")
    if q22 == '**=':
        print random.choice(correct)
        score +=1
    else:
        print random.choice(incorrect)
        print "Correct Answer: **=\n"

# score
    print "\n---You answered", str(score) + "/22 correctly", str(user_name)
    if score == 22:
        print random.choice(a)
    elif score > 18:
        print random.choice(c)
    else:
        print random.choice(f)
    
    print "\n###############  - NOW RETURNING TO START MENU - ###############\n\n\n"
    
    start()
    
    
root()
