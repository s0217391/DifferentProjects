surface outsideGlass()
{
	shader lipstick = getshader("lipstick");
	shader fingerprints = getshader("fingerprints");
	
	color lipCol = 1, lipO, fingerCol = 1, fingerO;
	
	if(lipstick != null)
		lipstick->surface(lipCol, lipO);
	
	if(fingerprints != null)
		fingerprints->surface(fingerCol, fingerO);
	
	shader glass = getshader("glassLayer");
	
	if(glass != null)
		glass->surface(Ci, Oi);
		
	Ci = Ci * fingerCol * lipCol * lipCol * Oi;
}
