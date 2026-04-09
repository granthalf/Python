import sys
from pixels2svg import pixels2svg
import svgwrite

def png_to_svg(input_path: str, output_path: str):
    svg_data = pixels2svg(
        input_path,
        color_tolerance=1,
        remove_background=False,
    )

    # Cas 1 : liste de chaînes
    if isinstance(svg_data, list):
        svg_str = "\n".join(svg_data)

    # Cas 2 : chaîne unique
    elif isinstance(svg_data, str):
        svg_str = svg_data

    # Cas 3 : objet Drawing (ton cas actuel)
    elif isinstance(svg_data, svgwrite.Drawing):
        svg_str = svg_data.tostring()

    else:
        raise TypeError(f"Type de retour inattendu : {type(svg_data)}")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_str)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage : python png2svg.py input.png output.svg")
        sys.exit(1)

    input_png = sys.argv[1]
    output_svg = sys.argv[2]
    png_to_svg(input_png, output_svg)
    print(f"SVG généré : {output_svg}")
