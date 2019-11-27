# loading R package TDA
library(package="TDA")
prefix <- 'datafull'
increasedlist <- read.csv(paste0(prefix,'occupied.csv'))
totaln <- nrow(increasedlist)
print(totaln)
#1000
#80% train
trainnum <- 800
testnum <- 200
print(trainnum+testnum)

distmatrix <- matrix(0,nrow = totaln, ncol = totaln)
d <-5

startindex<-trainnum+1
#full range: startindex<-trainnum+1
#full range: for (i in startindex:totaln){
for (i in startindex:totaln){
  #full range: for (j in 1:trainnum){
  for (j in 1:trainnum){
    print(i)
    #print(j)
mat1 <- scan(paste('./txtfiles/',prefix,'pc',i-1,'.txt',sep = ""))
mat1 <- matrix(mat1, ncol = d, byrow = TRUE)
Diag1 <- ripsDiag(X=mat1, maxdimension=1, maxscale=10,
                  dist="euclidean")

mat2 <- scan(paste('./txtfiles/',prefix,'pc',j-1,'.txt',sep = ""))
mat2 <- matrix(mat2, ncol = d, byrow = TRUE)
Diag2 <- ripsDiag(X=mat2, maxdimension=1, maxscale=10,
                  dist="euclidean")

dist <- wasserstein(Diag1=Diag1[["diagram"]],Diag2=Diag2[["diagram"]],
                   dimension=0)

distmatrix[i,j] <- dist
}
}

write.csv(distmatrix,"WassersteinDistMatrix.csv")