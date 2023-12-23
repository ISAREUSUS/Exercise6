from PIL import Image
class ImageEditor():
    def __init__(self, filename):
        self.filename = filename
        self.original = None
        self.changed = []
    def open_image(self):
        try:
            self.original = Image.open(self.filename)
        except:
            print('Файл не знайдений!')
        self.original.show()
    def rotate_image(self):
        rotated = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.changed.append(rotated)
        temp_filename = self.filename.split('.')
        new_filename = temp_filename[0]+ str(len(self.changed))+'.png'
        rotated.save(new_filename)
    def croppe_image(self):
        box = (250,100,600,400)
        cropped = self.original.crop(box)
        self.changed.append(cropped)
        temp_filename = self.filename.split('.')
        new_filename = temp_filename[0]+ str(len(self.changed))+'.png'
        cropped.save(new_filename)
MyImage = ImageEditor('VergilDMC5.png')
MyImage.open_image()
MyImage.rotate_image()
MyImage.croppe_image()
for im in MyImage.changed:
    im.show()

