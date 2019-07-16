# Working Code for Snek Tutorial

## Disclaimer
I did not make this tutorial or come up with this code but I really enjoyed the tutorial. To help others I am putting up a working version on github. This will help others see how it works if they are having trouble. Props to [Amir Rachum](https://discuss.amir.rachum.com/t/python-entry-points-explained/193/19) for the tutorial.

python 3.7 tested working on Windows

## How to use code
1. follow tutorial at [snek tutorial by Amir Rachum](https://discuss.amir.rachum.com/t/python-entry-points-explained/193/19)
2. create and activate a virtualenv
```
python -m venv venv
venv\Scripts\activate # Windows
venv/bin/activate # Linux
pip install docopt
```
3. go to snek folder and install
```
cd snek
python setup.py develop # install snek
```
4. go to cute_snek and install
```
cd cute_snek # from root folder otherwise cd ../cute_snek
python setup.py develop # install snek
```
5. test out functionality
```
snek
snek --type cute
snek --type fancy
```
## Epilogue 
thanks [Amir Rachum](https://discuss.amir.rachum.com/t/python-entry-points-explained/193/19) looking forward to seeing more tutorials