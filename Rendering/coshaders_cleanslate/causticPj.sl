class causticPj(float Kc = 1) 
{

	/*
	 *	Get the caustic map value
	 */
	public void surface(output color Ci, Oi)
	{
		vector Nn = normalize(N);
		
		
		Oi = 1;
		Ci = Kc * caustic(P, Nn);
		
	}
}
