from org.csstudio.opibuilder.scriptUtil import PVUtil

map = display.getWidget("existing_pvs").getPropertyValue("text")
print map
maplines = map.split("\n")
print maplines
lineparts = maplines[0].split("\t")
soi = "box_%s_%s_%s" % (lineparts[0], lineparts[1], lineparts[2])
print maplines
print lineparts
print soi
array = [1,"2"]
print array
count = 0
mapelementarray = []
mapboxarray = []
maplevelarray = []
mapchannelarray = []
maplinearray = []

#while count < len(maplines):

mapline = maplines[0].split("\t")
mapline[0] = int(mapline[0])
mapelementarray.append(mapline[0])

print mapelementarray[0]
