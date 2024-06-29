# Dictoimage framework
# Version 1.0
# Build 1
# 2023 Copyleft happen3, some rights reserved #

class Utilities:
    @staticmethod
    def rgba_to_hex(rgba):
        """Convert RGBA tuple (r, g, b, a) to HEX string."""
        r, g, b, a = rgba
        return '#{:02x}{:02x}{:02x}'.format(r, g, b)

    @staticmethod
    def create_list_of_dicts(size_tuple):
        height, width = size_tuple

        # Creating a list of dictionaries
        list_of_dicts = [{} for _ in range(height * width)]

        return list_of_dicts

    @staticmethod
    def find_next_void_dict(list_of_dicts):
        for idx, d in enumerate(list_of_dicts):
            if not d:  # Check if dictionary is empty (void)
                return idx
        return None  # Return None if no void dictionary is found


class Pixel:
    def __init__(self, rgba_val: tuple, position: tuple):
        """Initialize a DictoPixel element."""
        self.DictoPixel = {
            "HexValue": Utilities.rgba_to_hex(rgba_val),
            "Alpha": rgba_val[3],
            "Position": [
                position[0],
                position[1]
            ]
        }

    def __repr__(self):
        return "DictoPixel Object of length " + str(len(self.DictoPixel)) # Represent the object

    def GetPixel(self):
        return self.DictoPixel

    def GetPixelColour(self):
        return self.DictoPixel["HexValue"]

    def GetPixelPosition(self):
        return self.DictoPixel["Position"]

    def GetPixelTransparency(self):
        return self.DictoPixel["Alpha"]

    def SetPixelColour(self, rgba_val: tuple):
        self.DictoPixel["HexValue"] = Utilities.rgba_to_hex(rgba_val)
        self.DictoPixel["Alpha"] = rgba_val[3]
        return True  # Signal to the user that the event is completed.

    def SetPixelPosition(self, position: tuple):
        self.DictoPixel["Position"] = [
            position[0],
            position[1]
        ]
        return True

    def Destroy(self):
        del self
        return True


class PixelCanvas:
    def __init__(self, size: tuple):
        self.Canvas = Utilities.create_list_of_dicts(size)
        self.CanvasHeader = {
            "Size": size,
            "Format": "DictoImage"
        }

    def AddPixel(self, pixel: dict):
        next_pixel = Utilities.find_next_void_dict(self.Canvas)
        self.Canvas[next_pixel] = pixel
        return True

    def RemovePixel(self, index: int):
        self.Canvas[index] = {}
        return True

    def __repr__(self):
        return f"DictoCanvas object with length {len(self.Canvas)}"

    def GetCanvas(self):
        return self.Canvas

    def SetCanvas(self, canvas: list):
        """Imports new canvas"""
        self.Canvas = canvas
        return True