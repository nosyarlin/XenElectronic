# XenElectronic
## Overview
This is a MVP for an online web store for XenElectronics. For the purpose of this exercise, only the following features were implemented:

+ Viewing products by category on home page
+ Adding products to cart
+ Viewing cart
+ Removing products from cart
+ Proceeding to checkout

For the interest of time, login feature was not implemented. For parts of the api that requires userId, a test userId was hardcoded. In a real web store, the server will return a cookie after the user has authenticated themselves and we will use the cookie in future requests. 

## Requirements
Python 3.5.2+
node 14+
yarn 1.22+
direnv

## Server Usage
First follow the instructions on https://direnv.net/ and install and activate direnv inside the `swagger_server` directory. This is required for setting PYTHONPATH.
Next, add a .envrc file inside the `swagger_server` directory
```
export PYTHONPATH=${PYTHONPATH}:.
```

After that is done, please execute the following from the root directory:
```
pip3 install -r requirements.txt
```

Finally, run the following from `swagger_server` directory
```
flask run
```

To launch automated tests, run the following from `swagger_server` directory
```
python3 -m pytest
```

If you wish to see the test coverage, you can run pytest with the --cov argument
```
python3 -m pytest --cov=.
```

## Client Usage
The client is written in react. To run it, go to the `client` directory and run 
```
yarn install
yarn build
yarn start
```

and open your browser to here:

```
http://localhost:3000/home
```

Once you have setup everything and ensured that you can start both the server and the client, you can start both at the same time using the provided shell script in the root directory
```
./start_app
```
