# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 15:43:55 2022

@author: georg
"""

import unittest
import miniMain

class TestminiMain(unittest.Testcase):
    
    def setUp(self):
        self.nombre_producto1 = miniMain('pollo')
        self.cantidad_producto1 = miniMain(90)
    
    def tearDown(self): 
        pass
    
    def test_agregarInventario(self):
        print('test_agregarInventario')
        self.assertEqual(self.ombre_producto1.agregarInventario,'pollo')
        self.assertEqual(self.cantidad_producto1.agregarInventario, 90)
        
if __name__=="__main__":
    unittest.main()
    
        
