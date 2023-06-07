# replace_last_backslash

Python package for replacing the last backslash '\\' in a path string with a forward slash '/'.

## Installation

You can install the development version of the `replace_last_backslash` package from GitHub by following these steps:

1. Clone the repository or download the source code from GitHub:

```bash
git clone https://github.com/your-username/replace_last_backslash.git
```

Replace `your-username` with your GitHub username.

2. Navigate to the cloned or downloaded directory:

```bash
cd replace_last_backslash
```

3. Install the package and its dependencies with [poetry](https://python-poetry.org/):

```bash
poetry install
```

## Usage

Import the replace_last_backslash function from the replace_last_backslash module and use it in your Python scripts as follows:

```python
from replace_last_backslash import replace_last_backslash

path = "C:the\\string\\in\\this\\path\\to\\fix.txt"
modified_path = replace_last_backslash(path)
print(modified_path) # Output: "C:the\\string\\in\\this\\path\\to/fix.txt"
```

The replace_last_backslash function takes a path string as input and returns the modified path string with the last backslash replaced by a forward slash. If the path does not contain any backslashes, it is returned as is.

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).

