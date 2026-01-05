from PIL import Image

def create_multi_layer_ico(source_file, output_file):
    try:
        img = Image.open(source_file)
        
        if img.size[0] != img.size[1]:
            print("图片不是正方形，正在自动裁剪")
            min_side = min(img.size)
            left = (img.size[0] - min_side) / 2
            top = (img.size[1] - min_side) / 2
            right = (img.size[0] + min_side) / 2
            bottom = (img.size[1] + min_side) / 2
            img = img.crop((left, top, right, bottom))

        icon_sizes = [(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)]
        
        img.save(output_file, format='ICO', sizes=icon_sizes)
        
        print(f"已生成包含多尺寸图层的图标：{output_file}")
        
    except Exception as e:
        print(f"失败：{e}")

create_multi_layer_ico('logo_original.png', 'game_icon.ico')