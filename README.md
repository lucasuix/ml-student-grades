
# Grade Prediction w/ Machine Learning

## Usage

Make sure you're in the 'main' directory.

To retrain the model and export the best model, if found one, as 'studentmodel.pickle'

`$ python regression.py`

To make a series of prediction of a random collection of data from the dataset:

`$ python predict.py`

## Dependencies
This repository contains a Python virtual environment with the dependencies needed already installed.

If, for any reason, the Python environment doesn't work, here's how to set up your own:

Open the terminal and type:

`$ python -m venv path/to/your/virtual/environment`

or, if you're already in your project's directory:

`$ python -m venv .`

Lastly, activate the virtual environment using:

`$ source bin/activate`

Next, we want to install the dependencies we will be using for this project.

`$ pip install scikit-learn`
`$ pip install pandas`

## License
Concerning the dataset (students directory and its content):

Cortez, Paulo. (2014). Student Performance. UCI Machine Learning Repository. https://doi.org/10.24432/C5TG7T.

This dataset is licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) license.

This license allows for the sharing and adaptation of the datasets for any purpose, provided that the appropriate credit is given.

Concerning the rest of the project:

This project is under the [MIT License](https://opensource.org/licenses/MIT).

MIT License

Copyright (c) [2024] [LUCAS VILLANI JUSTO]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
