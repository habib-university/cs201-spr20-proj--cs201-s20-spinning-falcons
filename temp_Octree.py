class Node:

    def __init__(self, Point1, Point2, Data=None, Render=True):
        self.Top_Left_Front = Point(Point1)
        self.Back_Right_Bottom = Point(Point2)
        self.Data = Data
        self.Render = Render
        self.LeafNode = True

    def Change_Render_State(self):
        if not self.LeafNode:
            self.Render = False

    def Change_Data(self, Data):
        self.Data = Data


class Point:

    def __init__(self, x=None, y=None, z=None):
        self.x = x
        self.y = y
        self.z = z


class Octree:
    def __init__(self, Point_1 = None, Point_2 = None):

        self.Children = {'TLF':None, 'TRF': None, 'BRF':None, 'BLF' :None,'TLB': None,'TRB': None,
        'BRB': None,'BLB': None}

        self.Top_Left_Front = None
        self.Bottom_Right_Back = None

        if Point_1 == None and Point_2 == None:
            self.Root_Node = Point()
        
        elif Point_2 == None and Point_1 != None:
            self.Root_Node = Point(Point_1.x, Point_1.y, Point_1.z)
        
        elif Point_1 != None and Point_2 != None:
            self.Top_Left_Front = Point_1 
            self.Bottom_Right_Back = Point_2

        
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
            'BLB': 7    # bottom left back
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
            
        if (self.Children[Position] != None):
            if self.Root_Node == None:
                self.Children[Position].Add(Point1)
            else:
                temp_point:Point = self.Children[Position].Root_Node
                self.Children[Position].Root_Node = None

                if(Position == 'TLF'):
                    self.Children[Position] = Octree(self.Top_Left_Front, Point(Mid_Point_x, Mid_Point_y, Mid_Point_z))

                elif Position == 'TLB':
                    self.Children[Position] = Octree(Point(Mid_Point_x + 1, self.Top_Left_Front.y, self.Top_Left_Front.z),
                    Point(self.Bottom_Right_Back.x, Mid_Point_y, Mid_Point_z))

                elif Position == 'BRF':
                    self.Children[Position] = Octree(Point(Mid_Point_x + 1, Mid_Point_y + 1, self.Top_Left_Front.z),
                    Point(self.Bottom_Right_Back.x, self.Bottom_Right_Back.y, Mid_Point_z))
            
                elif Position == 'BLF':
                    self.Children[Position] = Octree(Point(self.Top_Left_Front.x, Mid_Point_y+1, self.Top_Left_Front.z),
                    Point(Mid_Point_x, self.Bottom_Right_Back.y, Mid_Point_z))

                elif Position == 'TLB':
                    self.Children[Position] = Octree(Point(self.Top_Left_Front.x, self.Top_Left_Front.y, Mid_Point_z + 1),
                    Point(Mid_Point_x, Mid_Point_y, self.Bottom_Right_Back.z))

                elif Position == 'TRB':
                    self.Children[Position] = Octree(Point(Mid_Point_x + 1, self.Top_Left_Front.y, Mid_Point_z +1),
                    Point(self.Bottom_Right_Back.x, Mid_Point_y, self.Bottom_Right_Back.z))

                elif Position == 'BRB':
                    self.Children[Position] = Octree(Point(Mid_Point_x + 1, Mid_Point_y+1, Mid_Point_z +1),
                    Point(self.Bottom_Right_Back.x, self.Bottom_Right_Back.y, self.Bottom_Right_Back.z))

                elif Position == 'BLB':
                    self.Children[Position] = Octree(Point(self.Top_Left_Front.x, Mid_Point_y+1, Mid_Point_z +1),
                    Point(Mid_Point_x, self.Bottom_Right_Back.y, self.Bottom_Right_Back.z))

                self.Children[Position].Add(temp_point)
                self.Children[Position].Add(Point1)

        if self.Children[Position] == None:
            self.Children[Position] = Octree(Point1)

            # arrived at closest leaf node
                
        
        ## add node how
        
        

        




####### Helper Functions #######

def check_bounds(p1: Point, u: Node):
    if (p1.x < u.Top_Left_Front.x or p1.x > u.Back_Right_Bottom.x or
        p1.y < u.Top_Left_Front.y or p1.y > u.Back_Right_Bottom.y or
            p1.z > u.Top_Left_Front.z or p1.z < u.Back_Right_Bottom.z):
        return False

    return True


