from psycopg2.errors import NotNullViolation

from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError
from odoo.tools import mute_logger


class GlobalTestSession(TransactionCase):
    def setUp(self):
        super().setUp()
        self.session = self.env["session"]
        self.course = self.env.ref('open_academy.course_demo1')
        self.partner_1 = self.env.ref('base.res_partner_1')

    def create_session(self, name, course_id, instructor_id, attendee_ids, number_seat):
        """Global function to create sessions"""
        session_id = self.session.create({
            'name': name,
            'course_id': course_id,
            'instructor_id': instructor_id,
            'attendee_ids': [(6, 0, [attendee_ids])],
            'number_seat': number_seat,
        })
        return session_id

    @mute_logger('odoo.sql_db')
    def test_01_session_no_name(self):
        """Case when session have no name: Error sql constraint"""
        with self.assertRaisesRegex(
            NotNullViolation,
            'null value in column "name" of relation "session" violates not-null constraint'
        ):
            self.create_session(None, self.course.id, None, None, 5)

    @mute_logger('odoo.sql_db')
    def test_02_session_no_course(self):
        """Case when session have no course_id: Error sql constraint"""
        with self.assertRaisesRegex(
            NotNullViolation,
            'null value in column "course_id" of relation "session" violates not-null constraint'
        ):
            self.create_session('test', None, None, None, 5)

    @mute_logger('odoo.sql_db')
    def test_03_session_no_number_seat(self):
        """Case when session have no number_seat: Error sql constraint"""
        with self.assertRaisesRegex(
            NotNullViolation,
            'null value in column "res_partner_id" of relation "res_partner_session_rel" violates not-null constraint'
        ):
            self.create_session('test', self.course.id, None, None, None)

    def test_04_instructor_in_attendee(self):
        """Case when session have instructor in attendees: Error python constraint"""
        with self.assertRaisesRegex(
            ValidationError,
            'Instructor can not be on attendee field'
        ):
            self.create_session('test', self.course.id, self.partner_1.id, self.partner_1.id, 2)

    def test_05_attendees_greater_number_seat(self):
        """Case when session have more attendees than number seats: Error python constraint"""
        with self.assertRaisesRegex(
            ValidationError,
            'he test session can NOT have more attendees'
        ):
            self.create_session('test', self.course.id, self.partner_1.id, self.partner_1.id, 0)
