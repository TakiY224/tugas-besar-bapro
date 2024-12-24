import flet as ft

def tampilkan_menu_utama(page):
    page.clean()  # Membersihkan halaman
    page.add(
        ft.Text("DAUR BATUAN", size=30, weight="bold"),
        ft.Text("Batuan adalah kumpulan mineral yang telah membeku atau mengkristal dan menjadi bagian utama kerak bumi"),
        ft.Text("Batuan merupakan benda padat yang terbentuk secara alami dan bisa terdiri dari satu atau beberapa jenis mineral"),
        ft.Text("Batuan memiliki beberapa karakteristik, di antaranya: Terdiri dari mineral atau mineraloid, Menjadi penyusun utama materi bumi"),
        ft.Text("Membutuhkan waktu jutaan tahun untuk terbentuk, Memiliki siklus hidup yang panjang, Dapat dimanfaatkan untuk pondasi bangunan"),
        ft.Text("Berdasarkan proses pembentukannya, batuan dibedakan menjadi tiga jenis."),
        ft.Text("Pilih kategori batuan yang ingin Anda pelajari:"),
        ft.Column([
            ft.ElevatedButton("Batuan Beku", on_click=lambda e: batuan_beku(page)),
            ft.ElevatedButton("Batuan Sedimen", on_click=lambda e: batuan_sedimen(page)),
            ft.ElevatedButton("Batuan Metamorf", on_click=lambda e: batuan_metamorf(page)),
            ft.ElevatedButton("Keluar", on_click=lambda e: page.window.close())
        ])
    )

def batuan_beku(page):
    page.clean()
    page.add(
        ft.Text("Pilih jenis batuan beku yang ingin dipelajari:"),
        ft.Column([
            ft.ElevatedButton("Granit", on_click=lambda e: info_batuan_beku(page, "Granit")),
            ft.ElevatedButton("Granodiorit", on_click=lambda e: info_batuan_beku(page, "Granodiorit")),
            ft.ElevatedButton("Diorit", on_click=lambda e: info_batuan_beku(page, "Diorit")),
            ft.ElevatedButton("Andesit", on_click=lambda e: info_batuan_beku(page, "Andesit")),
            ft.ElevatedButton("Gabro", on_click=lambda e: info_batuan_beku(page, "Gabro")),
            ft.ElevatedButton("Basalt", on_click=lambda e: info_batuan_beku(page, "Basalt")),
            ft.ElevatedButton("Batu Kaca/Obsidian", on_click=lambda e: info_batuan_beku(page, "Batu Kaca/Obsidian")),
            ft.ElevatedButton("Batu Apung", on_click=lambda e: info_batuan_beku(page, "Batu Apung")),
            ft.ElevatedButton("Kembali ke Menu Utama", on_click=lambda e: tampilkan_menu_utama(page))
        ])
    )

