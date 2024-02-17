meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "CMIIW": "Sebuah kata koreksi",
            "STFU": "tanggapan kepada seseorang supaya dia diam dengan kata kasar",
            "BRUH": "Tanggapan terhadap orang ketika kita mendapat informasi yang tidak sesuai dengan ekspektasi kita",
            }
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    Print("Its not a meme bruh")
