class glassShaderPj (float ior = 1.5; float Ks = 1;	float rough = 0.01) {

public void surface (output color Ci, Oi)
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
		//Cr += environment("result.tx", R);
	}
	
	samples = 4;
	color Ct = 0;
	color hitColor = 0;
	gather("illuminance", P, T, blur, samples, "volume:Ci", hitcolor) {
		Ct += (hitcolor/samples);
	} else {
		//Ct += environment("result.tx", T);
	}


	color result = (kr * Cr) + (0.9 * kt * Ct);
	
	Oi = Os;	
	//Actual Color
	Ci =  Ks * specular(Nn, V, rough) + result;	
}

}
