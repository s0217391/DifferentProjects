/*
Shader for an environment light. Based on this webpage:
http://renderman.pixar.com/resources/17/rps/legacyShaders.html#light-sources
*/
light envlight(string texturename = "result.tx"; float intensity = 1.0)
{
	solar() {
		Cl = intensity * color environment(texturename, -L);
	}
}