from PIL import Image, ImageOps

class ImageMirror:
    def __init__(self, input_path):
        self.original_image = Image.open(input_path)

    def mirror_image(self, mirror_type='ambos'):
        if mirror_type == 'vertical':
            self.mirrored_image = ImageOps.mirror(self.original_image)
        elif mirror_type == 'horizontal':
            self.mirrored_image = ImageOps.flip(self.original_image)
        elif mirror_type == 'ambos':
            self.mirrored_image = ImageOps.mirror(ImageOps.flip(self.original_image))
        else:
            raise ValueError("Invalid mirror_type. Use 'vertical', 'horizontal', ou 'ambos'.")

    def save_image(self, output_path):
        self.mirrored_image.save(output_path)

def main():
    input_image_path = input("Escreva o caminho para a imagem: ")

    mirror_type = input("Digite onde quer aplicar o efeito espelho (vertical, horizontal, ou ambos): ").lower()

    while mirror_type not in ['vertical', 'horizontal', 'ambos']:
        print("Invalid mirror type. Use 'vertical', 'horizontal', ou 'ambos'.")
        mirror_type = input("Digite onde quer aplicar o efeito espelho (vertical, horizontal, ou ambos): ").lower()

    image_mirror = ImageMirror(input_image_path)
    image_mirror.mirror_image(mirror_type)

    output_path = f"imagem_espelhada_{mirror_type}.jpg"
    image_mirror.save_image(output_path)

    print(f"Imagem espelhada {mirror_type} com sucesso. A saída foi salva no {output_path}")

if __name__ == "__main__":
    main()
