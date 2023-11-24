from PIL import Image, ImageOps

def mirror_image(input_path, output_path, mirror_type='ambos'):
    original_image = Image.open(input_path)

    if mirror_type == 'vertical':
        mirrored_image = ImageOps.mirror(original_image)
    elif mirror_type == 'horizontal':
        mirrored_image = ImageOps.flip(original_image)
    elif mirror_type == 'ambos':
        mirrored_image = ImageOps.mirror(ImageOps.flip(original_image))
    else:
        raise ValueError("Invalid mirror_type. Use 'vertical', 'horizontal', ou 'ambos'.")

    mirrored_image.save(output_path)

def main():
    input_image_path = input("Escreva o caminho para a imagem: ")

    mirror_type = input("Digite onde quer aplicar o efeito espelho (vertical, horizontal, ou ambos): ").lower()

    while mirror_type not in ['vertical', 'horizontal', 'ambos']:
        print("Invalid mirror type. Please enter 'vertical', 'horizontal', or 'ambos'.")
        mirror_type = input("Enter mirror type (vertical, horizontal, or ambos): ").lower()

    output_path = f"imagem_espelhada_{mirror_type}.jpg"

    mirror_image(input_image_path, output_path, mirror_type)

    print(f"Imagem espelhada {mirror_type} com sucesso. A saída foi salva no {output_path}")

if __name__ == "__main__":
    main()
