surface env()
{
	vector In = normalize(I);
	vector V = In; //this goes away from the viewer.
	
	matrix M = 1;
	M = rotate(M, 90, vector (1, 0, 0));
	
	vector Vt = vtransform(M, V);
	vector Ve = vtransform("object", Vt);
	
	
	Ci = color environment("result.tx", Ve);
}
