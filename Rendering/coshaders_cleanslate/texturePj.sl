class texturePj(string mapname = ""; 
				float stretchS = 1; 
				float stretchT = 1; 
				float offsetS = 0;
				float offsetT = 0;
				float tiling = 1) 
{

	/*
	 *	Get a texture value
	 */
	public void surface(output color Ci, Oi)
	{
		
		color Ctex = 1;
		
		if(mapname != ""){
			float ss = stretchS * s - offsetS;
			float tt = stretchT * t - offsetT;
			
			if(tiling > 0) 
			{
				ss = mod(ss, 1);
				tt = mod(tt, 1);
			}
			
			Ctex = color texture(mapname, ss, tt);
		
		} 
		
		Oi = Os;
		Ci = Ctex;
	}
}
