/* I wrote this myself, based solely on Ian stephenson's book. 
Apparently there is a renderman glass example but I haven't looked at that for developing this one.
I'm assuming it's pretty similar because well, it's glass */
surface glass()
{
	normal Nn = normalize(N);
	normal Nf = faceforward(Nn, I);
	vector In = normalize(I);
	vector V = -In;
  
	vector R, T;
	float Kr, Kt;
  
	float refractiveRatio = 1.05;
	float refrac_inv = 1.0 / refractiveRatio;  
  
  	if(In.N < 0)
  	{
		fresnel(In, Nn, refractiveRatio, Kr, Kt, R, T);
	} else {
		fresnel(In, -Nn, refrac_inv, Kr, Kt, R, T);
	}
	
	color Cr = trace(P, R);
	color Ct = trace(P, T);
	
	
	color result = (Kr * Cr) + (Kt * Ct);
	
	Oi = 1;
	
	// Normal Check
	//color test = color (normalize(N).V);
	//Ci = test;
	
	//Actual Color
	Ci = Cs * (result + 0.1);
}
