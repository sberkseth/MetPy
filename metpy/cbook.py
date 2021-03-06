'''Collection of generally useful utility code from the cookbook'''
import os
import os.path
from matplotlib.cbook import iterable, is_string_like, Bunch


def get_test_data(fname, as_file_obj=True):
    # Look for an environment variable to point to the test data. If not, try looking at
    # the appropriate path relative to this file.
    data_dir = os.environ.get('TEST_DATA_DIR',
                              os.path.join(os.path.dirname(__file__), '..', 'testdata'))

    # Assemble the path
    path = os.path.join(data_dir, fname)

    # If we want a file object, open it, trying to guess whether this should be binary mode
    # or not
    if as_file_obj:
        mode = 'r'
        if os.path.splitext(path)[-1].lower() not in ('.csv', '.txt'):
            mode += 'b'

        return open(path, mode)

    return path

__all__ = ['Bunch', 'get_test_data', 'is_string_like', 'iterable']
