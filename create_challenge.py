import argparse
import os
from datetime import datetime

parser = argparse.ArgumentParser(description='Create a directory and file for a challenge.')
parser.add_argument('-n', '--name', type=str, help='Challenge Name', required=True)

args = parser.parse_args()
func_name = args.name
folder_name = "".join([x.capitalize() for x in func_name.split("_")])

month, year = datetime.now().strftime("%b-%Y").split("-")

folder_year = f"Y{year}"
if not folder_year in os.listdir():
    os.mkdir(folder_year)

if not month in os.listdir(folder_year):
    os.mkdir(month)

os.chdir(f"{folder_year}/{month}")

if folder_name in os.listdir():
    raise Exception("Challenge already exists.")

os.mkdir(folder_name)

with open(f"{folder_name}/README.md", 'w') as readme_file:
    readme_file.write(
        f"""
# Testing

### Run:
```sh
python3 -m unittest {folder_year}/{month}/{folder_name}/test_challenge.py
```

"""
    )

with open(f"{folder_name}/challenge.py", "w") as python_file:
    python_file.write(
        f"""
def {func_name}():
    return 3
"""
        )

with open(f"{folder_name}/test_challenge.py", "w") as pytesting_file:
    pytesting_file.write(
        f"""
import unittest

from {folder_year}.{month}.{folder_name}.challenge import {func_name}


class Test{folder_name}(unittest.TestCase):
    def test_{func_name}(self):

        ans = {func_name}()
        self.assertEqual(ans, 3)

if __name__ == '__main__':
    unittest.main()

"""
        )
