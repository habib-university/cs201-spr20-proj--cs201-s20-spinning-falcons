class Octree:
    def __init__(self, x, y, z, x1, y1, z1):

        self.Root_Node = Node((x, y, z), (x1, y1, z1))
        self.Height = 0
        self.Max_Size = 0  # size to not be exceeed
        self.Total_Nodes = 1

        self.Position_Map = {
            'TLF': 0,   # top left front
            'TRF': 1,   # top right front
            'BRF': 2,   # bottom right front
            'BLF': 3,   # bottom left front
            "TLB": 4,   # top left back
            'TRB': 5,   # top right back
            'BRB': 6,   # bottom right back
            'BLB': 7
        }

    def Split_Node(self):
        # self.Total_Nodes += 8
        # if it splits we will change it render to false and no longer leaf node
        pass

    def Search(self, Point1):  # searching for a Point

        u = self.Root_Node
        Path = []

        # if (Point1.x < u.Top_Left_Front.x or Point1.x > u.Back_Right_Bottom.x or Point1.y < u.Top_Left_Front.y or Point1.y > u.Back_Right_Bottom.y or Point1.z < u.Top_Left_Front.z or Point1.z > u.Back_Right_Bottom.z):

        #     return ' Point lies outside octree Region '

        if check_bounds(Point1, u) == False:
            return ' Point lies outside octree Region '

        else:

            while(u.LeafNode == False):

                Mid_Point_x = (u.Top_Left_Front.x + u.Back_Right_Bottom.x) // 2
                Mid_Point_y = (u.Top_Left_Front.y + u.Back_Right_Bottom.y) // 2
                Mid_Point_z = (u.Top_Left_Front.z + u.Back_Right_Bottom.z) // 2

                if (Point1.x <= Mid_Point_x):
                    if(Point1.y <= Mid_Point_y):
                        if (Point1.z <= Mid_Point_z):
                            Position = 'TLF'
                        else:
                            Position = 'TLB'
                    else:
                        if(Point1.z <= Mid_Point_z):
                            Position = 'BLF'
                        else:
                            Position = 'BLB'
                else:
                    if(Point1.y <= Mid_Point_y):
                        if (Point1.z <= Mid_Point_z):
                            Position = 'TRF'
                        else:
                            Position = 'TRB'
                    else:
                        if (Point1.z <= Mid_Point_z):
                            Position = 'BRF'
                        else:
                            Position = 'BRB'
                if u.Children[self.Position_Map[Position]] != None:

                    u = u.Children[self.Position_Map[Position]]
                    Path.append(self.Position_Map[Position])

                else:  # arrived at closest leaf node

                    return Path, u

    def Delete(self, Point):

        pass

    def Add(self, Point1, u: Node = None):
        if u == None:
            u = self.Root_Node


        if not check_bounds(Point1, u):
            print("Not in Bounds")
            return False

        if (not u.LeafNode):
            Mid_Point_x = (u.Top_Left_Front.x + u.Back_Right_Bottom.x) // 2
            Mid_Point_y = (u.Top_Left_Front.y + u.Back_Right_Bottom.y) // 2
            Mid_Point_z = (u.Top_Left_Front.z + u.Back_Right_Bottom.z) // 2

            if (Point1.x <= Mid_Point_x):
                if(Point1.y <= Mid_Point_y):
                    if (Point1.z <= Mid_Point_z):
                        Position = 'TLF'
                    else:
                        Position = 'TLB'
                else:
                    if(Point1.z <= Mid_Point_z):
                        Position = 'BLF'
                    else:
                        Position = 'BLB'
            else:
                if(Point1.y <= Mid_Point_y):
                    if (Point1.z <= Mid_Point_z):
                        Position = 'TRF'
                    else:
                        Position = 'TRB'
                else:
                    if (Point1.z <= Mid_Point_z):
                        Position = 'BRF'
                    else:
                        Position = 'BRB'

            if u.Children[self.Position_Map[Position]] != None:

                self.Add( Point1, u.Children[self.Position_Map[Position]])

            # arrived at closest leaf node
                
        
        ## add node how
        
        

        


class Point:

    def __init__(self, x=-1, y=-1, z=-1):
        self.x = x
        self.y = y
        self.z = z


class Node:

    def __init__(self, Point1, Point2, Data=None, Render=True):
        self.Top_Left_Front = Point(Point1)
        self.Back_Right_Bottom = Point(Point2)
        self.Data = Data
        self.Render = Render
        self.LeafNode = True
        self.Children = [None, None, None, None, None, None, None, None]

    def Change_Render_State(self):
        if not self.LeafNode:
            self.Render = False

    def Change_Data(self, Data):
        self.Data = Data


####### Helper Functions #######

def check_bounds(p1: Point, u: Node):
    if (p1.x < u.Top_Left_Front.x or p1.x > u.Back_Right_Bottom.x or
        p1.y < u.Top_Left_Front.y or p1.y > u.Back_Right_Bottom.y or
            p1.z > u.Top_Left_Front.z or p1.z < u.Back_Right_Bottom.z):
        return False

    return True
