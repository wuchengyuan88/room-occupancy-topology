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
d <- 5


mat1 <- scan(paste('./txtfiles/',prefix,'pc',60,'.txt',sep = ""))
mat1 <- matrix(mat1, ncol = d, byrow = TRUE)
Diag1 <- ripsDiag(X=mat1, maxdimension=1, maxscale=0.2,
                  dist="euclidean")
plot(Diag1[["diagram"]])
