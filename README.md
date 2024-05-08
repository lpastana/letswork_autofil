
# Letswork Timesheet Autofil

This project is designed to automate the process of filling out timesheets using Selenium and PyAutoGUI. It simplifies the routine task of time entry, ensuring accuracy and efficiency.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

To install the project, follow these steps:

1. Clone the repository to your local machine:
    ```
    git clone https://github.com/your-username/letswork_autofil.git
    ```

2. Navigate to the project directory:
    ```
    cd letswork_autofil
    ```

3. Install the project dependencies using pipenv:
    ```
    pipenv install
    ```

4. Create a `.env` file in the project root directory and add your username and password:
    ```
    USERNAME=your-username
    PASSWORD=your-password
    ```

    Now the environment is ready!

    Note: Make sure to replace `your-username` and `your-password` with your actual credentials.

## Usage

The script provides the following commands to manage the autofill process:

- To fill the timesheet for a specified date range:
  ```
  python main.py -s <start-date> -e <end-date>
  ```

  ```
  python main.py --start-date <start-date> --end-date <end-date>
  ```

- To fill the timesheet for the current day:
  ```
  python main.py --today
  ```

- To view help for command usage:
  ```
  python main.py --help
  ```

Example scripts in `Pipfile`:

- `gap`: Fill timesheet for a given date range
    ```
    pipenv run gap -s <start-date> -e <end-date>
    ```
    ```
    pipenv run gap --start-date <start-date> --end-date <end-date>
    ```

- `today`: Fill timesheet for today
    ```
    pipenv run today
    ```

- `help`: Display help
    ```
    pipenv run help
    ```

## Features

- **Automated Timesheet Filling**: Automatically fills timesheets for specified dates.
- **Custom Date Ranges**: Ability to specify start and end dates for timesheet filling.
- **Immediate Fill Option**: Option to fill the timesheet immediately for the current day.

## Contributing

Contributions are welcomed from everyone! If you have suggestions on how to improve this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
