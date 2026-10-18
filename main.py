import unittest


class SmartLight:
    def __init__(self):
        self.is_on = False
        self.brightness = 0

    def turn_on(self):
        self.is_on = True
        print("Light turned on.")

    def turn_off(self):
        self.is_on = False
        print("Light turned off.")

    def set_brightness(self, level):
        if 0 <= level <= 100:
            self.brightness = level
            print(f"Brightness set to {level}%.")
        else:
            raise ValueError("Brightness must be between 0 and 100.")


# Create an object to test the SmartLight class
light = SmartLight()

light.turn_on()
light.set_brightness(75)
light.turn_off()


# Unit tests
class TestSmartLight(unittest.TestCase):

    def setUp(self):
        self.light = SmartLight()

    def test_turn_on(self):
        self.light.turn_on()
        self.assertTrue(self.light.is_on)

    def test_turn_off(self):
        self.light.turn_on()
        self.light.turn_off()
        self.assertFalse(self.light.is_on)

    def test_set_brightness(self):
        self.light.set_brightness(50)
        self.assertEqual(self.light.brightness, 50)

    def test_invalid_brightness(self):
        with self.assertRaises(ValueError):
            self.light.set_brightness(150)


if __name__ == "__main__":
    unittest.main()