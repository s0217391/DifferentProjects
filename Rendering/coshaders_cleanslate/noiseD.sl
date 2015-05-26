class noiseDisp(float Km = 0.01) 
{

	/*
	 *	Get the caustic map value
	 */
	public void displacement(output point P; output normal N)
	{
		normal NN = normalize(N);
		float mag = 0;
	
		float mult = 1;
	
		point pp = transform("object", P);
	
		mag = float noise(mult * pp);
		mag /= length(vtransform("object", NN));
	
		P = P + Km*mag*NN;
		N = calculatenormal(P);
	}
}
