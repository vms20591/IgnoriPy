from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
import unittest
from ignoripy import GitIgnore, GitIgnoreError, format_error

class TestGitIgnore(unittest.TestCase):
  def setUp(self):
    self.endpoint = "https://gitignore.io/api"

  def test_get_with_single_valid_language(self):
    gitignore = GitIgnore(self.endpoint, "python")
    response = gitignore.get()

    self.assertNotIn("#!! ERROR", response)

  def test_get_with_single_invalid_language(self):
    gitignore = GitIgnore(self.endpoint, "pythons")

    with self.assertRaises(GitIgnoreError) as context_mgr:
      gitignore.get()

    self.assertEqual("`pythons` doesn't have a gitignore", context_mgr.exception.message)

  def test_get_with_multiple_valid_language(self):
    gitignore = GitIgnore(self.endpoint, "python,node,java")
    response = gitignore.get()

    self.assertNotIn("#!! ERROR", response)

  def test_get_with_multiple_invalid_language(self):
    gitignore = GitIgnore(self.endpoint, "java,pythons")

    with self.assertRaises(GitIgnoreError) as context_mgr:
      gitignore.get()

    self.assertEqual("`pythons` doesn't have a gitignore", context_mgr.exception.message)

  def test_get_with_invalid_endpoint(self):
    gitignore = GitIgnore(self.endpoint + "/apis", "pythons")

    with self.assertRaises(GitIgnoreError) as context_mgr:
      gitignore.get()

    self.assertEqual("Error occurred getting .gitignore", context_mgr.exception.message)

class Test_format_error(unittest.TestCase):
  def test_with_valid_error(self):
    message = format_error(GitIgnoreError("error"), "python")
    expected = "# Language: python\n# Error: error"

    self.assertEqual(message, expected)

  def test_with_int_error(self):
    message = format_error(10, "python")
    expected = "# Language: python\n# Error: 10"

    self.assertEqual(message, expected)

  def test_with_invalid_error(self):
    message = format_error(None, None)
    expected = "# Language: N/A\n# Error: N/A"

    self.assertEqual(message, expected)

  def test_with_string_error(self):
    message = format_error("error", "python")
    expected = "# Language: python\n# Error: error"

    self.assertEqual(message, expected)

  def test_with_empty_error(self):
    message = format_error(None, "python")
    expected = "# Language: python\n# Error: N/A"

    self.assertEqual(message, expected)

  def test_with_empty_language(self):
    message = format_error("error", "")
    expected = "# Language: N/A\n# Error: error"

    self.assertEqual(message, expected)

if __name__ == "__main__":
  unittest.main()