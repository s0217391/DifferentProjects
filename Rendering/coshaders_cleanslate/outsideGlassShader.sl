surface outsideGlass()
{
	shader lipstick = getshader("lipstick");
	shader fingerprints = getshader("fingerprints");
	
	color lipCol = 1, lipO, fingerCol = 1, fingerO;
	
	if(lipstick != null)
		lipstick->surface(lipCol, lipO);
	
	//Strengthen lipstick mark effects by squaring.
	lipCol = lipCol * lipCol;
	
	// Get smudges with fingerprint patterns in them
	// Multiply with noise to get fingerprints only on parts of the glass
	if(fingerprints != null)
		fingerprints->surface(fingerCol, fingerO);
		
	fingerCol = 1 - fingerCol;
	
	float noise = float noise(1.5*transform("object", P), 13);
	noise *= noise;
	fingerCol *= 0.3 * noise;


	shader glass = getshader("glassLayer");
	
	if(glass != null)
		glass->surface(Ci, Oi);
	
	Ci = (Ci * lipCol - (fingerCol)) * Oi;
}
