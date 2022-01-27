from psycopg2.errors import CheckViolation
from psycopg2.errors import UniqueViolation

from odoo.tests.common import TransactionCase
from odoo.tools import mute_logger


class GlobalTestCourse(TransactionCase):
    def setUp(self):
        super().setUp()
        self.course = self.env['course']

    def create_course(self, title, description):
        """Global function to create courses"""
        course_id = self.course.create({
            'title': title,
            'description': description,
        })
        return course_id

    @mute_logger('odoo.sql_db')
    def test_01_course_same_name_description(self):
        """Case when course's title is same as course's description: Error sql constraint"""
        with self.assertRaisesRegex(
            CheckViolation,
            'new row for relation "course" violates check constraint "course_check_title_description'
        ):
            self.create_course('test', 'test')

    @mute_logger('odoo.sql_db')
    def test_02_two_courses_same_name(self):
        """Case when the user try to create repeated courses' title: Error sql constraint"""
        with self.assertRaisesRegex(
            UniqueViolation,
            'duplicate key value violates unique constraint "course_title_unique"'
        ):
            self.create_course('test', 'test_description_01')
            self.create_course('test', 'test_description_02')

    def test_03_duplicate_course(self):
        """Case when the user try to copy a course: ideal case"""
        course = self.env.ref('open_academy.course_demo1')
        copy_data = course.copy_data()
        self.course.create(copy_data[0])
        course_copy = self.course.search([('title', '=', copy_data[0]['title'])])
        self.assertRecordValues(course_copy, [{'title': 'Copy of [%s]' % course.title}])
