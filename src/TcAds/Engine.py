class Engine:

    valueDict = {}

    def __init__(self):
        pass

    

    def addVariables(self, variable):
        """Adds variable """
        self.valueDict[variable.name] = variable
    

    def __str__(self):
        return self.valueDict