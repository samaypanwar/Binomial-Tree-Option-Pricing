import numpy as np
from icecream import ic
from scipy.stats import binom as binomial


class Binomial:
    def __init__(
        self,
        initialAssetPrice,
        riskFreeRate,
        timeToExpiration,
        u,
        d,
        numberOfSteps,
        expirationPrice,
    ):
        self.initialAssetPrice = initialAssetPrice
        self.riskFreeRate = riskFreeRate
        self.timeToExpiration = timeToExpiration
        self.numberOfSteps = numberOfSteps
        self.expirationPrice = expirationPrice
        self.u = u
        self.d = d

    def find_probability(self):

        probabilityOfGoingUp = ((np.exp(self.riskFreeRate * self.timeToExpiration / self.numberOfSteps)
                                - self.d) / (self.u - self.d))

        print(f"The probability of going up is : {probabilityOfGoingUp:.3f}")

        return probabilityOfGoingUp

    def find_endstep_asset_prices(self):

        endStepAssetPrices = []

        for i in range(self.numberOfSteps + 1):

            possibleAssetPrice = (
                (self.u ** i)
                * (self.d ** (self.numberOfSteps - i))
                * self.initialAssetPrice
            )

            endStepAssetPrices.append(possibleAssetPrice)

        print(f"Number of Steps in Process: {self.numberOfSteps}")

        return endStepAssetPrices

    def find_endstep_option_price(self):

        endStepAssetPrices = self.find_endstep_asset_prices()

        endStepOptionPrices = [
            max(possibleAssetPrice - self.expirationPrice, 0)
            for possibleAssetPrice in endStepAssetPrices
        ]

        return endStepOptionPrices

    def option_price(self):

        endStepOptionPrices = self.find_endstep_option_price()
        probability = self.find_probability()
        optionArray = []
        for j, value in enumerate(endStepOptionPrices):
            endstepOption = binomial.pmf(j, self.numberOfSteps, probability)
            optionArray.append(endstepOption)

        futureExpectedValue = sum(optionArray)
        print(f"Future expected value of option: {futureExpectedValue: .3f} Dollars")

        optionPrice = np.exp(-self.riskFreeRate * self.timeToExpiration) * futureExpectedValue
        
        print(f"Price of Option right now: {optionPrice: .3f} Dollars")

        return optionPrice
