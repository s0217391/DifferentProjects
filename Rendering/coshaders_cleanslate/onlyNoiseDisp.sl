displacement onlyNoiseDisp () {

	shader noiseDisp = getshader("noiseD");
	
	if(noiseDisp != null)
		noiseDisp->displacement(P, N);

}
