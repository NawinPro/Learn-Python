import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QPushButton, QTextEdit
from PyQt5.QtCore import Qt

# Sample dictionary containing topics and their corresponding codes
topics_and_codes = {
    # Python Basics
    "Hello World": "# This program prints 'Hello, World!'\nprint('Hello, World!')",
    "Variables": "# This program demonstrates variable usage\nname = 'John'\nprint('Hello, ' + name)",
    "Conditional Statements": "# This program uses if-else statement to check age\nage = 25\nif age >= 18:\n    print('You are an adult.')\nelse:\n    print('You are a minor.')",
    "Loops": "# This program demonstrates for loop\nfor i in range(5):\n    print(i)",
    "Functions": "# This program defines and calls a function\ndef greet(name):\n    print('Hello, ' + name)\ngreet('Alice')",

    # Common Life Problems
    "Armstrong Number": "# This program checks if a number is an Armstrong number\ndef is_armstrong(num):\n    digits = [int(digit) for digit in str(num)]\n    num_digits = len(digits)\n    armstrong_sum = sum(digit ** num_digits for digit in digits)\n    return num == armstrong_sum\n\nprint(is_armstrong(153))",
    "Printing Patterns": "# This program prints star patterns\nn = 5\n# Star Pattern 1\nfor i in range(1, n+1):\n    print('* ' * i)\n# Star Pattern 2\nfor i in range(n, 0, -1):\n    print('* ' * i)\n# Star Pattern 3\nfor i in range(n):\n    print(' ' * (n-i-1) + '* ' * (i+1))\n# Star Pattern 4\nfor i in range(n):\n    print(' ' * i + '* ' * (n-i))",
    "Odd or Even": "# This program checks if a number is odd or even\ndef check_odd_even(num):\n    if num % 2 == 0:\n        return 'Even'\n    else:\n        return 'Odd'\n\nprint(check_odd_even(7))",
    "Printing Date and Time": "# This program prints the current date and time\nfrom datetime import datetime\n\ncurrent_datetime = datetime.now()\nprint(current_datetime)",

    # File Handling with Functions
    "File Handling": "# This program demonstrates file handling\nwith open('example.txt', 'w') as file:\n    file.write('Hello, File!')\nwith open('example.txt', 'r') as file:\n    print(file.read())",
    "Write to File": "# This program writes content to a file\ndef write_to_file(filename, content):\n    with open(filename, 'w') as file:\n        file.write(content)\n\nwrite_to_file('example.txt', 'Hello, File!')",
    "Read from File": "# This program reads content from a file\ndef read_from_file(filename):\n    with open(filename, 'r') as file:\n        return file.read()\n\nprint(read_from_file('example.txt'))",

    # Projects
    "Simple GUI Creation Codes": "# This program demonstrates creating a simple GUI using tkinter\nimport tkinter as tk\n\nroot = tk.Tk()\nroot.title('Simple GUI')\n\n# Your GUI elements and logic here...\n\nroot.mainloop()",
    "Calculator Project": "# This program demonstrates a basic calculator project\ndef add(x, y):\n    return x + y\n\ndef subtract(x, y):\n    return x - y\n\ndef multiply(x, y):\n    return x * y\n\ndef divide(x, y):\n    return x / y\n\n# Your calculator GUI and logic here...",
    "Classes and Objects": "# This program defines a class and creates an object\nclass Person:\n    def __init__(self, name, age):\n        self.name = name\n        self.age = age\n\np1 = Person('John', 25)\nprint(p1.name)",

    # Printing Star Patterns
    "Star Pattern 1": "# This program prints a right-angled triangle of stars\nn = 5\nfor i in range(1, n+1):\n    print('* ' * i)",
    "Star Pattern 2": "# This program prints an inverted right-angled triangle of stars\nn = 5\nfor i in range(n, 0, -1):\n    print('* ' * i)",
    "Star Pattern 3": "# This program prints a pyramid of stars\nn = 5\nfor i in range(n):\n    print(' ' * (n-i-1) + '* ' * (i+1))",
    "Star Pattern 4": "# This program prints a diamond pattern of stars\nn = 5\nfor i in range(n):\n    print(' ' * (n-i-1) + '* ' * (i+1))\nfor i in range(n-1, 0, -1):\n    print(' ' * (n-i) + '* ' * i)",

    # Number Patterns
    "Number Pattern 1": "# This program prints a number pattern\nn = 5\nfor i in range(1, n+1):\n    print(str(i) * i)",
    "Number Pattern 2": "# This program prints another number pattern\nn = 5\nfor i in range(1, n+1):\n    print(' '.join(str(j) for j in range(1, i+1)))",
    # Add more topics and codes here...
}

class PythonProgramApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Learn Python Basics With Python ! ")
        self.setGeometry(200, 200, 800, 600)
        self.setStyleSheet("background-color: #2b2b2b; color: #FFFFFF;")

        layout = QVBoxLayout()

        # Create a combo box to display topics
        self.topic_combo = QComboBox(self)
        self.topic_combo.addItems(topics_and_codes.keys())
        self.topic_combo.currentIndexChanged.connect(self.display_code)
        layout.addWidget(self.topic_combo)

        # Create a button with sky blue background
        self.show_code_button = QPushButton("Show Code", self)
        self.show_code_button.setStyleSheet("background-color: #87CEEB; color: #FFFFFF;")
        self.show_code_button.clicked.connect(self.display_code)
        layout.addWidget(self.show_code_button)

        # Create a text area to display code
        self.code_text = QTextEdit(self)
        self.code_text.setStyleSheet("background-color: #1e1e1e; color: #FFFFFF;")
        layout.addWidget(self.code_text)

        self.setLayout(layout)

    def display_code(self):
        selected_topic = self.topic_combo.currentText()
        self.code_text.setPlainText(topics_and_codes[selected_topic])

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Apply Fusion style to get dark mode (comment this line if you prefer the default style)
    app.setStyle("Fusion")

    window = PythonProgramApp()
    window.show()

    sys.exit(app.exec_())
