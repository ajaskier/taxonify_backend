import os
import tempfile

from bson import ObjectId
from pandas.errors import EmptyDataError

from aquascope.tests.flask_app_test_case import FlaskAppTestCase
from aquascope.webserver.data_access.util import populate_system_with_items, MissingTsvFileError

DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         '../../../../../data/')


class TestPopulateSystemWithItems(FlaskAppTestCase):

    upload_id = ObjectId('999000000000000000001000')

    def test_can_populate_system_with_valid_data_package(self):
        data_package_path = os.path.join(DATA_PATH, '5p0xMAG_small')
        items_before = self.db.items.count_documents({})
        populate_system_with_items(self.upload_id, data_package_path, self.db, self.app.config['storage_client'])
        items_after = self.db.items.count_documents({})
        self.assertNotEqual(items_before, items_after)

    def test_cant_populate_system_with_invalid_data_package_with_missing_tsv_file(self):
        data_package_path = os.path.join(DATA_PATH, '5p0xMAG_small_missing_tsv')
        items_before = self.db.items.count_documents({})
        with self.assertRaises(MissingTsvFileError):
            populate_system_with_items(self.upload_id, data_package_path, self.db, self.app.config['storage_client'])
        items_after = self.db.items.count_documents({})
        self.assertEqual(items_before, items_after)

    def test_cant_populate_system_with_invalid_data_package_with_fake_image(self):
        data_package_path = os.path.join(DATA_PATH, '5p0xMAG_small_fake_image')
        items_before = self.db.items.count_documents({})
        with self.assertRaises(OSError):
            populate_system_with_items(self.upload_id, data_package_path, self.db, self.app.config['storage_client'])
        items_after = self.db.items.count_documents({})
        self.assertEqual(items_before, items_after)

    def test_cant_populate_system_with_invalid_data_package_with_missing_images(self):
        data_package_path = os.path.join(DATA_PATH, '5p0xMAG_small_missing_images')
        items_before = self.db.items.count_documents({})
        with self.assertRaises(FileNotFoundError):
            populate_system_with_items(self.upload_id, data_package_path, self.db, self.app.config['storage_client'])
        items_after = self.db.items.count_documents({})
        self.assertEqual(items_before, items_after)

    def test_cant_populate_system_with_invalid_data_package_with_no_files_at_all(self):
        with tempfile.TemporaryDirectory() as data_package_path:
            items_before = self.db.items.count_documents({})
            with self.assertRaises(MissingTsvFileError):
                populate_system_with_items(self.upload_id, data_package_path, self.db, self.app.config['storage_client'])
            items_after = self.db.items.count_documents({})
            self.assertEqual(items_before, items_after)

    def test_cant_populate_system_with_invalid_data_package_with_empty_tsv_file_and_no_images(self):
        data_package_path = os.path.join(DATA_PATH, '5p0xMAG_small_empty_tsv_no_images')
        items_before = self.db.items.count_documents({})
        with self.assertRaises(EmptyDataError):
            populate_system_with_items(self.upload_id, data_package_path, self.db, self.app.config['storage_client'])
        items_after = self.db.items.count_documents({})
        self.assertEqual(items_before, items_after)
