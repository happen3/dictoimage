import ast
import pathlib
import zlib


def pack_image(canvas_path: str):
    """Packs a DictoImage header and a DictoImage image into a .cdim."""
    canvas_path_name = canvas_path
    canvas_hdr_path = pathlib.Path(canvas_path + ".hdr")  # Initialize a path to the Canvas header
    canvas_path = pathlib.Path(canvas_path)  # Initialize a path to the Canvas
    if canvas_path.exists() and canvas_hdr_path.exists():
        with canvas_path.open() as fo:
            canvas_data = ast.literal_eval(fo.read())  # Read the canvas from file
        with canvas_hdr_path.open() as fo:
            canvas_hdr = ast.literal_eval(fo.read())  # Read the canvas header from file

        packed_canvas = str(
            [canvas_hdr, canvas_data]
        )  # Merge the Canvas header and Canvas into a list then convert it to a string.
        compressed_canvas = zlib.compress(packed_canvas.encode())  # Compress the encoded canvas

        with open(canvas_path_name + ".cdim", "wb") as fo:
            fo.write(compressed_canvas)
    else:
        raise FileNotFoundError("Cannot find the header or canvas file. Please check your input.")


def unpack_image(packed_path: str):
    """Unpacks a compressed DictoImage image into its constituent components"""
    canvas_path_name = packed_path
    canvas_path = pathlib.Path(packed_path)  # Initialize a path to the Canvas
    if canvas_path.exists():
        with canvas_path.open("rb") as fo:
            compressed_canvas = fo.read()  # Read the canvas from file

        uncompressed_canvas = zlib.decompress(compressed_canvas).decode()  # Compress the encoded canvas
        uncompressed_canvas = ast.literal_eval(uncompressed_canvas)

        with open(canvas_path_name[:-4], "w") as fo:
            fo.write(str(uncompressed_canvas[1]))
        with open(canvas_path_name[:-4] + "hdr", "w") as fo:
            fo.write(str(uncompressed_canvas[0]))
    else:
        raise FileNotFoundError("Cannot find the compressed canvas file. Please check your input.")
