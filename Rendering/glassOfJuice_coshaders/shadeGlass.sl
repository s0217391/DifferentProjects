surface onlyGlass ()
{

	shader baseglass = getshader("glassLayer");
	if(baseglass != null)
		baseglass->surface(Ci, Oi);
}
