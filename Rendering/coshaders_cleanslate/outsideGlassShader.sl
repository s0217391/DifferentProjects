surface outsideGlass()
{
	shader lipstick = getshader("lipstick");
	
	color lipCol = 1, lipO;
	
	if(lipstick != null)
		lipstick->surface(lipCol, lipO);
	
	shader glass = getshader("glassLayer");
	
	if(glass != null)
		glass->surface(Ci, Oi);
		
	Ci = Ci * lipCol * lipCol * Oi;
}
