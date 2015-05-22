displacement noiseDisp (
	float Km=0.1;
) {

	normal NN = normalize(N);
	float mag = 0;
	
	float mult = 1;
	
	point pp = transform("shader", P);
	
	mag = float noise(mult * pp);
	mag /= length(vtransform("object", NN));
	
	P = P + Km*mag*NN;
	N = calculatenormal(P);
}
