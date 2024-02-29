# dojo-challenge-diego-dominguez
## create_challenge.py
This file will create basic structure directory for starting point.
The file will create a directory from current year and month, then will add Folder with name of the challenge and within that folder there will be README file, 2 python files, one for challenge code, other one for testing.
```
dojo-challenge-diego-dominguez/
├── Y[current_year]/
│   ├── [current_month]/
│   │   ├── [challenge_name]/
│   │   │   ├── README.md
│   │   │   ├── test_challenge.py
│   │   │   └── challenge.py
├── create_challenge.py
└── README.md
```

### Run
The file will receive a name. Name should be in snake case.<br>
<b>FILE NAME SHOULD NOT CONTAIN SPACES</b>. <br>
For new challenge just run:
```sh
python3 create_challenge -n [challenge_name]
```

## README file
Each challenge folder will have a `README.md` file, there is not much there to explain other than the command to be used on terminal to run the tests
