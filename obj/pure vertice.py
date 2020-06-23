#import bpy

with open(r"Handgun_obj.txt", "r") as file1:
    # file2 = open("Point_cloud.txt", "a")

    vertices = []
    faces = []

    for line in file1.readlines():
        if line[0:2] == "v ":
            line = line.split()
            v_tuple = (float(line[1]), float(line[2]), float(line[3]))
            vertices.append(v_tuple)
        if line[0:2] == "f ":
            face_tuple = list()
            line = line.split()
            for element in line[1:]:
                element = element.split("/")
                face_tuple.append(int(element[0]))
            face_tuple = tuple(face_tuple)
            faces.append(face_tuple)
    # file1.close()


# print(vertices[:])
# print(len(vertices))
print(faces[:10])
# mymesh = bpy.data.meshes.new("Abbu")
# myobj = bpy.data.objects.new("Abbu", mymesh)

# myobj.location = bpy.context.scene.cursor.location
# bpy.context.collection.objects.link(myobj)

# mymesh.from_pydata(vertices, [], faces)
# mymesh.update(calc_edges=True)
