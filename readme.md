# Steps to run

## 1. Creating .env file

create a file named ".env" in the root directory of the project and add the following code in it

```
OPENTRIPMAP_API_KEY="replace with api"
```

go to this [link](https://dev.opentripmap.org/account/settings) and sign in with google, copy the api key from the page and paste in the .env file.

## 2. Install required packages using pip

run the following command on the terminal

```
pip install -r requirements.txt
```

## 3. run the main file

run the `main.py` file in the root directory of the project either by opening the file and pressing `f5` or by running `python main.py` in the vscode terminal. 
