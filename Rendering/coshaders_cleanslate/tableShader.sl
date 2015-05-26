surface table(
	float Kd = 1;
	float Ka = 1;
)
{

	vector NN = normalize(N);
	
	color woodCol = 0, woodOp = 0;
	
	shader woodshader = getshader("woodtexture");
	if(woodshader != null)
		woodshader->surface(woodCol, woodOp);
	
	color HLCol, HLOp = 0; 
	
	shader tableHL = getshader("tableHighLights");
	if(tableHL != null)
		tableHL->surface(HLCol, HLOp);
	
	shader caustic = getshader("tableCaustic");
	
	color causCol, causOp;
	if(caustic != null)
		caustic->surface(causCol, causOp);
		
	Oi = Os * HLOp * woodOp * causOp;
	
	Ci = Kd * woodCol * diffuse(NN) + Ka * ambient() * woodCol;
	Ci += HLCol;
	Ci += causCol;
	
	Ci *= Oi;
}
