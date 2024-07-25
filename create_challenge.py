import argparse
import os
from datetime import datetime

parser = argparse.ArgumentParser(description='Create a directory and file for a challenge.')
parser.add_argument('-n', '--name', type=str, help='Challenge Name (separated with underscore (_))', required=True)
parser.add_argument('-nd', '--not-dojo', action="store_false", help='Is challenge for dojo?')

args = parser.parse_args()
func_name = args.name
dojo = args.not_dojo
folder_name = "".join([x.capitalize() for x in func_name.split("_")])

month, year = datetime.now().strftime("%b-%Y").split("-")
print(f"Date: {month}-{year}")

print(f"Creating challenge for dojo: {dojo}")
if not dojo:
    if not "NotDojo" in os.listdir():
        os.mkdir("NotDojo")
    os.chdir("NotDojo")

if not "tests" in os.listdir():
    print(f"There is no folder for tests, creating one...")
    os.mkdir("tests")
    print(f"Folder 'tests' created")

folder_year = f"Y{year}"
if not folder_year in os.listdir():
    print(f"There is no folder for year {year}, creating one...")
    os.mkdir(folder_year)
    print(f"Folder '{folder_year}' created")

if not month in os.listdir(folder_year):
    print(f"There is no folder for month {month}, creating one...")
    os.mkdir(f"{folder_year}/{month}")
    print(f"Folder '{folder_year}/{month}' created")

# Creating tests file before changing directory
with open(f"tests/test_{func_name}.py", "w") as pytesting_file:
    pytesting_file.write(
        f"""import unittest

from {folder_year}.{month}.{folder_name}.challenge import {func_name}


class Test{folder_name}(unittest.TestCase):
    def test_{func_name}(self):
        expected_ans = 3

        ans = {func_name}()

        self.assertEqual(ans, expected_ans)

if __name__ == '__main__':
    unittest.main()

"""
        )

# Chaniging directory to create challenge file and README.md
os.chdir(f"{folder_year}/{month}")

if folder_name in os.listdir():
    raise Exception("Challenge already exists.")

print(f"Creating {folder_name}/")
os.mkdir(folder_name)

with open(f"{folder_name}/README.md", 'w') as readme_file:
    readme_file.write(
        f"""# {" ".join([x.capitalize() for x in func_name.split("_")])}

### Description:
[Add Description]
# Testing
### Run tests:
```sh
python3 -m unittest discover -s tests
```

"""
    )

with open(f"{folder_name}/challenge.py", "w") as python_file:
    python_file.write(
        f"""def {func_name}():
    return 3
"""
        )

print("Done with no errors.")
print(
    f"""
dojo-challenge-diego-dominguez/
├── {folder_year}/
│   ├── {month}/
│   │   ├── {folder_name}/
│   │   │    ├── README.md
│   │   │    ├── challenge.py
│   ├──tests/└── test_{func_name}.py
├── create_challenge.py
└── README.md
"""
)

print(f"Git url: https://github.com/U9-GLO297-CW/dojo-challenge-diego-dominguez/tree/main/{folder_year}/{month}/{folder_name}")
