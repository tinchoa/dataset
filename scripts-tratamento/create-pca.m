
X=load('classes-21.out');
label= X(:,46);
X(:,1)=[];
X(:,2)=[];
[COEFF,SCORE,latent] = princomp(X);
XPca = X * COEFF;
XPca = XPca(:,1:6);

label( label~=0 )=1;

Xt=[XPca label];
csvwrite('XPCA6-comlabel-21',Xt);