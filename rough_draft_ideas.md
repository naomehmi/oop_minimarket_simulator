# PROJECT OOP : MINIMARKET SIMULATOR

## features

- minimarket bisa diupgrade/level up gitu (blm tau gimn)
- memperbanyak jenis produk yang dijual pas level up
- pakai system day gitu (kek day 1, day 2, day 3, dll) main, biar unlimited terus mainnya sampe quit. Jadi sebelum 1 day mulai, karyawan/player bisa 
- ada tutorial dari si pemilik minimarket
- buang produk yang udah expired
- gameplay nya diinspirasi dari 'supermarket cashier', coba kelen tes install di playstore AWKWKKW
- jujur setelah membaca2 ulg apa yg kutulis, kayaknya bakal susah si gaiz rip, klo ada ide yg lebi sederhana tulis aja

## classes

1. ***Product*** (ini cuman 1)
    - Property:
        - productCode (self generated?? mau dibuat private kah idk) _string_
        - productName (e.g. "Apple") _string_
        - productPrice (harga) _integer_
        - productUOM (satuan unit, kek misal pcs/ltr/mtr/dll) _string_
        - productCondition (bagus/rusak) _string_
    - Method = -
    - SubClass (ni nnt M02 ada belajar ttg inheritance gitu):
        1. **consumable** (produk yang bisa kadaluarsa cth: buah-buahan)
            - Property:
                - productExpDate (tgl kadaluarsa) _string_
            - Method = -
        2. **nonConsumable** (produk yang gak ada kadaluarsa cth: kursi)
            - Property = -
            - Method = -
2. ***Customer***
    - Property: 
        - customerName _string_
        - customerCart (keranjang customer cth {class produk : qty}) _dict_
    - Method
        - `fillCart()`
            - randomized
            - diisi produk yg ada di minimarketnya di dalam cart nya
            - keknya bakal susah si coding ini T-T
        - `pay()`
            - bayar ke kasir
3. ***Employee*** (si player)
    - Property
        - employeeCode (bikin private keknya) _string_
        - employeeName (nama si karyawan/player) _string_
    - Method
        - `restock()`
            - minigame gitu
            - jadi kek buang produk expired
            - isi ulang produk yg udah mau habis stock
            - jadi keknya produk bisa diupgrade untuk increase harganya dan uang itu bisa digunakan untuk upgrade minimarket
        - `cashier()`
            - game utama
            - jadi diinspirasi oleh game 'supermarket cashier'
            - gimana ya scan produk, blm tau
4. ***Minimarket***
    - Property
        - minimarketMoney (total uang si player utk restock uang/level minimarket, klo udh 0 atau minus game over mungkin)
        - minimarketCustomers (jlh customer per level gt) _list_
        - minimarketLevel _int_
        - minimarketDay (kek udah main sampe day berapa gt) _int_
5. ***Stock*** (ini daftar semua produk gt)
    - Property
        - listOfProducts _dict or maybe 2d list, blm tau soalnya ni cuman bacot2 dulu ide_
        - stockMaxCapacity _int_ , qty maksimal restock 1 produk (biar user gak input terlalu byk)
    - Method
        - `showStock()`
            - tampil semua produk minimarket dalam sebuah tabel
        - `restock()`
            - sebelum mulai level, si player boleh cek stock. Klo barang gk ada stock nnt customernya mana bs belanja :V
            - jadi misal produk apel sisa 2 pcs, jadi si player bisa memilih untuk restock apel sebyk 7 pcs
            -  terus si player bisa buang produk yg udah exp atau rusak

## gameplay

- menu utama
    - play
    - quit
- play
    - starting money = $1000
    - user input nama mereka
        - bikin keyword yang tidak diperboleh (mis angka-angka gt)
        - maks 20 karakter
    - sblm shift/level mulai, ada kek submenu
        - klo baru pertama kali main ada dialog tutorial gitu dari si om om manager
        - check stock
            - filter produk (minigame gitu, buang produk yg udah expired (max 1 minggu sblm hari shift))
            - boleh pesan produk yang udah mau habis stock
            - klo level up bisa unlock produk baru yg dijual (harga lbh mahal ofc)
        - upgrade minimarket
            - bisa tambah cafe di minimarket mungkin, jadi setelah shift selesai bisa dapat uang ekstra dari penghasilan cafe. Makin dilevel up cafe nya makin byk penghasilannya. soalnya kan minimarket/supermarket cth brastagi, ada cafe, giveaway la, dll.
            - upgrade max capacity shelf gitu (class Stock), jadi misal level 1 maks restock 1 produk itu 10 pcs. Level 2 maks 15 pcs, dst
        - mulai shift
            - mulai dari day 1
            - keknya setiap 2-3 hari level up gt ?? atau mien pakek level ya bikin ribet aja AWKWKWKWK
            - customer datang, randomize isi cart nya
            - mungkin bisa bikin game simpel aja gitu
                - mis customer udah mau bayar ini
                - player boleh tekan `x` untuk scan barcode
                - klo gk ada barcode, player mungkin bisa ketik harga secara manual, mirip game supermarket cashier di hpku AWKWKWK
                - terus setelah semua barang discan, player tekan `t` untuk totalin semua harganya
                - abis itu, customer bayar, random uangnya
                - jadi kita harus kasi kembalian kek brp lbr uang 100, brp lbr uang 50, dll (keknya pakek dolar lebih mudah dibanding rupiah)
                - abis itu klik `r` biar kasi struk untuk si customer ?? boi cai
- mungkin sblm quit bisa liat progress player kek udah main sebrp lama, sisa uang, jlh customer yg udh dilayani, dsb
- produk yg dijual
    - apel => lvl 1
    - susu => lvl 1
    - telur => lvl 2
    - tisu => lvl 3
    - minyak goreng => lvl 5
    - kursi kayu => lvl 6
    - meja kayu => lvl 7
    - beras => lvl 8
