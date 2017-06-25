FWD_SLASH = "/"

def attributesFromDict(d):
    self = d.pop('self')    
    for k, v in d.items():
        setattr(self, k, v)