document.addEventListener("load", e =>
{
	// only execute once (even though multiple instances exist)
	if(!parentDoc.hasOwnProperty(componentID+'_data'))
	{
		// Dispatch the event.
		document.dispatchEvent(preLoadedOnceEvent);
		parentDoc[componentID+'_data'] = {registeredComponents: []};
		
		CSSVariablesToString(vars, false, "#"+tooltipID);

		let client = new XMLHttpRequest();
		addParentStyleSheets.forEach( styleSheetPath =>
		{
			client.open('GET', styleSheetPath);
			client.onreadystatechange = function() {
				client.responseText.replaceVariables();
				AppendStyle(componentID, client.responseText, parentDoc);
			}
			client.send();
		}
		
		// Dispatch the event.
		document.dispatchEvent(loadedOnceEvent);
	}
	sharedData = parentDoc[componentID+'_data'];
	sharedData.registeredComponents.push(document);
	
	let global_component_data = 'global_component_data';
	if(!parentDoc.hasOwnProperty(global_component_data))
	{
		parentDoc[global_component_data] = {registeredComponents: sharedData.registeredComponents};
	}
	globalData = parentDoc[global_component_data];
	
	document.dispatchEvent(componentLoadedEvent);
});