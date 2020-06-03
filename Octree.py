class Octree:
    def __init__(self):
        self.Root_Node = Node(0, 0, 0)
        self.Height = 0
        self.Max_Size = 0  # size to not be exceeed
        self.Total_Nodes = 1

    def Split_Node(self):
        self.Total_Nodes += 8
        pass

    def Search(self, Node):
        pass

    def Delete(self, Node):

        pass

    def Add(self, Node):
        pass


class Node:

    def __init__(self, Point, Data=None, Render=True):
        self.Points = Point
        self.Data = Data
        self.Render = True
        self.Children = [None, None, None, None, None, None, None, None, ]

    def Change_Render_State(self, State):
        self.Render = State

    def Change_Data(self, Data):
        self.Data = Data
