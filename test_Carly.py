#Make sure that this program is saved at the same file as Carly.py
#Intall Pytest module before running this. 
#After Pytest is installed open Command Prompt 
#Dirict the Command Prompt to the location where the file is saved 
#then type "py.test -v"

import Carly
data = "Hello Carly search consumer last name Milan"
def test_Carly ():
    result = Carly.Carly("Hello Carly search consumer last name Milan", "Hey Carly search consumer last name Milan")
    assert result == True
    


def test_consumerCheck ():
    result = Carly.consumerCheck("Hello Carly search consumer last name Milan","Hey Carly search consumer last name Milan")
    assert result == True
    

def test_function ():
    result = Carly.function("Hello Carly search consumer last name Milan")
    assert result == True

  

def test_search ():
    result = Carly.search("Hello Carly search consumer last name Milan")
    assert result == True