def info_batuan_beku(page, jenis):
    info = {
        "Granit": ("Granit adalah batuan beku yang terbentuk dari pendinginan magma dalam suhu yang relatif rendah.",
                   "Ciri-ciri: Warnanya bervariasi dari putih, abu-abu, hingga merah muda, dengan butiran kasar.",
                   "Proses pembentukannya adalah berasal dari pendinginan magma di bawah permukaan bumi yang terjadi secara lambat.",
                   "Batu ini biasanya dapat ditemukan di daerah pinggiran pantai, pinggiran sungai, maupun di dasar sungai.",
                   "Pada zaman sekarang, keberadaan batu granit kerap digunakan sebagai bahan bangunan.",
                   "https://lh3.googleusercontent.com/d/1PnThkSok3nKSgOlacUqHp-YMB7ZQfHuI"),
        
        "Granodiorit": ("Granodiorit adalah batuan beku yang mirip dengan granit tetapi mengandung lebih banyak plagioklas.",
                        "Ciri-ciri: Berwarna abu-abu hingga putih dengan butiran kasar.",
                        "Proses pembentukannya terjadi dari pendinginan magma yang kaya akan mineral plagioklas.",
                        "Batuan ini umumnya terbentuk di zona subduksi dan lingkungan tektonik.",
                        "Granodiorit sering digunakan sebagai bahan bangunan dan ornamental.",
                        "https://lh3.googleusercontent.com/d/1fzQBSzEicC3mDwlb9L82USBWWAFuTvLX"),
        
        "Diorit": ("Diorit adalah batuan beku dengan kandungan mineral plagioklas dan beberapa mineral lainnya.",
                   "Ciri-ciri: Berwarna abu-abu hingga hijau dengan butiran kasar.",
                   "Proses pembentukannya adalah berasal dari hasil peleburan lantai samudra yang bersifat mafic.",
                   "Biasanya, batu ini diproduksi pada busur lingkaran vulkanis yang mana membentuk suatu gunung.",
                   "Kegunaan batu diorit adalah sebagai batu ornamen dinding maupun lantai yang ada di bangunan gedung.",
                   "https://lh3.googleusercontent.com/d/1NYn4TCzsSeFHkbAvxHK8SJo8ofOzlhLg"),
        
        "Andesit": ("Andesit adalah batuan beku yang terbentuk dari lava yang mengandung lebih banyak mineral silikat.",
                    "Ciri-ciri: Warna abu-abu hingga coklat dengan butiran lebih halus.",
                    "Proses pembentukannya terjadi dari pendinginan lava di permukaan atau dekat permukaan bumi.",
                    "Batuan ini umum ditemukan di daerah gunung api.",
                    "Andesit sering digunakan sebagai bahan konstruksi dan perkerasan jalan.",
                    "https://lh3.googleusercontent.com/d/15Px4OLpN_UQYoIr04tg_KiC-NeeWN_59"),
        
        "Gabro": ("Gabro adalah batuan beku yang memiliki kandungan mineral yang lebih banyak daripada basalt.",
                  "Ciri-ciri: Berwarna gelap dan memiliki butiran kasar.",
                  "Proses pembentukannya terjadi dari pendinginan magma basa secara lambat di dalam bumi.",
                  "Batuan ini sering ditemukan di dasar samudra dan ophiolite.",
                  "Gabro digunakan sebagai batu hias dan dalam konstruksi.",
                  "https://lh3.googleusercontent.com/d/1C5AUCv0Zl5iFwBHT362HCm8DXPHJZvCR"),
        
        "Basalt": ("Basalt adalah batuan beku yang terbentuk dari pendinginan lava yang cepat.",
                   "Ciri-ciri: Berwarna hitam atau abu-abu gelap dengan butiran halus.",
                   "Proses pembentukannya adalah berasal dari pendinginan lava yang mengandung gas, tetapi gasnya telah meluap.",
                   "Batuan ini umum ditemukan di dasar laut dan daerah vulkanik.",
                   "Batu basalt digunakan sebagai bahan pondasi bangunan misalnya gedung, jembatan, dan jalan raya.",
                   "https://lh3.googleusercontent.com/d/13MW6IdVTrlXjOItCX5LGqwaq4J4br7lI"),
        
        "Batu Kaca/Obsidian": ("Obsidian adalah batuan beku yang terbentuk dari pendinginan lava yang sangat cepat.",
                               "Ciri-ciri: Bersifat kaca, sangat tajam, dan berwarna hitam.",
                               "Proses terbentuknya adalah berasal dari lava permukaan yang mendingin secara cepat.",
                               "Batuan ini sering ditemukan di daerah gunung api.",
                               "Batu obsidian kerap digunakan sebagai kerajinan dan alat pemotong.",
                               "https://lh3.googleusercontent.com/d/1WoPUhbJf6b8rBL_e_NoP_fBpYZ6ZgqMj"),
        
        "Batu Apung": ("Batu apung adalah batuan beku yang sangat ringan karena mengandung banyak gelembung gas.",
                       "Ciri-ciri: Berwarna abu-abu atau hitam, ringan dan dapat mengapung di air.",
                       "Proses terbentuknya adalah berasal dari pendinginan magma yang berbentuk gelembung-gelembung gas.",
                       "Batuan ini terbentuk dari letusan gunung api yang kaya akan gas.",
                       "Batu apung digunakan sebagai bahan pengisi, isolator temperatur tinggi, dan untuk mengamplas.",
                       "https://lh3.googleusercontent.com/d/19kF2iiQKlKSJSaKD9UfdlH5vZcviuPbd")
    }
    page.clean()
    page.add(
       ft.Text(f"Informasi tentang {jenis}:"),
        ft.Text(info[jenis][0]),
        ft.Text(info[jenis][1]),
        ft.Text(info[jenis][2]),
        ft.Text(info[jenis][3]),
        ft.Text(info[jenis][4]),
        ft.Image(src=info[jenis][5], width=300),
        ft.ElevatedButton("Kembali", on_click=lambda e: batuan_beku(page))
    )

