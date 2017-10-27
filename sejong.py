from collections import OrderedDict

priceTotal = 0
# item = OrderedDict([('cabbage', 5000), ('Daikon', 2000), ('Lettuce', 3000)])
item = {'cabbage' : 5000, 'Daikon' : 2000, 'Lettuce' : 3000, 'Pepper' : 4000, 'Cucumber': 1000, 'Pumpkim': 6000, 'Eggplant': 7000}


if __name__ == "__main__":

    totalPrice = 0
    goodsName = [""]
    MAX_BUY = 0
    while True:

        for index, (key, elem) in enumerate(item.items()):
            print(index + 1, key, elem)
        print("*** Item ***")
        print("Select Item (1-7) = ")
        goodsIdx = int(input(""))
        if goodsIdx >= 1 and goodsIdx <= 7:
            print("Input the number of item ({}) : ".format(list(item.keys())[goodsIdx-1]) )
            goodsNum = int(input(""))
            disc_Item = list(item.values())[goodsIdx-1]
            MAX_BUY += 1
            goodsName.append(list(item.keys())[goodsIdx-1])
            if goodsIdx == 1:
                if goodsNum == 1:
                    totalPrice += disc_Item * 0.85
                elif goodsNum >= 2:
                    totalPrice += disc_Item * goodsNum * 0.50
            elif goodsIdx == 2:
                if goodsNum == 1:
                    totalPrice += disc_Item * 0.80
                elif goodsIdx == 2 and goodsNum >= 2:
                    totalPrice += disc_Item * goodsNum * 0.60
            elif goodsIdx == 3:
                if goodsNum == 1:
                    totalPrice += disc_Item * 0.85
                elif goodsIdx == 3 and goodsNum >= 2:
                    totalPrice += disc_Item * goodsNum * 0.70
            elif goodsIdx == 4:
                if goodsNum == 1:
                    totalPrice += disc_Item * 0.90
                elif goodsIdx == 4 and goodsNum >= 2:
                    totalPrice += disc_Item * goodsNum * 0.80
            elif goodsIdx == 5:
                if goodsNum == 1:
                    totalPrice += disc_Item * 0.95
                elif goodsIdx == 5 and goodsNum >= 2:
                    totalPrice += disc_Item * goodsNum * 0.90
            continue
        elif goodsIdx == 0:
            for i in range(1, MAX_BUY+1):
                goodsPrice = item.get(goodsName[i])
                print("장바구니 : ", goodsName[i], "=", goodsPrice)
            print("*** Total Price ***")
            print("Total Price : {}원".format(totalPrice))
            break



