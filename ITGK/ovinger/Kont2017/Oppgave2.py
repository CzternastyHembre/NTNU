def file_to_list(filename):
    try:
        tbl = []
        with open(filename, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                line = line.split()
                for el in line:
                    el = el.strip()
                line[-1] = float(line[-1])
                tbl.append(line)
        return tbl
    except:
        print('Could not read file')


def list_stores(dataList):
    stores = []
    for data in dataList:
        if data[0] not in stores:
            stores.append(data[0])
    return stores

def sum_prices_stores(dataList, storeList):
    prices = []
    for store in storeList:
        sums = 0
        for data in dataList:
            if store in data[0]:
                sums += data[-1]
        prices.append(sums)

    return prices




def rank_stores(storeList, sumStores):
    for i in range(len(sumStores)-1):
        if sumStores[i] > sumStores[i+1]:
            sumStores[i], sumStores[i+1] = sumStores[i+1], sumStores[i]
            storeList[i], storeList[i+1] = storeList[i+1], storeList[i]

    return storeList


def store_analysis(filename):
    dataList = file_to_list(filename)
    stores = list_stores(dataList)
    sum_p = sum_prices_stores(dataList, stores)

    for i in range(len(sum_p)):
        print(stores[i],sum_p[i])
    print()
    ranked = rank_stores(stores, sum_prices_stores(dataList, stores))
    for store in ranked:
        print(store)


store_analysis('pricewar.txt')

