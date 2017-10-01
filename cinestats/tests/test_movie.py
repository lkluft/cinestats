"""Test the cinestats.movie module.
"""
import cinestats


class TestMovie:
    def test_init(self):
        """Test basic initialisation of a Movie object."""
        m = cinestats.Movie(title='Foo', date='2017-10-01')

        assert m.title == 'Foo'
        assert m.date == '2017-10-01'
