surface second()
{
  normal Nf = faceforward(normalize(N), I);
  vector In = normalize(I);
  vector V = -In;
  
  vector R, T;
  float Kr, Kt;
  
  fresnel(In, N, 1.5, Kr, Kt, R, T);
  
  //color Cr = trace(P, R);
  //color Ct = trace(P, T);

  //color result = Kr * Cr + Kt * Ct;
  
  vector Rworld = vtransform("world", R);
  color Cr = color environment("../environmentmap/result.tx", Rworld);
  
  Oi = 1;
  Ci = Cr + 0.0;
}