def batuan_sedimen(page):
    page.clean()
    page.add(
        ft.Text("Pilih jenis batuan sedimen yang ingin dipelajari:"),
        ft.Column([
            ft.ElevatedButton("Breksi", on_click=lambda e: info_batuan_sedimen(page, "Breksi")),
            ft.ElevatedButton("Konglomerat", on_click=lambda e: info_batuan_sedimen(page, "Konglomerat")),
            ft.ElevatedButton("Sandstone", on_click=lambda e: info_batuan_sedimen(page, "Sandstone")),
            ft.ElevatedButton("Shale", on_click=lambda e: info_batuan_sedimen(page, "Shale")),
            ft.ElevatedButton("Limestone", on_click=lambda e: info_batuan_sedimen(page, "Limestone")),
            ft.ElevatedButton("Saltstone", on_click=lambda e: info_batuan_sedimen(page, "Saltstone")),
            ft.ElevatedButton("Gipsum", on_click=lambda e: info_batuan_sedimen(page, "Gipsum")),
            ft.ElevatedButton("Coal", on_click=lambda e: info_batuan_sedimen(page, "Coal")),
            ft.ElevatedButton("Kembali ke Menu Utama", on_click=lambda e: tampilkan_menu_utama(page))
        ])
    )

def info_batuan_sedimen(page, jenis):
    info = {
       "Breksi": ("Breksi adalah batuan sedimen yang terbentuk dari fragmen batuan yang kasar.",
                   "Ciri-ciri: Terdiri dari fragmen kasar yang terikat matriks halus.",
                   "Proses terbentuknya adalah berasal dari letusan gunung berapi yang terlempar tinggi ke udara, kemudian mengendap di suatu tempat",
                   "Keberadaan batu ini biasanya dijadikan sebagai kerajinan dan bahan bangunan.",
                   "https://lh3.googleusercontent.com/d/1fv4Qc5Qy0In5evvhRBVf-s1SHyuri-LT"),
        
        "Konglomerat": ("Konglomerat adalah batuan sedimen yang tersusun dari fragmen batuan bulat.",
                        "Ciri-ciri: Terdiri dari butiran bulat yang lebih besar daripada pasir.",
                        "Proses pembentukannya adalah berasal dari bahan-bahan yang lepas akibat gaya berat sehingga menjadikannya lebih padat dan terikat.",
                        "Biasanya, batu jenis ini digunakan sebagai bahan bangunan.",
                        "https://lh3.googleusercontent.com/d/1bWPTsOTQVsFY2EdzxTe8uej4Z2z7dHrn"),
        
        "Sandstone": ("Sandstone adalah batuan sedimen yang terdiri dari butiran pasir yang terikat bersama.",
                      "Ciri-ciri: Berwarna kuning, merah, atau coklat, dan terasa kasar.",
                      "Proses pembentukannya berasal dari pengendapan butiran pasir yang terkonsolidasi.",
                      "Batu ini sering digunakan dalam konstruksi dan arsitektur.",
                      "https://lh3.googleusercontent.com/d/1tJGtv63SXz9d3y1fcYdSivJ1t7wHb8Mh"),
        
        "Shale": ("Shale adalah batuan sedimen halus yang terbentuk dari lapisan tanah liat.",
                  "Ciri-ciri: Halus, berlapis, dan mudah pecah.",
                  "Proses pembentukannya berasal dari pengendapan partikel tanah liat dalam lingkungan yang tenang.",
                  "Shale memiliki berbagai kegunaan dalam industri konstruksi dan pembuatan keramik.",
                  "https://lh3.googleusercontent.com/d/1CAlqHC4PIFzSelU-8L-OT2K7NotieK9R"),
        
        "Limestone": ("Limestone adalah batuan sedimen yang terbentuk dari kalsium karbonat.",
                      "Ciri-ciri: Berwarna putih, abu-abu, atau kuning, dan terasa keras.",
                      "Proses pembentukannya berasal dari pengendapan sisa-sisa organisme laut.",
                      "Batu kapur banyak digunakan dalam industri semen dan konstruksi.",
                      "https://lh3.googleusercontent.com/d/14GO7xXeowhGDSh9L4-7CQ_PkuATE1Qmb"),
        
        "Saltstone": ("Saltstone adalah batuan sedimen yang sebagian besar terdiri dari garam.",
                      "Ciri-ciri: Biasanya putih atau transparan dan mudah larut dalam air.",
                      "Proses pembentukannya berasal dari penguapan air laut dalam cekungan tertutup.",
                      "Batuan ini penting dalam industri garam dan kimia.",
                      "https://lh3.googleusercontent.com/d/1BBMB3yuSFFYXPRrdGTa0HQVa5Oqqe4Rq"),
        
        "Gipsum": ("Gipsum adalah batuan sedimen yang terbentuk dari pengendapan kalsium sulfat.",
                   "Ciri-ciri: Berwarna putih atau transparan, lunak dan mudah dipotong.",
                   "Proses pembentukannya berasal dari penguapan air laut atau danau asin.",
                   "Gipsum banyak digunakan dalam industri konstruksi dan pembuatan plester.",
                   "https://lh3.googleusercontent.com/d/1FKBIMOI2l-lizZ-fF8cQA6WSZOTlboMc"),
        
        "Coal": ("Coal atau batubara adalah batuan sedimen organik yang terbentuk dari tumbuhan.",
                 "Ciri-ciri: Berwarna hitam, dapat terbakar, dan berlapis-lapis.",
                 "Proses pembentukannya berasal dari pembusukan material tumbuhan dalam kondisi anaerobik.",
                 "Batubara merupakan sumber energi fosil yang penting.",
                 "https://lh3.googleusercontent.com/d/1jk2s3t0bucRhWLbS90e-WQsJUieBONvD")
    }
    page.clean()
    page.add(
        ft.Text(f"Informasi tentang {jenis}:"),
        ft.Text(info[jenis][0]),
        ft.Text(info[jenis][1]),
        ft.Text(info[jenis][2]),
        ft.Text(info[jenis][3]),
        ft.Image(src=info[jenis][4], width=300),
        ft.ElevatedButton("Kembali", on_click=lambda e: batuan_sedimen(page))
    )

