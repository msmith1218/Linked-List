class node(object):
    def __init__(self, data = None, next_node = None, previous_node = None):
        self.previous_node = previous_node
        self.data = data
        self.next_node = next_node


    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def get_previous(self):
        return self.previous_node

    def set_next(self, new_next):
        self.next_node = new_next

    def set_previous(self, new_previous):
        self.previous_node = new_previous
