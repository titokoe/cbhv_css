importPackage(Packages.org.csstudio.opibuilder.scriptUtil);


//Create a new Macro Input
var macroInput = DataUtil.createMacrosInput(true);
var pvname ="CB:HV:BOX:0:1:read_volt";

//Put a macro in the new Macro Input

	//display.getWidget("input2").setPropertyValue("text", pvArray[0]);
macroInput.put("pvinput", PVUtil.getString(pvArray[0]));

//Set the macro input of the linking container to this new macro input.
displayController.setPropertyValue("macros", macroInput);

//Reload the OPI file in the linking container again 
//by setting the property value with forcing fire option in true.
displayController.setPropertyValue("opi_file", 
	displayController.getPropertyValue("opi_file"), true);

