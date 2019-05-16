# 1. Prerequisites

Testing your code is really important. It allows you to verify if a newly added feature doesn't break another, and also the check the behavior of your code.

The program used to run unit tests is *pytest*. It enhances the behavior of the *unittest* standard library in Python.

## 1. Install requirements

Using pip (or pip3 depending on your use case), install the following packages :
- pytest
- pytest-cov

## 2. Setup environment

To use pytest conveniently, you need to setup some environment variables. You'll need to setup these every time you open a new terminal (or setup these in your bashrc or zshrc). You can type the following command : 
```
export PYTHONPATH=$PYTHONPATH:.:./Parser
```

# 2. Run tests

## 1. Only run tests

To launch the testing using pytest, just enter the following command at the root of the project : 
```
pytest
```
It will run the tests, and show errors when a test doesn't succeed as intended.

## 2. Run tests with coverage

You will also need to check the coverage of your tests. The coverage is a percentage of code covered by your tests. It can be useful to spot useless chunks of code (impossible to reach for exemple). Your goal is to achieve **100% coverage** on each file.

To run the tests with coverage enabled, type this : 
```
pytest --cov=. --cov-report=term-missing --cov-report=xml 
```

This command will run the tests, enable the coverage and report it to both the terminal and an xml file located at the root.


# 3. Write tests

Run tests is one thing, write tests is another. If you doubt on something, you can refer to the documentation of pytest and unittest, or check in already done test files.

## 1. Conventions

By convention, one file of code equals one file of test. When you want to add unit tests for a file, create a Tests folder in the same folder as the file. You can refer to the following tree : 
```
.
└── Src
    ├── program.py
    ├── Misc
    │   ├── dataExtraction.py
    │   └── Tests
    │       └── test_dataExtraction.py
    └── Tests
        └── test_program.py
```

## 2. Writing

To check the norm regarding tests writing, please check an already done file.