# Translation App

## Description

The **Translation App** is a basic command-line tool built with Python that allows users to translate words or short phrases between English and French. This application is perfect for beginners who want to practice Python while learning about dictionaries, functions, and user input handling.

The app provides a simple, interactive interface where users can:
- Translate from **English to French**.
- Translate from **French to English**.
- Exit the application when finished.

---

## Features

- **Two-way Translation**: Easily switch between English-to-French and French-to-English translations.
- **Custom Dictionary**: Includes a predefined dictionary of common words and phrases for quick translations.
- **User-Friendly Interface**: Simple menu system for seamless interaction.
- **Error Handling**: Notifies users when a word or phrase is not found in the dictionary.

---

## How It Works

1. The user chooses one of the following options from the main menu:
    - Translate from **English to French**.
    - Translate from **French to English**.
    - Exit the application.
2. The user enters a word or short phrase in the desired language.
3. The app checks the predefined dictionary and returns the translation if found.
4. If the translation is unavailable, the app displays a message indicating that the translation is not found.

---

## Requirements

- Python 3.6 or later.

---

## Installation

1. Clone this repository or download the project files:
   ```bash
   git clone https://github.com/your-username/translation-app.git
   ```
2. Navigate to the project directory:
   ```bash
   cd translation-app
   ```
3. Run the app:
   ```bash
   python main.py
   ```

---

## Usage

1. Launch the program:
   ```bash
   python main.py
   ```
2. Follow the on-screen prompts to:
    - Translate words or phrases.
    - Switch between English-to-French and French-to-English translations.
    - Exit the application.

### Example

```
Bienvenue dans le Traducteur Basique!
Options disponibles:
1. Traduire de l'anglais au français
2. Traduire du français à l'anglais
3. Quitter

Choisissez une option (1, 2, ou 3) : 1
Entrez un mot ou une phrase en anglais : hello
Traduction en français : bonjour
```

---

## Future Improvements

- **Translation of full sentences**: Add functionality to handle sentences by splitting them into words and translating each one.
- **Support for additional languages**: Extend the dictionary to include other languages such as Spanish or German.
- **File-based dictionary storage**: Store translations in a JSON or database file to allow for dynamic updates.
- **Graphical User Interface (GUI)**: Build a more user-friendly experience using frameworks like Tkinter or PyQt.

---

## Contributing

If you'd like to contribute to this project:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/new-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/new-feature
   ```
5. Create a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Author

Developed by **Konan Bernard**  
