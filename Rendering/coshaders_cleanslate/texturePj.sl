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
			
			float ss_m = mod(ss, 1.0);
			float tt_m = mod(tt, 1.0);
			
			Ctex = color texture(mapname, ss_m, tt_m);
			
			if(tiling < 0.5){
				//These borders are specific for my project: 
				// 		They assume the texture of interest is in the center of the image
				//		Avoids artifacts at the borders of the lipstick mark.
				if(ss < 0.1 || ss > 0.9 || tt < 0.1 || tt > 0.9) Ctex = 1;
			}
			

		
		} 
		
		Oi = 1;
		Ci = Ctex;
	}
}
