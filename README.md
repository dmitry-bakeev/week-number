# week-number

This is solution of the test task for the position on Python developer.

## How to test

1. Clone this repo

```bash
# If use https
git clone https://github.com/dmitry-bakeev/week-number.git

# if use ssh
git clone git@github.com:dmitry-bakeev/week-number.git
```

2. Move to repo folder

```bash
cd ./week-number
```

3. Run tests

```
./tests.py -v
```

## How to use

This code is running in AWS (Lambda + API Gateway) by [URL](https://s7a2ppnhjj.execute-api.eu-west-2.amazonaws.com/week-number?date=2019-01-06)

URL must contain GET parameter date. Date format is `YYYY-MM-DD`.
