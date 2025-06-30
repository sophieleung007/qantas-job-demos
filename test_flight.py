import unittest
class Flight:
    def __init__(self, number, status):
        self.number = number
        self.status = status
    def update_status(self, new_status):
        valid_statuses = ["On Time", "Delayed", "Boarding", "Departed"]
        if new_status in valid_statuses:
            self.status = new_status
            return True
        return False
class TestFlight(unittest.TestCase):
    def setUp(self):
        self.flight = Flight("QF101", "On Time")
    def test_valid_status_update(self):
        self.assertTrue(self.flight.update_status("Boarding"))
        self.assertEqual(self.flight.status, "Boarding")
    def test_invalid_status(self):
        self.assertFalse(self.flight.update_status("In Flight"))
        self.assertEqual(self.flight.status, "On Time")
if __name__ == "__main__":
    unittest.main()
