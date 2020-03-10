# File containing validators for forms - data validation is a part of security so we must use our own data validators

from . import db  # Import database for use in validation

from . import sanitise  # Some data may have to be sanitised if validating with database

from wtforms import ValidationError  # Raise wtforms ValidationError whenever data is invalid

from collections.abc import Iterable  # Used to check if data is Iterable for various validators
from string import ascii_letters, digits  # Used to check if data has alphabetic and/or numeric characters
import re


class NotInTableColumn(object):
    def __init__(self, table, column_name, message=None):
        self.table = str(table)
        self.column_name = str(column_name)
        if message:
            self.message = message
        else:
            self.message = u'Field is invalid'

    def __call__(self, form, field):
        if field.data:
            raw_sql = 'SELECT * FROM ' + self.table + ' WHERE ' + self.column_name + '="{}"'.format(sanitise.all(field.data))
            existing_user = db.session.execute(raw_sql).first()
            if existing_user:
                raise ValidationError(self.message)


class Required(object):
    def __init__(self, message=None):
        if message:
            self.message = message
        else:
            self.message = u'Field is required'

    def __call__(self, form, field):
        if not field.data:
            raise ValidationError(self.message)


class EqualTo(object):
    def __init__(self, field_name, message=None):
        self.field_name = field_name
        if message:
            self.message = message
        else:
            self.message = u'Field must be the same as {}'.format(self.field_name)

    def __call__(self, form, field):
        if form[self.field_name].data != field.data:
            raise ValidationError(self.message)


class DifferentFrom(object):
    def __init__(self, field_name, message=None):
        self.field_name = field_name
        if message:
            self.message = message
        else:
            self.message = u'Field must not be the same as {}'.format(self.field_name)

    def __call__(self, form, field):
        if form[self.field_name].data == field.data:
            raise ValidationError(self.message)


class Length(object):
    def __init__(self, min_length=None, max_length=None, message=None):
        if not min_length and not max_length:
            raise ValueError('Length validator does not have a minimum or maximum length to validate against')
        self.min = min_length
        self.max = max_length
        if message:
            self.message = message
        else:
            if self.min and self.max:
                self.message = u'Field must contain at least {} but no more than {} characters'.format(self.min, self.max)
            elif self.min:
                self.message = u'Field must contain at least {} characters'.format(self.min)
            elif self.max:
                self.message = u'Field must contain no more than {} characters'.format(self.max)

    def __call__(self, form, field):
        data_length = 0  # Handle no data input (data length default to 0)
        if field.data:
            data_length = len(field.data)
        if (self.min and data_length < self.min) or (self.max and data_length > self.max):
            raise ValidationError(self.message)


class AlphaNumeric(object):
    def __init__(self, message=None):
        if message:
            self.message = message
        else:
            self.message = u'Field must contain both letters and numbers'

    def __call__(self, form, field):
        alphabetic = False
        numeric = False
        for letter in ascii_letters:
            if letter in field.data:
                alphabetic = True
                break
        for digit in digits:
            if digit in field.data:
                numeric = True
                break
        if not alphabetic or not numeric:
            raise ValidationError(self.message)


class NotContainAny(object):
    def __init__(self, check, message=None):
        if not isinstance(check, Iterable):
            raise TypeError('NotContainAny validator requires validation data to be Iterable')
        self.check = check
        if message:
            self.message = message
        else:
            self.message = u'Field must not contain any of the following terms: {}'.format(self.check)

    def __call__(self, form, field):
        for i in self.check:
            if str(i) in str(field.data):
                raise ValidationError(self.message)


class MustContain(object):
    def __init__(self, check, message=None):
        if not isinstance(check, Iterable):
            raise TypeError('MustContain validator requires validation data to be Iterable')
        self.check = check
        if message:
            self.message = message
        else:
            self.message = u'Field must contain the following terms: {}'.format(self.check)

    def __call__(self, form, field):
        for i in self.check:
            if str(i) not in str(field.data):
                raise ValidationError(self.message)


class MustContainRegex(object):
    def __init__(self, message=None):
        if message:
            self.message = message
        else:
            self.message = u'Invalid Email Address'.format()

    def __call__(self, form, field):
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if not re.search(regex, field.data):
            raise ValidationError(self.message)




