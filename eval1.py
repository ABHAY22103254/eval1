add = { "abhay": [12,"fbbf"],
         "arnav": [32,"fdfdf"],
         "ritvish": [323,"fwew"]
      } 

def adding(name,phone_no,email):
    add[name] = [phone_no,email]
    print("adding contacts: ",add)
    

def updating(name,new_phone,new_email):
    add[name] = [new_phone,new_email]
    print("updating cotacts: ",add)

def delete(name):
    add.pop(name)
    print("deleteing contacts: ",add)


def display():
    print("displaing contacts: ",add)

'''def listing():
    if add.name[0] == "a"
    print()'''

def search(name):
    for i in add:
        if i == name:
            print("name found: ",add.name)
        else:
            print("name not found")
    
    
    
adding("aryash",234,"sfsdf")
adding("manan",343,"dfsdg")
updating("abhay",1,"saini")
delete("abhay")
search("arnav")
