/* I wrote this myself, based solely on Ian stephenson's book. 
Apparently there is a renderman glass example but I haven't looked at that for developing this one.
I'm assuming it's pretty similar because well, it's glass */
surface glass(
	float ior = 1.5;
	float Ks = 1;
	float rough = 0.01;
	string mapname = ""
	)
{
	normal Nn = normalize(N);
	vector In = normalize(I);
	vector V = -In;
  
	normal Nspec = faceforward(Nn, I);
	
	vector R, T;
	float kr, kt;
  
	float entering = (In.Nn <= 0) ? 1 : 0;
	float eta = (entering == 1) ? (1/ior) : ior; //because ior of air is 1
	
	fresnel(In, Nspec, eta, kr, kt, R, T);
	
	//color Cr = trace(P, R);
	//color Ct = trace(P, T);

	float blur = radians(0.1);
	float samples = 1;
	color Cr = 0;
	color hitcolor = 0;
	gather("illuminance", P, R, blur, samples, "volume:Ci", hitcolor) {
		Cr += (hitcolor/samples);
	} else {
		Cr += environment("result.tx", R);
	}
	
	samples = 4;
	color Ct = 0;
	color hitColor = 0;
	gather("illuminance", P, T, blur, samples, "volume:Ci", hitcolor) {
		Ct += (hitcolor/samples);
	} else {
		Ct += environment("result.tx", T);
	}


	color result = (kr * Cr) + (0.9 * kt * Ct);
	
	Oi = 1;	
	//Actual Color
	Ci =  Ks * specular(Nn, V, rough) + result;
	
	//Ci = color noise(P);
	
	if(mapname != ""){
		float ss = 7*s - 1.5;
		float tt = 2*t - 1.6;
		if(ss > 0.1 && ss < 0.9 && tt > 0.1 && tt < 0.9){
			color Ctex = color texture(mapname, ss, tt);
			Ci = Ctex * Ci;
		}
	}
	
}
