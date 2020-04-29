library("tictoc")

# loading R package TDA
library(package="TDA")

tic()
#prefix <- 'datafull'
increasedlist <- read.csv('cyclinglist.csv')
totaln <- nrow(increasedlist)
print(totaln)
#2880
#60% train
trainnum <- 1728
validnum <- 576
testnum <- 576
print(trainnum+validnum+testnum)

distmatrix <- matrix(0,nrow = totaln, ncol = totaln)
d <-6

startindex<-trainnum+1
#full range: startindex<-trainnum+1
#full range: for (i in startindex:totaln){
for (i in startindex:(totaln)){
  #full range: for (j in 1:trainnum){
  for (j in 1:trainnum){
    if (j==1){
    print(i)
    }
    #print(j)
mat1 <- scan(paste('./txtfiles/','pc',i-1,'.txt',sep = ""),quiet=TRUE)
mat1 <- matrix(mat1, ncol = d, byrow = TRUE)
Diag1 <- ripsDiag(X=mat1, maxdimension=1, maxscale=20,
                  dist="euclidean")

mat2 <- scan(paste('./txtfiles/','pc',j-1,'.txt',sep = ""),quiet=TRUE)
mat2 <- matrix(mat2, ncol = d, byrow = TRUE)
Diag2 <- ripsDiag(X=mat2, maxdimension=1, maxscale=20,
                  dist="euclidean")

dist <- wasserstein(Diag1=Diag1[["diagram"]],Diag2=Diag2[["diagram"]],
                   dimension=0)

distmatrix[i,j] <- dist
}
}

write.csv(distmatrix,"WassersteinDistMatrix.csv")

toc()
#917.633 sec elapsed