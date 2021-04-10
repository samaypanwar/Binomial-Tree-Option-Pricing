from binomial import Binomial
import sys
sys.path.append('../')
import yaml

if __name__ == '__main__':

    inp = input("Would you like to enter custom values ? (Y/n)")

    if inp == 'Y':

        typeOfOption = input("What kind of option is it? : ")
        initialAssetPrice = float(input("Initial Asset Price : "))
        riskFreeRate = float(input("Risk Free Rate : "))
        timeToExpiration = float(input("Time to expiration : "))
        u = float(input("value of u : "))
        d = 1 / u
        numberOfSteps = int(input("Number of steps in process : "))
        expirationPrice = float(input("Expiration price of option : "))

    else:

        with open('Binomial/config.yaml') as file:
            config = yaml.safe_load(file)

        typeOfOption = config.get('typeOfOption')
        initialAssetPrice = config.get('initialAssetPrice')
        riskFreeRate = config.get('riskFreeRate')
        timeToExpiration = config.get('timeToExpiration')
        u = config.get('u')
        d = config.get('d')
        numberOfSteps = config.get('numberOfSteps')
        expirationPrice = config.get('expirationPrice')

    binomial = Binomial(typeOfOption=typeOfOption, initialAssetPrice=initialAssetPrice, riskFreeRate=riskFreeRate,
    timeToExpiration=timeToExpiration,u=u, d=d, numberOfSteps=numberOfSteps, expirationPrice=expirationPrice)

    print("\n-------------------------------\n")
    binomial.option_price()
    print("\n-------------------------------\n")
