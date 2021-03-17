from binomial import Binomial

if __name__ == '__main__':

    inp = input("Would you like to enter custom values ? (Y/n)")
    if inp == 'Y':
        initialAssetPrice = float(input("Initial Asset Price : "))
        riskFreeRate = float(input("Risk Free Rate : "))
        timeToExpiration = float(input("Time to expiration : "))
        u = float(input("value of u : "))
        d = float(input("value of d : "))
        numberOfSteps = int(input("Number of steps in process : "))
        expirationPrice = float(input("Expiration price of option : "))

    else:
        initialAssetPrice = 100
        riskFreeRate = 0.05
        timeToExpiration = 1
        u, d, numberOfSteps, expirationPrice = 1.3, 0.9, 10, 100

    binomial = Binomial(initialAssetPrice=initialAssetPrice, riskFreeRate=riskFreeRate,
    timeToExpiration=timeToExpiration,u=u, d=d, numberOfSteps=numberOfSteps, expirationPrice=expirationPrice)

    print("\n-------------------------------\n")
    binomial.option_price()
    print("\n-------------------------------\n")
