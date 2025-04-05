class loggerParam:
    def __init__(self, message, place="", tag=""):
        self.message = message
        self.place = place
        self.tag = tag

    def parse_dict(self):
        return {
            'message' : self.message,
            'place' : self.place,
            'tag' : self.tag
        }