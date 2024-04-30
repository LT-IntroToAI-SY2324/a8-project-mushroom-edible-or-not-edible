<<<<<<< HEAD
pip install ucimlrepo

=======
>>>>>>> bd642412d026bb20c07ebe920ab67aca4f652e3d
from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
mushroom = fetch_ucirepo(id=73) 
  
# data (as pandas dataframes) 
X = mushroom.data.features 
y = mushroom.data.targets 
  
# metadata 
print(mushroom.metadata) 
  
# variable information 
<<<<<<< HEAD
print(mushroom.variables) 
=======
print(mushroom.variables) 
>>>>>>> bd642412d026bb20c07ebe920ab67aca4f652e3d
