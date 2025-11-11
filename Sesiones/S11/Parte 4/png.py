from PIL import Image, ImageDraw, ImageFont
import math

def add_labels_to_wheel(
    wheel_path,
    output_path,
    names,
    center=None,
    radius_factor=0.65,
    font_size=40
):
    img = Image.open(wheel_path).convert("RGBA")
    W, H = img.size

    if center is None:
        cx, cy = W // 2, H // 2
    else:
        cx, cy = center

    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("Arial.ttf", font_size)
    except:
        font = ImageFont.load_default()

    radius = int(min(W, H) * radius_factor / 2)

    for t, name in enumerate(names):

        angle_deg = 15 + 30 * t
        angle_rad = math.radians(angle_deg)

        x = cx + radius * math.cos(angle_rad)
        y = cy + radius * math.sin(angle_rad)

        # Compute text bounding box (replacement for textsize)
        bbox = draw.textbbox((0, 0), name, font=font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]

        text_img = Image.new("RGBA", (tw + 10, th + 10), (255, 255, 255, 0))
        text_draw = ImageDraw.Draw(text_img)
        text_draw.text((5, 5), name, font=font, fill="black")

        # Rotate text so it's radial
        rotate_deg = angle_deg + 90
        rotated = text_img.rotate(-rotate_deg, expand=True)

        img.paste(rotated,
                  (int(x - rotated.width / 2),
                   int(y - rotated.height / 2)),
                  rotated)

    img.save(output_path)
    print("Saved:", output_path)


# Example usage
if __name__ == "__main__":
    players = ["Juan", "Cristian", "Wendy", "Sebastián"]*3

    add_labels_to_wheel(
        wheel_path="Sesiones/S11/Parte 4/resources/rainbow-spinning-wheel-png.png",
        output_path="Sesiones/S11/Parte 4/resources/named_wheel.png",
        names=players
    )
