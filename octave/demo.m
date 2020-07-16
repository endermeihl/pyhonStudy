function z=demo(x,y)
z=x.^7+y.^7;
h=surf(x,y,z);
shading interp