class Octree:
    def __init__(self, x, y, z, x1, y1, z1):
        self.Top_Right = Point(x, y, z)
        self.Back_Left = Point(x1, x1, z1)
        self.Root_Node = Node((x+x1)/2, (y+y1)/2, (z+z1)/2)
        self.Height = 0
        self.Max_Size = 0  # size to not be exceeed
        self.Total_Nodes = 1

    def Split_Node(self):
        #self.Total_Nodes += 8
        # if it splits we will change it render to false and no longer leaf node
        pass

    def Search(self, Node):
        pass

    def Delete(self, Node):

        pass

    def Add(self, Node):
        pass


class Point:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z


class Node:

    def __init__(self, Point, Data=None, Render=True):
        self.Points = Point(Point)
        self.Data = Data
        self.Render = True
        self.LeafNode = True
        self.Children = [None, None, None, None, None, None, None, None, ]

    def Change_Render_State(self):
        if not self.LeafNode:
            self.Render = False

    def Change_Data(self, Data):
        self.Data = Data
