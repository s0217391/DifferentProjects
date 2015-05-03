surface first()
{
  Oi = Os;
  
  normal Nf = faceforward( normalize(N), I);
  normal Nw = ntransform("world", Nf);
  
  Ci = color Nw;
}
