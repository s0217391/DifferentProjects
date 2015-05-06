surface env()
{
	vector In = normalize(I);
	vector V = -In;
	
	matrix M = 1;
	M = rotate(M, -90, vector (1, 0, 0));
	
	vector Vt = vtransform(M, V);
	
	
	Ci = color environment("result.tx", Vt);
}