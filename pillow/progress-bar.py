from PIL import Image, ImageDraw

def create_progress_bar(width, height, progress, bg_color, fg_color, outline_color, outline_width, gap, save_path=None):
    """
    Create a progress bar image.

    Args:
        width (int): Width of the progress bar.
        height (int): Height of the progress bar.
        progress (int): Progress as a percentage (0 to 100).
        bg_color (tuple): Background color in RGB format.
        fg_color (tuple): Foreground (progress) color in RGB format.
        outline_color (tuple): Color of the outline in RGB format.
        outline_width (int): Width of the outline.
        gap (int): Gap between the progress bar and the outline.
        save_path (str, optional): Path to save the image. If None, the image is not saved.

    Returns:
        Image: A PIL Image object with the progress bar.
    """
    # Create a new image
    image = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(image)

    # Calculate the width of the progress bar
    progress_width = int((width - 2 * (outline_width + gap)) * (progress / 100))

    # Draw the outline and the filled progress bar
    draw.rectangle(
        [outline_width // 2, outline_width // 2, width - outline_width // 2, height - outline_width // 2],
        outline=outline_color, width=outline_width
    )
    draw.rectangle(
        [outline_width + gap, outline_width + gap,
         outline_width + gap + progress_width, height - outline_width - gap],
        fill=fg_color
    )

    # Save the image if save_path is provided
    if save_path:
        image.save(save_path)

    return image

# #################################################################################################################### #

width, height = 300, 30
progress = 100
bg_color = (51, 51, 51)  # Dark gray
fg_color = (72, 255, 0)  # Neon Green
outline_color = (72, 255, 0)  # Neon Green for the outline
outline_width = 3  # Thickness of the outline
gap = 4  # Gap between the bar and the outline
progress_bar = create_progress_bar(width, height, progress, bg_color, fg_color, outline_color, outline_width, gap)
progress_bar.show()
