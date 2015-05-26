/*
 * Loosely based on: https://renderman.pixar.com/resources/RPS_17/importanceOfImportance.html
 */
class glassPj (float ior = 1.5; 
			   float Kr = 1; 
			   float Kt = 1; 
			   float maxdepth = 4; 
			   float rtsamples = 4;
			   float Ks = 1;
			   float shiny = 20.0;
			   float Kabsorp = 0.01) {

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
	
	// Fresnel
	fresnel(In, Nspec, eta, kr, kt, R, T);

	// ray trace parameters
	float blur = radians(0.1);
	float samples = rtsamples;
	
	// Get ray depth
	// Will use this to limit raytracing. Rather than returning 0 when max depth has been found, I will return the environment map
	// This limits the raytracing depth and hence the rendertime, without resulting in black spots.
	// I believe the difference with deeper raytracing will be hard to tell as no one really knows what refraction is supposed to look like.
	float raydepth;
	rayinfo("depth", raydepth);
	
	// Limit the ray tracing samples when raydepth is high enough
	if(raydepth > 2) samples = 1;
	
	color Cr = 0;
	color Ct = 0;
	
	// Reflection depth
	if(Kr * kr > 0) {
		color hitcolor = 0;
		if(raydepth <= maxdepth) {
			gather("illuminance", P, R, blur, samples, "surface:Ci", hitcolor) {
				Cr += hitcolor;
			} else {
				Cr += environment("environment.tx", R);
			}
			Cr = Cr / samples;
		} else {
			//Avoid deeper ray tracing
			Cr = environment("environment.tx", R);
		}
	}
	
	// Refraction rays
	if(Kt * kt > 0) {
		color hitcolor = 0;
		float distance = 0;
		point hitP = (0, 0 ,0);
		if(raydepth <= maxdepth) {
			gather("illuminance", P, T, blur, samples, "surface:Ci", hitcolor, "surface:P", hitP) {
				if(entering < 0.5){
					distance = length(hitP - P);
					//Beer's law
					float decay = exp(- Kabsorp * distance);
					Ct += hitcolor * decay;
					
					
				} else {
					Ct += hitcolor;
				}
			} else {
				Ct += environment("environment.tx", T);
			}
			Ct = Ct / samples;
		} else {
			//Avoid deeper ray tracing
			Ct = environment("environment.tx", T);
		}
	}


	color result = (Kr * kr * Cr) + (Kt * kt * Ct);
	
	Oi = 1;	
	//Actual Color
	Ci =  result;	
		
	//Add phong highlights
	Ci += Ks * specular(Nn, V, 1 / shiny);
}

}
