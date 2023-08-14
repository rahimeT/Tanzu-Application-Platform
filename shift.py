def shift_text_right(text, shift_amount):
    lines = text.split('\n')
    shifted_lines = [' ' * shift_amount + line for line in lines]
    shifted_text = '\n'.join(shifted_lines)
    return shifted_text
def main():
    file_path = input("Dosya yolunu girin: ")
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            shift_amount = int(input("Kaç satır sağa kaydırmak istersiniz?: "))
            shifted_text = shift_text_right(content, shift_amount)
            print("Sağa kaydırılmış metin:\n" + shifted_text)
    except FileNotFoundError:
        print("Dosya bulunamadı. Lütfen geçerli bir dosya yolunu girin.")
    except ValueError:
        print("Hatalı giriş. Lütfen geçerli bir sayı girin.")
if __name__ == "__main__":
    main()
