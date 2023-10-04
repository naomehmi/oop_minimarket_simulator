# CODE NOTES

*** pas edit file ini, bikin kode pakek inisial di akhir paragraf jadi bisa tau siapa2 aja yang udah berkontribusi.

(4/10/23) saya suggest demo dulu codenya di laptop kalian. Aku udah sediakan tutorial singkat untuk game kita, biar nanti kalian bisa ngerti penjelasanku di bawah _- N_

## file minimarketClasses.py

### product class

```
from time import sleep
from random import randrange

class product:
    def __init__(self, productCode, productName, productPrice, productUOM, productCondition):
        self.productCode = productCode
        self.productName = productName
        self.productPrice = productPrice
        self.productUOM = productUOM
        self.productCondition = productCondition
```

Ini class produk. Keknya nama property nya boleh kupendekin, kek dari `self.productCode` jadi `self.code` doang, biar hemat tenaga jari. Propertinya ada kodenya, itu nanti dirandom aja, abis itu ada nama produk, harga, satuan unit, dan kondisinya masi bagus/rusak. Nah, aku juga terpikir untuk membuat kelas ini abstrak, karena aku sering silap pakek kelas ini padahal gabole, cuman bisa pakek consumable sm nonConsumable kita. Gimana menurut kelen? _- N_

<hr>

### consumable and nonConsumable classes

```
class consumable(product):
    def __init__(self, productCode, productName, productPrice, productUOM, productCondition, productExpDate):
        super().__init__(productCode, productName, productPrice, productUOM, productCondition)
        self.productExpDate = productExpDate

class nonConsumable(product):
    def __init__(self, productCode, productName, productPrice, productUOM, productCondition):
        super().__init__(productCode, productName, productPrice, productUOM, productCondition)
```

Ini dua adlh child dari class produk. Consumable untuk produk yg bisa expired kek makanan, klo nonConsumable untuk produk yg gk bs expired. Sejauh ini masi blm ada method, karena kek emg produknya bs ngapain T-T. Saya juga stuggle si buat exp date sm product condition, karena untuk exp aku agak bingung gimana randomize tgl nya, jadi di main program utk sementara aku bikin semua '1 week', nnt kalian mikir dulu idenya. Abis itu utk product condition, aku bikin ada 1 dlm 9 kemungkinan dia bad, sisanya good. di main program ada kutulis, tp keknya mending aku pindahin ke sini aja gak sih. _- N_

<hr>

### customer class

```
class customer:
    def __init__(self, customerName, customerCart):
        self.customerName = customerName
        self.customerCart = customerCart
    def fillCart(self):
        pass
    def pay(self):
        pass
```

Class customer, untuk pelanggan minimarket kita. Jadi cart saya kepikir bikin tipe datanya dictionary saja, kek cth {apel : 2 pcs, susu : 2pcs} gitu. nanti bakal randomize utk method fillCart() untuk isi produk2nya, dan kita harus pastikan gak bakal ngebug kek misal ambil apel 10 pcs padahal stock hanya tersedia 5 gitu. Bakal susah sepertinya, tp kita gak boleh nyerah. Untuk method pay, itu blm 100% yakin, itu biar trigger menjalankan method cashier() si employee, nanti kujelasin di bagian class employee _- N_

<hr>

### employee Class

```
class employee:
    def __init__(self, employeeCode, employeeName):
        self.employeeCode = employeeCode
        self.employeeName = employeeName
    def cashier(self):
        pass
```

Untuk class employee, cashier saya kepikir untuk ikut game ini di play store, namanya Supermarket Cashier. Jadi sistem gamenya, kita jadi kasir gitu input2, abis itu kasi kembalian berapa lbr 10rb, berapa lbr 5rb, harus uang pas untuk kembaliannya. Pakek while() seharusnya bisa lah buat method ini. Untuk demo bisa lihat di foto yg w udah lampirkan di github, yang ada skema2 (buriq si tulisannya, but kira2 aja lah itu blm pasti). _- N_

<hr>

### minimarket class

```
class minimarket:
    def __init__ (self, minimarketMoney, minimarketCustomers, minimarketLevel, minimarketDay):
        self.minimarketMoney = minimarketMoney
        self.minimarketCustomers = minimarketCustomers
        self.minimarketLevel = minimarketLevel
        self.minimarketDay = minimarketDay
```

Saya kepikir untuk class minimarket bisa level up gitu, terus sehari berapa customers, bla bla bla. money ya sisa uang seluruh minimarket, customer itu jumlah customer per hari, abis itu ada level (dimana klo udah naik bisa unlock lebih banyak item), terus day itu untuk hitung udah berapa lama si player main game ini. _- N_

<hr>

### stock class

ini bakal kupecahin jadi bbrp bagian karena ane padat si methodnya. _- N_

```
class stock:
    def __init__ (self, listofProducts, stockMaxCapacity):
        self.listofProducts = listofProducts
        self.stockMaxCapacity = stockMaxCapacity
```

Ini deklarasi property doang. jadi listOfProducts itu untuk tampilin dalam tabel semua produk kita, abis itu stockMaxCapacity buat jumlah maksimum per produk yang bisa dijual. Biar bisa menghindari player nya beli kek 1000000000 apel misalnya. Nanti per level bisa dinaikkan juga jumlahnya.

```
    def showStock(self,unlocked,tutorial=False):
        def printProducts():
            print("-"*60)
            print("|{:^3}|{:^15}|{:^12}|{:^25}|".format("No.","Product Name", "Total Stock","Price per Unit (USD)"))
            print("|{:^3}|{:^15}|{:^12}|{:^25}|".format("-"*3,"-"*15,"-"*12,"-"*25))
            for i in range(unlocked):
                print("|{:^3}|{:^15}|{:^12}|{:^25}|".format(i+1, self.listofProducts[i][0].productName, str(len(self.listofProducts[i]))+" "+self.listofProducts[i][0].productUOM,self.listofProducts[i][0].productPrice))
                i += 1
            print("-"*60)
            print()
            print(f"Press '0' to go back to the main menu, or press a number between 1-{unlocked} to check each item of the product.")
        printProducts()
        interact = ""
        while interact != "0" or interact > str(unlocked) or interact < "0":
            if tutorial:
                print(f"Let's try to check our apples. Since apple is on the No. '1' row, press '1'")
            interact = input("=> ")
            if tutorial:
                if interact != "1":
                    print("=> Press '1' to continue the tutorial.")
                    continue
            if "1" <= interact <= str(unlocked):
                if tutorial:
                    self.restock(int(interact)-1,True)
                    printProducts()
                    if tutorial:
                        print("=> Press 0 to return to the previous menu")
                    tutorial = False
                else:
                    self.restock(int(interact)-1)
            elif interact == "0":
                break
            else:
                print("=> there is no product with that number. Try again.")
```

def printProducts() untuk tampilkan dalam bentuk tabel. klo kalian ada nampak `if tutorial:` itu artinya klo misal lagi mode tutorial (alias `tutorial = True`), kodenya dijalankan. Tapi klo mode normal (`tutorial = False`), bagian kode itu diskip aja biar gak berbelit2. Jadi per baris ada setiap jenis produk yg dijual misal apel, susu, dsb. Jadi player tinggal ketik barisan yang mana yang ingin dicek secara detail. nanti di method restock() baru bisa kek hapus produk, beli produk, dll. _- N_
