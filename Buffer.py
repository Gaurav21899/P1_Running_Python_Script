import arcpy

# Setting the default workspace environment
arcpy.env.workspace = r"D:\Sem-3\Programming for GIS-3\Practical_1_ProProject\Practical_1_ProProject\01_Running_Python_Scripts.gdb"
arcpy.analysis.Buffer("Wilsin_Schools.Buffer","500 meters")