import array
import io


class PPMImage:

    def __init__(self, image):
        self.image = ''
        self.magic_number = ''
        self.width = -1
        self.height = -1
        self.max_color_value = 0
        self.raster = []
        if image.endswith(".ppm"):
            self.image = image
            self.readImage()
        else:
            print("Error! Invalid file extension!")

    def writeImage(self, filename):
        header = f'{self.magic_number}\n{self.width} {self.height}\n{self.max_color_value}\n'

        image = array.array('B', self.raster)

        # Save PPM
        with open(filename, 'wb') as f:
            f.write(bytearray(header, 'ascii'))
            image.tofile(f)

    def cleanup(self, str):
        return str.replace("b'", "").replace("\\n'", "")

    def readImage(self):
        with open(self.image, "rb") as f:
            self.magic_number = self.cleanup(str(f.readline()))
            self.width, self.height = str(f.readline()).split(" ")
            self.width = self.cleanup(self.width)
            self.height = self.cleanup(self.height)
            self.max_color_value = self.cleanup(str(f.readline()))

            byte = f.read(1)
            while byte != b"":
                self.raster.append(int.from_bytes(byte, byteorder="big"))
                byte = f.read(1)

    def int2bin(self, order):
        return f'{order:08b}'.format(8)

    def hideData(self, message):
        clean_message = message
        bytelist = []
        for i in range(len(clean_message)):
            bytelist.append(self.int2bin(ord(clean_message[i])))
        bytelist += ['00000000']

        bit_index = 0
        for byte in bytelist:
            for bit in byte:
                if bit == '0':
                    mask = 254 # 0b11111110
                    self.raster[bit_index] = self.raster[bit_index] & mask

                else:
                    mask = 1 # 0b00000001
                    self.raster[bit_index] = self.raster[bit_index] | mask
                bit_index += 1

    def recoverData(self):
        msg = []
        secret = []
        data = []

        # get secret data in binary
        for b in self.raster:
            lsb = bin(b)
            lsb = lsb[-1:]
            data.append(lsb)
            if len(data) == 8:
                if "".join(data) == '00000000':  # end of message!
                    break
                secret.append(data)
                data = []

        # binary to ex
        for s in secret:
            sc = int("".join(s), 2)
            msg.append(chr(sc))

            # print(f's:{s} and sc:{sc}, and msg:{chr(sc)}')
        # todo: clean data after recover

        return "".join(msg)

        # with io.open("test.txt", 'w', encoding='utf8') as f:
        #     f.write("".join(msg))


while True:
    print("What would you like to do?")
    print("a.) Hide a message")
    print("b.) Recover a message")
    print("c.) Exit")

    option = input("Enter your selection: ")
    option = option.strip().lower()

    if option == 'a':
        source = input("Please specify the source PPM filename: ")
        output = input("Please specify the output PPM filename: ")
        phrase = input("Please enter a phrase to hide: ")
        # if success
        ppm = PPMImage(source)
        ppm.hideData(phrase)
        ppm.writeImage(output)

        print("Your message " + phrase + " has been hidden in file: " + output + "\n")
    elif option == 'b':
        source = input("Please specify the source PPM filename: ")
        ppm = PPMImage(source)
        msg = ppm.recoverData()

        print("The following message has been recovered from file " + source + ": " + msg)
    elif option == 'c':
        break
    else:
        print("Invalid option, please try again")

# pp = PPMImage('tests/cat.ppm')
