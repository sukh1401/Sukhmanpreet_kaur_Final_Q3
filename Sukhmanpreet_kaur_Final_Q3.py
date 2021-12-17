import time


class AnalyzeTriangle:
    firstAngle = None
    firstAngle = None
    firstAngle = None

    def __init__(self):
        pass

    def run(self):
        self.firstAngle = int(input('Enter First Angle: '))
        self.secondAngle = int(input('Enter Second Angle: '))
        self.thirdAngle = int(input('Enter Third Angle: '))
        self.validateTriangle()

    def validateTriangle(self):
        global time
        today = time.strftime("%m/%d/%Y")
        time = time.strftime("%H:%M:%S")
        sum = self.firstAngle+self.secondAngle+self.thirdAngle
        if sum != 180:
            print("The entered angles do not form a triangle.")
        else:
            allAnglesEqual = self.isEquilateral()
            twoAnglesEqual = self.isIsosceles()
            if allAnglesEqual:
                print("The triangle is an equilateral triangle")
            elif twoAnglesEqual:
                print("The triangle is an Isosceles triangle")
            else:
                print("The triangle is a Scalene triangle ")
        print(f"Today's date: {today}, today's time: {time}")

    def isEquilateral(self):
        return self.firstAngle == self.secondAngle == self.thirdAngle

    def isIsosceles(self):
        return self.firstAngle == self.secondAngle or self.secondAngle == self.thirdAngle or self.thirdAngle == self.firstAngle


if __name__ == '__main__':
    app = AnalyzeTriangle()
    app.run()
