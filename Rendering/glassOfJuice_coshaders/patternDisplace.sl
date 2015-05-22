
float triangleWave(float s; float a)
{	
	float floored = floor((s/a) + 0.5);
	float result = (2/a) * (s - a*floored);
	result *= pow(-1, floored);
	result = abs(result);
	
	return result;
}


displacement pattern (
	float Km=0.01;
) {

	normal NN = normalize(N);
	float mag = 0;
	
	mag = triangleWave(s, 0.025) * triangleWave(t, 0.075);
	mag /= length(vtransform("object", NN));
	
	float switch = smoothstep(0, 0.05, t) * (1 - smoothstep(0.72, 0.77, t));
	
	
	
	P = P + switch*Km*mag*NN;
	N = calculatenormal(P);
}
