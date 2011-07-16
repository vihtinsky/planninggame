class Team(object):
    name = None
    def __init__(self, name):
        self.name = name

    def get_estimate(self):
        return Estimate(1)


class Estimate(object):
    title = "Estimate title"
    text = "Estimate text la la la"
    link = "http://redmine.odeskps.com/"
    def __init__(self, estimate_id):
        pass
