# test_ammedge.py
"""
Tests for AmmEdge module.
"""

import unittest
from ammedge import AmmEdge

class TestAmmEdge(unittest.TestCase):
    """Test cases for AmmEdge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AmmEdge()
        self.assertIsInstance(instance, AmmEdge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AmmEdge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
