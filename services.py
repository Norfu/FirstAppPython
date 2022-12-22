from classes import User
def UserAlreadyExist():
    """Look if an User is already created or not

    Returns:
        bool: false if user exist else true 
    """
    file = GetPath("UserDb","r")
        
    line = file.readline()
    if(line == ""):
        return True
    else:
        return False
    
def GetPath(name,command):
        """ Create file if not already create and get the path

        Args:
            name (string): file's name
            command (string): permission for the file (r : read-only, w: write but overwritte, a: write)

        Returns:
            IO: file (open)
        """
        try:
           file = open(f"C:\GitHub\Exercice-PYTHON\Projet Sante\{name}.txt",f"{command}")
        except FileNotFoundError:
            print("File not found")
        return file
    
def CreateUser(user):
    """Write in the UserDb the value of properties from user

    Args:
        user (User): Object User
    """
    file = GetPath("UserDb","w")
    file.write(f"{user}")   
    
    file.close()
    
def GetUser():
    file = GetPath("UserDb","r")
    
    lines = file.readlines()
    for l in lines :
        user = User(l[0],l[1],l[2],l[3],l[4])