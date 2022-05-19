from app import app
import unittest 

class TestCase(unittest.TestCase):

    def test_upload_api(self):
        tester = app.test_client(self)
        response = tester.get("/api/upload")
        statuscode = response.status_code
        self.assertEqual(statuscode,200)

    def test_output_api(self):
        tester = app.test_client(self)
        response = tester.get("/api/output")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_output_return(self):
        tester = app.test_client(self)
        response = tester.get("/api/output")
        self.assertEqual(response.content_type, "application/json")

    def test_output_data(self):
        tester = app.test_client(self)
        response = tester.get("/api/output")
        self.assertTrue(b'src_ip' in response.data)

if __name__ == "__main__":
    unittest.main()