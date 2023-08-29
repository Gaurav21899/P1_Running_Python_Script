import arcpy

# Path to the input feature class
input_feature_class_path = r"D:\Sem-3\Programming for GIS-3\P1_Running_Python_Script\Practical_1_ProProject\01_Running_Python_Scripts.gdb\Wilson_Schools"

# Path to the output buffer feature class
output_buffer_path = r"D:\Sem-3\Programming for GIS-3\P1_Running_Python_Script\Practical_1_ProProject\Ouput.gdb\buffer_500m"

# Buffer distance
Distance = "500 meters"

arcpy.analysis.Buffer(input_feature_class_path,output_buffer_path,Distance)

print("Process Completed")