surface insideGlass()
{
	
	shader glass = getshader("glassLayer");
	
	if(glass != null)
		glass->surface(Ci, Oi);
}
