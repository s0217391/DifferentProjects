/* Fully based on http://renderman.pixar.com/view/cook-torrance-shader */
surface CT (
	float Ka = 1;
	float Ks = 1;
	float Kd = 1;
	float F0 = 1;
	float roughness = .2;
	color opacity = 1;
	color specularColor = 1;
	float gaussConstant = 100;
) {

vector In = normalize(I);
vector Nn = normalize(N);
vector Vn = -In;
float m = roughness;

float F, KTransmit = 1;
fresnel( In, Nn, F0, F, KTransmit);

float NdotV = Nn.Vn;
color cook = 0;
illuminance(P, Nn, PI/2) {
	
	// Cook Torrance goes here
	vector Ln = normalize(L);
        vector H = normalize(Vn+Ln);
        float NdotH = Nn.H;
        float NdotL = Nn.Ln;
        float VdotH = Vn.H;


	// Geometric attenuation
	float G = min(1, (2*NdotH*NdotV/VdotH), (2*NdotH*NdotL/VdotH));
	// Slope distribution D
	float alpha = acos(NdotH);
	float D = gaussConstant*exp(-(alpha*alpha)/(m*m));
	
	//sum contributions
	cook += Cl * (F * D * G)/ (PI * NdotV);
	
}

cook = cook/PI;

Oi = opacity;
Ci = (Kd * Cs * diffuse(Nn) + Ks * specularColor * cook + Ka * ambient()) * Oi;

}
