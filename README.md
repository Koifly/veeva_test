# veeva_test

## Veeva coding challenge

Written and tested on Pop!\_OS (based on Ubuntu).

How to run the weather script (Use Python 3.7+):

Clone repo:
```sh
git clone git@github.com:Koifly/veeva_test.git
cd veeva_test
```

Set up python venv in local repo (if on Windows I suggest to use Bash shell):
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run the script:
```sh
python -m script.main -z [ZIP code] -k [API key]
```

To run the tests:
```sh
pytest
```