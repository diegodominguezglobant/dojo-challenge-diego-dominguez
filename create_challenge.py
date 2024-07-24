import argparse
import os
from datetime import datetime

parser = argparse.ArgumentParser(description='Create a directory and file for a challenge.')
parser.add_argument('-n', '--name', type=str, help='Challenge Name', required=True)

args = parser.parse_args()
func_name = args.name
folder_name = "".join([x.capitalize() for x in func_name.split("_")])

month, year = datetime.now().strftime("%b-%Y").split("-")
print(f"Date: {month}-{year}")

folder_year = f"Y{year}"
if not folder_year in os.listdir():
    print(f"There is no folder for year {year}, creating one...")
    os.mkdir(folder_year)
    print(f"Folder '{folder_year}' created")

if not month in os.listdir(folder_year):
    print(f"There is no folder for month {month}, creating one...")
    os.mkdir(f"{folder_year}/{month}")
    print(f"Folder '{folder_year}/{month}' created")

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
python3 -m unittest {folder_year}/{month}/{folder_name}/test_challenge.py
```

"""
    )

with open(f"{folder_name}/challenge.py", "w") as python_file:
    python_file.write(
        f"""def {func_name}():
    return 3
"""
        )

with open(f"{folder_name}/test_challenge.py", "w") as pytesting_file:
    pytesting_file.write(
        f"""import unittest

from {folder_year}.{month}.{folder_name}.challenge import {func_name}


class Test{folder_name}(unittest.TestCase):
    def test_{func_name}(self):

        ans = {func_name}()
        expected_ans = 3
        self.assertEqual(ans, expected_ans)

if __name__ == '__main__':
    unittest.main()

"""
        )
print("Done with no errors.")
print(
    f"""
dojo-challenge-diego-dominguez/
├── {folder_year}/
│   ├── {month}/
│   │   ├── {folder_name}/
│   │   │   ├── README.md
│   │   │   ├── test_challenge.py
│   │   │   └── challenge.py
├── create_challenge.py
└── README.md
"""
)

print(f"Git url: https://github.com/U9-GLO297-CW/dojo-challenge-diego-dominguez/tree/main/{folder_year}/{month}/{folder_name}")
