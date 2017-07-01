FWD_SLASH = "/"


def attributes_from_dict(d):
    self = d.pop('self')    
    for k, v in d.items():
        setattr(self, k, v)