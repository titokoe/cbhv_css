from org.csstudio.opibuilder.scriptUtil import PVUtil

value = display.getWidget("rect1").getPVByName("loc://forward").getValue()
widget.getPV().setValue(value)
