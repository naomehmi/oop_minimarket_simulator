# PROJECT OOP : MINIMARKET SIMULATOR

## features

- minimarket bisa diupgrade/level up gitu (blm tau gimn)
- memperbanyak jenis produk yang dijual pas level up
- pakai system day gitu (kek day 1, day 2, day 3, dll) main, biar unlimited terus mainnya sampe quit. Jadi sebelum 1 day mulai, karyawan/player bisa 
- ada tutorial dari si pemilik minimarket
- minigame?? (kek tarok diskon gt)
- buang produk yang udah expired
- mau pakek sistem save file gitu keknya tp emcai sih

## classes

1. ***Product*** (ini cuman 1)
    - Property:
        - productCode (self generated?? mau dibuat private kah idk) _string_
        - productName (e.g. "Apple") _string_
        - productPrice (harga) _integer_
        - productCondition (bagus/rusak) _string_
    - Method = -
    - SubClass:
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
        - `pay()`
            - bayar ke kasir
3. ***Employee*** (si player)
    - Property
        - employeeCode (bikin private keknya) _string_
        - employeeName (nama si karyawan/player) _string_
        - employeeDay (kek udah shift kebrp, stlh selesai setiap level +1)
        - employeeLevel
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
        - emcai lagi capek
5. ***Stock*** (ini daftar semua produk gt)
    - Property
        - listOfProducts _dict_ or maybe _2d list_
    - Method
        - `showStock()`
            - tampil semua produk minimarket dalam sebuah tabel

## gameplay

- menu utama
    - play
    - quit
- play
    - starting money = 100.000
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
            - bisa tambah cafe di minimarket mungkin, jadi setelah shift selesai bisa dapat uang ekstra dari penghasilan cafe. Makin dilevel up cafe nya makin byk penghasilannya
            - upgrade max capacity shelf gitu, jadi misal level 1 maks restock 1 produk itu 10 pcs. Level 2 maks 15 pcs, dst
        - mulai shift
            - mulai dari day 1
            - keknya setiap 10 hari level up gt
            - customer datang, randomize isi cart nya
            - baru bayar sm si player
            - aduh prosesnya aku masi blm yakin gimn