def batuan_metamorf(page):
    page.clean()
    page.add(
        ft.Text("Pilih jenis batuan metamorf yang ingin dipelajari:"),
        ft.Column([
            ft.ElevatedButton("Quartzite/Kuarsit", on_click=lambda e: info_batuan_metamorf(page, "Quartzite/Kuarsit")),
            ft.ElevatedButton("Hornfels", on_click=lambda e: info_batuan_metamorf(page, "Hornfels")),
            ft.ElevatedButton("Schist/Sekis", on_click=lambda e: info_batuan_metamorf(page, "Schist/Sekis")),
            ft.ElevatedButton("Gneiss", on_click=lambda e: info_batuan_metamorf(page, "Gneiss")),
            ft.ElevatedButton("Slate", on_click=lambda e: info_batuan_metamorf(page, "Slate")),
            ft.ElevatedButton("Fillit/Phylite", on_click=lambda e: info_batuan_metamorf(page, "Fillit/Phylite")),
            ft.ElevatedButton("Marmer/Marble", on_click=lambda e: info_batuan_metamorf(page, "Marmer/Marble")),
            ft.ElevatedButton("Milonit", on_click=lambda e: info_batuan_metamorf(page, "Milonit")),
            ft.ElevatedButton("Filonit", on_click=lambda e: info_batuan_metamorf(page, "Filonit")),
            ft.ElevatedButton("Serpetinit", on_click=lambda e: info_batuan_metamorf(page, "Serpetinit")),
            ft.ElevatedButton("Kembali ke Menu Utama", on_click=lambda e: tampilkan_menu_utama(page))
        ])
    )

