# Python Programming Syllabus

## Table of Contents
- [Module 1: Introduction to Python](#module-1-introduction-to-python)
- [Module 2: Basic Python Syntax](#module-2-basic-python-syntax)
- [Module 3: Data Structures](#module-3-data-structures)
- [Module 4: Functions and Modules](#module-4-functions-and-modules)
- [Module 5: Control Flow](#module-5-control-flow)
- [Module 6: File Handling](#module-6-file-handling)
- [Module 7: Error Handling and Exceptions](#module-7-error-handling-and-exceptions)
- [Module 8: Object-Oriented Programming (OOP)](#module-8-object-oriented-programming-oop)
- [Module 9: Advanced Topics](#module-9-advanced-topics)
- [Module 10: Final Project & Review](#module-10-final-project--review)
- [Assessments](#assessments)
- [References](#references)

---

## Module 1: Introduction to Python

- Overview — [README](01_Introduction_to_Python/README.md)
1. **Overview of Python**
   - What is Python? — see [README](01_Introduction_to_Python/README.md)
   - History & Evolution — see [README](01_Introduction_to_Python/README.md)
   - Features — see [README](01_Introduction_to_Python/README.md)
   - Applications — see [README](01_Introduction_to_Python/README.md)
2. **Setting Up the Environment**
   - Installing Python — see [README](01_Introduction_to_Python/README.md)
   - IDEs (VS Code / PyCharm) — see [README](01_Introduction_to_Python/README.md)
   - Interpreter & Interactive Mode — see [README](01_Introduction_to_Python/README.md)
   - Your first script — [`helloworld.py`](01_Introduction_to_Python/helloworld.py)

---

## Module 2: Basic Python Syntax

- Overview — [README](02_Basic_Python_Syntax/README.md)
1. **Python Basics**
   - Syntax & Indentation — [`syntaxandindentation.py`](02_Basic_Python_Syntax/syntaxandindentation.py)
   - Comments — [`commentlines.py`](02_Basic_Python_Syntax/commentlines.py)
   - Print & String Formatting — [`printstatement.py`](02_Basic_Python_Syntax/printstatement.py), [`stringformatting.py`](02_Basic_Python_Syntax/stringformatting.py)
2. **Variables and Data Types**
   - Variables & Assignments — [`variablesanddatatypes.py`](02_Basic_Python_Syntax/variablesanddatatypes.py)
   - Basic Types (int, float, str, bool) — [`variablesanddatatypes.py`](02_Basic_Python_Syntax/variablesanddatatypes.py)
   - Type Conversion / Casting — [`variablesanddatatypes.py`](02_Basic_Python_Syntax/variablesanddatatypes.py)
   - Basic Input/Output — [`inputandoutput.py`](02_Basic_Python_Syntax/inputandoutput.py)
3. **Basic Operators**
   - Arithmetic / Assignment — [`basicoperators.py`](02_Basic_Python_Syntax/basicoperators.py)
   - Comparison — [`basicoperators.py`](02_Basic_Python_Syntax/basicoperators.py)
   - Logical — [`logicaloperators.py`](02_Basic_Python_Syntax/logicaloperators.py)

---

## Module 3: Data Structures

- Overview — [README](03_Data_Structures/README.md)
1. **Lists**
   - Lists, slicing, methods — [`sequencetype.py`](03_Data_Structures/sequencetype.py), [`methods.py`](03_Data_Structures/methods.py)
2. **Tuples**
   - Tuples & operations — [`sequencetype.py`](03_Data_Structures/sequencetype.py)
3. **Dictionaries**
   - Basics & methods — [`dictionary.py`](03_Data_Structures/dictionary.py), [`methods.py`](03_Data_Structures/methods.py)
4. **Sets**
   - Basics & operations — [`setdatatype.py`](03_Data_Structures/setdatatype.py)
5. **Numeric & Boolean**
   - Numeric types — [`numeric.py`](03_Data_Structures/numeric.py)
   - Boolean logic — [`boolean.py`](03_Data_Structures/boolean.py)
6. **Reference Image**
   - Data structures diagram — [`pythondatastructures.png`](03_Data_Structures/pythondatastructures.png)

---

## Module 4: Control Flow

1. **Conditional Statements** — [README](04_Control_Flow/README.md)
   - `if` / `elif` / `else` — [`ifelifelse.py`](04_Control_Flow/1_Conditional_Statements/ifelifelse.py), [`ifelse.py`](04_Control_Flow/1_Conditional_Statements/ifelse.py)
   - Nested Conditions — [`nestedconditions.py`](04_Control_Flow/1_Conditional_Statements/nestedconditions.py)
   - Ternary Operator — [`ternaryoperation.py`](04_Control_Flow/1_Conditional_Statements/ternaryoperation.py)
2. **Loops**
   - `for` loops — [`forloop.py`](04_Control_Flow/2_Loops/forloop.py)
   - `while` loops — [`whileloop.py`](04_Control_Flow/2_Loops/whileloop.py)
   - `break` / `continue` — [`breakandcontinue.py`](04_Control_Flow/2_Loops/breakandcontinue.py)
   - Ranges — [`ranges.py`](04_Control_Flow/2_Loops/ranges.py)
3. **Comprehensions**
   - List Comprehensions — [`listcomprehensions.py`](04_Control_Flow/3_Comprehensions/listcomprehensions.py)
   - Dictionary Comprehensions — [`dictcomprehensions.py`](04_Control_Flow/3_Comprehensions/dictcomprehensions.py)
   - Set Comprehensions — [`setcomprehensions.py`](04_Control_Flow/3_Comprehensions/setcomprehensions.py)

---

## Module 5: Functions and Modules

- Overview — [README](04_Control_Flow/README.md)
1. **Functions**
   - Defining & Calling — [`definingandcalling.py`](05_Functions_and_Modules/Functions/definingandcalling.py)
   - Parameters & Arguments — [`parametersandarguments.py`](05_Functions_and_Modules/Functions/parametersandarguments.py)
   - Return Values / Scope / Lambda — [`definingandcalling.py`](05_Functions_and_Modules/Functions/definingandcalling.py)
2. **Modules and Packages**
   - Importing Modules — [`importingmodules.py`](05_Functions_and_Modules/Modules_and_Packages/Builtin_Modules/importingmodules.py)
   - Aliasing Imports — [`alias.py`](05_Functions_and_Modules/Modules_and_Packages/Builtin_Modules/alias.py)
   - Importing Packages — [`importingpackages.py`](05_Functions_and_Modules/Modules_and_Packages/Builtin_Modules/importingpackages.py)
   - Custom Package Example — [`banking/`](05_Functions_and_Modules/Modules_and_Packages/Custom_Modules/banking/)
     - `__init__` — [`__init__.py`](05_Functions_and_Modules/Modules_and_Packages/Custom_Modules/banking/__init__.py)
     - Accounts package — [`accounts/`](05_Functions_and_Modules/Modules_and_Packages/Custom_Modules/banking/accounts/)
       - [`__init__.py`](05_Functions_and_Modules/Modules_and_Packages/Custom_Modules/banking/accounts/__init__.py)
       - [`accountinfo.py`](05_Functions_and_Modules/Modules_and_Packages/Custom_Modules/banking/accounts/accountinfo.py)
       - [`credit.py`](05_Functions_and_Modules/Modules_and_Packages/Custom_Modules/banking/accounts/credit.py)
       - [`debit.py`](05_Functions_and_Modules/Modules_and_Packages/Custom_Modules/banking/accounts/debit.py)
   - Test Modules — [`testmodules.py`](05_Functions_and_Modules/Modules_and_Packages/Custom_Modules/testmodules.py), [`testmodulefromlibfolder.py`](05_Functions_and_Modules/Modules_and_Packages/Custom_Modules/testmodulefromlibfolder.py)

---

## Module 6: File Handling

1. **Reading & Writing Files** — [`filehandling.py`](06_File_Handling/filehandling.py), [`fileoperations.py`](06_File_Handling/fileoperations.py)
   - Notes — [`file_handling_notes.md`](06_File_Handling/file_handling_notes.md)
   - Examples — [`sample1.txt`](06_File_Handling/sample1.txt), [`sample3.txt`](06_File_Handling/sample3.txt)
2. **File Paths & Utilities**
   - `os` / `pathlib` usage — [`fileoperations.py`](06_File_Handling/fileoperations.py)

---

## Module 7: Error Handling and Exceptions

1. **Exception Handling**
   - `try` / `except` / `else` / `finally` — [`errorhandling.py`](07_Error_Handling_and_Exceptions/errorhandling.py)
   - Raising Exceptions — [`raiseexceptions.py`](07_Error_Handling_and_Exceptions/raiseexceptions.py)
2. **Common Exceptions**
   - Notes & examples — [`error_handling_and_exceptions_notes.md`](07_Error_Handling_and_Exceptions/error_handling_and_exceptions_notes.md)

---

## Module 8: Object-Oriented Programming (OOP)

- Overview Notes — [`oop_notes.md`](08_Object_Oriented_Programming/oop_notes.md)
1. **Basic Concepts**
   - Classes, Objects, Methods — [`basicconcepts.py`](08_Object_Oriented_Programming/basicconcepts.py)
2. **Encapsulation, Inheritance, Polymorphism, Abstraction**
   - Encapsulation — [`encapsulation.py`](08_Object_Oriented_Programming/encapsulation.py)
   - Inheritance — [`inheritance.py`](08_Object_Oriented_Programming/inheritance.py)
   - Polymorphism — [`polymorphism.py`](08_Object_Oriented_Programming/polymorphism.py)
   - Abstraction — [`abstraction.py`](08_Object_Oriented_Programming/abstraction.py)

---

## Module 9: Advanced Topics

1. **Database Connection with MySQL**
   - Notes — [`database_connection_notes.md`](09_Advanced_Topics/1_Database_Connection_with_MySQL/database_connection_notes.md)
   - Code — [`databaseconnection.py`](09_Advanced_Topics/1_Database_Connection_with_MySQL/databaseconnection.py)
2. **Multithreading**
   - Notes — [`multithreading_notes.md`](09_Advanced_Topics/2_Multithreading/multithreading_notes.md)
   - Code — [`multithreading.py`](09_Advanced_Topics/2_Multithreading/multithreading.py)
3. **Iterators and Generators**
   - Notes — [`iterator_and_generator_notes.md`](09_Advanced_Topics/3_Iterators_and_Generators/iterator_and_generator_notes.md)
   - Iterator — [`iterator.py`](09_Advanced_Topics/3_Iterators_and_Generators/iterator.py)
   - Generator — [`generator.py`](09_Advanced_Topics/3_Iterators_and_Generators/generator.py)
4. **Decorators**
   - Notes — [`decorators_notes.md`](09_Advanced_Topics/4_Decorators/decorators_notes.md)
   - Code — [`decorator.py`](09_Advanced_Topics/4_Decorators/decorator.py)
5. **Regular Expressions**
   - Notes — [`regex_notes.md`](09_Advanced_Topics/5_Regular_Expressions/regex_notes.md)
   - Cheat Sheet — [`regular_expressions_cheat_sheet.pdf`](09_Advanced_Topics/5_Regular_Expressions/regular_expressions_cheat_sheet.pdf)
   - Code — [`regex.py`](09_Advanced_Topics/5_Regular_Expressions/regex.py)
6. **JSON and XML Processing**
   - JSON — [`jsonprocessing.py`](09_Advanced_Topics/6_JSON_and_XML_Processing/jsonprocessing.py), [`dict_to_json.json`](09_Advanced_Topics/6_JSON_and_XML_Processing/dict_to_json.json)
   - XML — [`xmlprocessing.py`](09_Advanced_Topics/6_JSON_and_XML_Processing/xmlprocessing.py), [`input_data.xml`](09_Advanced_Topics/6_JSON_and_XML_Processing/input_data.xml)
7. **Advanced Concepts Overview (Async, Memory Mgmt)**
   - Notes — [`async_programming_and_memory_management_notes.md`](09_Advanced_Topics/7_Advanced_Concepts/async_programming_and_memory_management_notes.md)
   - Code — [`asyncandmemorymgmt.py`](09_Advanced_Topics/7_Advanced_Concepts/asyncandmemorymgmt.py)

---

## Module 10: Final Project & Review

1. **Capstone: Personal Finance Manager**
   - Requirements & Notes — [`project_notes.md`](10_Project/project_notes.md)
   - Implementation — [`financemanager.py`](10_Project/financemanager.py)
2. **Review & Q&A**
   - Course-wide revision — see topic READMEs under each module above.

---

## Assessments

- Basics Assessment — [`Assessments/Basic_Assessments/`](Assessments/Basic_Assessments/)
- Coding Exercises — [`Assessment_1.docx`](Assessments/Coding_Exercises/Assessment_1.docx), [`Assessment_2.docx`](Assessments/Coding_Exercises/Assessment_2.docx), [`Assessment_3.docx`](Assessments/Coding_Exercises/Assessment_3.docx)

---

## References

- **Repository Home** — [`README.md`](README.md)
- **Reference Links (Installs, IDEs, docs)** — [`README.md`](README.md)
- **Git / Workflow Notes** — [`GIT_Notes.md`](GIT_Notes.md)
- **License** — [`LICENSE`](LICENSE)
