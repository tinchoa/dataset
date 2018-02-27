pkg load statistics % carrega o pacote de estatistica (que possui a funcao princomp)
X=load('classes.out'); % carrega o arquivo csv classes.out
label= X(:,46);
X(:,1)=[]; % remove a 1° coluna
X(:,2)=[]; % e a 3° (2° da matrix X atualizada)
[COEFF,SCORE,latent] = princomp(X); % aqui se executa o PCA da matrix X
% Isso realiza transformacoes ortogonais na matriz em questão com o intuito de remover features que podem ter correlação
% mantendo apenas aqueles que preservam a parte principal da matriz em features linearmente nao-correlacionados
XPca = X * COEFF; % aqui se usa a matriz COEFF reduzir a matrix X
XPca = XPca(:,1:6); % retira-se apenas as primerias 6 colunas

label( label~=0 )=1; % os resultados que nao sao 0 se tornam 1

Xt=[XPca label]; % monta-se a matriz resultado, com os features e os resultados pra cada observação
csvwrite('XPCA6-comlabel.csv',Xt); % e a escrevemos num arquivo
