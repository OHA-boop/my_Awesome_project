def cleanWB(entity):
    ExtAPI.Log.WriteMessage("Cleaning up in progress, please wait ...")
    for system in GetAllSystems():
        try:
            modelComponent = system.GetComponent(Name="Model")
            ExtAPI.Log.WriteMessage("Cleaning up " + system.Name.ToString())
            modelComponent.Clean()
        except: # some systems can not be updated, geometry for example
            pass