import fitz
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def is_red(color, tolerance=0.1):
    """
    Check if the color is red (RGB) with a given tolerance.
    """
    if color is None:
        return False
    r, g, b = color
    return abs(r - 1) <= tolerance and g <= tolerance and b <= tolerance

def extract_red_dashed_lines(pdf_path):
    doc = fitz.open(pdf_path)
    red_dashed_lines = []

    for page_num, page in enumerate(doc, start=1):
        for d in page.get_drawings():
            color = d.get("color", None)
            dash_pattern = d.get("dash", None)
            print(f"\n--- Page {page_num} ---")
            print("Color:", color)
            print("Dash:", dash_pattern)
            print("Items:", d["items"])
            
            for item in d["items"]:
                print("    item:", item)
                if item[0] == "l":
                    # Extract coords
                    start_point, end_point = item[1], item[2]
                    print("    Line coords:", start_point, end_point)

                    # Now decide if this line is "red dashed"
                    if is_red(color, 0.3):
                        red_dashed_lines.append((start_point, end_point))
                        print("    --> ADDED as red dashed line")

    return red_dashed_lines


def plot_red_dashed_lines(lines, output_image_path):
    plt.figure(figsize=(10, 10))
    ax = plt.gca()

    for line in lines:
        x = [line[0][0], line[1][0]]
        y = [line[0][1], line[1][1]]
        ax.add_line(Line2D(x, y, color='red', linestyle='--'))

    # Force Matplotlib to recalculate the data limits based on the added lines
    ax.relim()
    ax.autoscale_view()

    # Optionally invert the Y-axis if you want PDF-like coordinates
    ax.invert_yaxis()

    # For debugging, it can help to keep the axis on:
    plt.axis('on')  # or 'off' if you prefer no axis lines

    plt.savefig(output_image_path, bbox_inches='tight', dpi=300)
    plt.close()

class PdfProcessor:
    def __init__(self):
        pass

    def process_file(self, pdf_file_path):
        """
        - Extract the red dashed lines
        - Plot them into an image
        - Return the path to the generated image
        """
        output_image_path = "/home/knapo/Desktop/output.png" 

        # Extract red dashed lines
        red_dashed_lines = extract_red_dashed_lines(pdf_file_path)

        # Plot and save as an image
        plot_red_dashed_lines(red_dashed_lines, output_image_path)

        return output_image_path