def info_batuan_metamorf(page, jenis):
    info = {
        "Quartzite/Kuarsit": ("Quartzite adalah batuan metamorf yang terbentuk dari perubahan pasir kuarsa.",
                              "Ciri-ciri: Keras, berkilau, dan berwarna putih atau abu-abu.",
                              "Proses pembentukannya terjadi ketika batupasir mengalami metamorfosis akibat tekanan dan suhu tinggi.",
                              "Dalam proses ini, butiran pasir melebur bersama membentuk tekstur yang sangat padat.",
                              "Batuan ini sering digunakan sebagai bahan bangunan dan material dekoratif.",
                              "https://lh3.googleusercontent.com/d/1Z1g4W26xQx-vsQ06iKF_-J8Qojwi_SzV"),
        
        "Hornfels": ("Hornfels adalah batuan metamorf yang terbentuk akibat panas tinggi.",
                     "Ciri-ciri: Keras, halus, dan berwarna gelap.",
                     "Proses pembentukannya terjadi ketika batuan mengalami kontak dengan magma panas.",
                     "Perubahan ini menghasilkan tekstur yang sangat halus dan padat.",
                     "Hornfels sering digunakan dalam konstruksi dan sebagai batu hias.",
                     "https://lh3.googleusercontent.com/d/1YVklQed2XAZkDGA_iS8mouAJCXgWjy0b"),
        
        "Schist/Sekis": ("Schist adalah batuan metamorf yang terbentuk dari perubahan batuan sedimen.",
                         "Ciri-ciri: Terdapat banyak lapisan mineral, berkilau, dan mudah dibelah.",
                         "Proses pembentukannya melibatkan tekanan yang tinggi dan suhu menengah.",
                         "Mineral-mineral dalam batuan tersusun sejajar membentuk lapisan-lapisan.",
                         "Batuan ini sering digunakan dalam landscaping dan konstruksi.",
                         "https://lh3.googleusercontent.com/d/12w1xcCimLqNiRaO8dNBtsVSy8_I8B0eW"),
        
        "Gneiss": ("Gneiss adalah batuan metamorf yang terbentuk dari perubahan granit.",
                   "Ciri-ciri: Memiliki lapisan mineral yang terlihat jelas, berwarna terang hingga gelap.",
                   "Proses pembentukannya terjadi pada suhu dan tekanan yang sangat tinggi.",
                   "Mineral-mineral dalam batuan tersegregasi membentuk pita-pita yang jelas.",
                   "Gneiss sering digunakan sebagai bahan bangunan dan ornamen.",
                   "https://lh3.googleusercontent.com/d/1M0wPc30edkUnKrlGXFN55arMinxQauMx"),
        
        "Slate": ("Slate adalah batuan metamorf yang terbentuk dari shale.",
                  "Ciri-ciri: Dapat dibelah menjadi lembaran tipis, berwarna abu-abu atau hitam.",
                  "Proses pembentukannya terjadi pada tekanan rendah hingga menengah.",
                  "Mineral lempung dalam batuan tersusun sejajar membentuk bidang belah.",
                  "Slate banyak digunakan sebagai material atap dan lantai.",
                  "https://lh3.googleusercontent.com/d/1M5ijZ6fCsuKorkmH6WzpFvqXIPZUMg_M"),
        
        "Fillit/Phylite": ("Fillit adalah batuan metamorf yang terbentuk dari shale.",
                           "Ciri-ciri: Halus dan mengkilap, berwarna abu-abu atau hijau.",
                           "Proses pembentukannya terjadi pada tingkat metamorfisme yang lebih tinggi dari slate.",
                           "Mineral mika dalam batuan tumbuh lebih besar memberikan kilap khas.",
                           "Batuan ini sering digunakan dalam konstruksi dan dekorasi.",
                           "https://lh3.googleusercontent.com/d/1Jqd2Vo3ox7OwEBQKv01851Ub_BG82VYB"),
        
        "Marmer/Marble": ("Marmer adalah batuan metamorf yang terbentuk dari perubahan batu kapur.",
                          "Ciri-ciri: Mengkilap, keras, dan berwarna putih atau beraneka warna.",
                          "Proses pembentukannya melibatkan rekristalisasi kalsit pada suhu tinggi.",
                          "Proses ini menghasilkan tekstur kristal yang khas dan indah.",
                          "Marmer banyak digunakan sebagai material konstruksi mewah dan seni pahat.",
                          "https://lh3.googleusercontent.com/d/1z5bm8fPhLcTx72OW_rRz1Woby9nAI6vZ"),
        
        "Milonit": ("Milonit adalah batuan metamorf yang terbentuk dari tekanan dan gesekan.",
                    "Ciri-ciri: Keras, sering berwarna gelap, dan terdapat mineral halus.",
                    "Proses pembentukannya terjadi di zona sesar dengan deformasi yang intensif.",
                    "Batuan mengalami penggerusan dan rekristalisasi selama pembentukan.",
                    "Milonit penting dalam studi struktur geologi dan tektonik.",
                    "https://lh3.googleusercontent.com/d/1ZitAMZ18nwYFiBXuRcuYMs1Cpl_0pZu0"),
        
        "Filonit": ("Filonit adalah batuan metamorf yang terbentuk akibat tekanan rendah.",
                    "Ciri-ciri: Keras dan berwarna hijau atau abu-abu.",
                    "Proses pembentukannya terjadi pada zona deformasi dengan tekanan rendah.",
                    "Mineral-mineral mengalami perubahan dan penyusunan ulang.",
                    "Batuan ini memiliki nilai penting dalam studi geologi struktur.",
                    "https://lh3.googleusercontent.com/d/1Ae4NROX5HCFBSeL9EM798afARRdcYnTK"),
        
        "Serpetinit": ("Serpetinit adalah batuan metamorf yang terbentuk dari mineral olivin.",
                       "Ciri-ciri: Berwarna hijau, mengandung serpentin.",
                       "Proses pembentukannya melibatkan hidrasi mineral olivin dan piroksen.",
                       "Transformasi ini biasanya terjadi di dasar laut atau zona subduksi.",
                       "Serpentinit digunakan sebagai batu hias dan dalam industri konstruksi.",
                       "https://lh3.googleusercontent.com/d/1HbQSJ2A3n6d7cgEcfBrqmD7pJKujZbkN")
    }
    page.clean()
    page.add(
        ft.Text(f"Informasi tentang {jenis}:"),
        ft.Text(info[jenis][0]),
        ft.Text(info[jenis][1]),
        ft.Text(info[jenis][2]),
        ft.Text(info[jenis][3]),
        ft.Text(info[jenis][4]),
        ft.Image(src=info[jenis][5], width=300),
        ft.ElevatedButton("Kembali", on_click=lambda e: batuan_metamorf(page))
    )

def main(page):
    tampilkan_menu_utama(page)

ft.app(target=main)