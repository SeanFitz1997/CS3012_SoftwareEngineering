import unittest
import LCA

class test_LCA(unittest.TestCase):

    def test_findLCA(self):
        #Test 1: test all values equal None
        self.assertEqual(LCA.findLCA(None, None, None), None)

        #Test 2: test when both node are root
        root = LCA.Node(1)
        self.assertEqual(LCA.findLCA(root, 1, 1), 1)

        #Test 3: test when a value is not in tree
        self.assertEqual(LCA.findLCA(root, 50, 51), None)

        #Test 4: LCA 4-5
        root.children.append(LCA.Node(2)) 
        root.children.append(LCA.Node(3))
        root.children[0].children.append(LCA.Node(4))
        root.children[0].children.append(LCA.Node(5))
        root.children[1].children.append(LCA.Node(6))
        root.children[1].children.append(LCA.Node(7))  
    
        self.assertEqual(LCA.findLCA(root, 4, 5), 2)

        #Test 5: LCA 4-6
        self.assertEqual(LCA.findLCA(root, 4, 6), 1)

        #Test 6: LCA 3-4
        self.assertEqual(LCA.findLCA(root, 3, 4), 1)

        #Test 7: LCA 2-4
        self.assertEqual(LCA.findLCA(root, 2, 4), 2)

        #Test 8: nodes at different heights
        self.assertAlmostEqual(LCA.findLCA(root, 2, 6), 1)

    def test_findLCA_v2(self):
        root = LCA.Node(1)
        root.children.append(LCA.Node(2))
        root.children.append(LCA.Node(5))
        root.children.append(LCA.Node(3))
        root.children[0].children.append(LCA.Node(4))
        root.children[2].children.append(LCA.Node(5))
        root.children[2].children.append(LCA.Node(6))
        root.children[2].children.append(LCA.Node(7))

        #Test 1: LCA 2-3
        self.assertEqual(LCA.findLCA(root, 2, 3), 1)

        #Test 2: LCA 4-5
        self.assertEqual(LCA.findLCA(root, 4, 5), 1)

        #Test 3: LCA 5-6
        self.assertEqual(LCA.findLCA(root, 5, 6), 3)

        #Test 4: LCA 1-7
        self.assertEqual(LCA.findLCA(root, 1, 7), 1)

        #New Graph
        root = LCA.Node('G')
        root.children.append(LCA.Node('D'))
        root.children.append(LCA.Node('F'))
        root.children[0].children.append(LCA.Node('C'))
        root.children[0].children[0].children.append(LCA.Node('B'))
        root.children[0].children[0].children[0].children.append(LCA.Node('A'))
        root.children[1].children.append(LCA.Node('F'))
        root.children[1].children[0].children.append(LCA.Node('E'))
        root.children[1].children[0].children[0].children.append(LCA.Node('B'))

        #Test 5: LCA G-G
        self.assertEqual(LCA.findLCA(root, 'G', 'G'), 'G')

        #Test 6: LCA G-C
        self.assertEqual(LCA.findLCA(root, 'G', 'C'), 'G')

        #Test 7: LCA G-C
        self.assertEqual(LCA.findLCA(root, 'C', 'E'), 'G')

        #Test 8: LCA G-C
        self.assertEqual(LCA.findLCA(root, 'A', 'B'), 'B')

    def test_pathTo(self):
        #Test 1: test all values equal None
        self.assertEqual(LCA.pathTo(None, None, None), False)

        #Test 2: test path to root
        root = LCA.Node(1)
        self.assertEqual(LCA.pathTo(root, [], 1), True)

        #Test 3: test for key not in tree
        self.assertEqual(LCA.pathTo(root, [], 50), False)

        #Test 4: path to 4
        root.children.append(LCA.Node(2)) 
        root.children.append(LCA.Node(3))
        root.children[0].children.append(LCA.Node(4))
        root.children[0].children.append(LCA.Node(5))
        root.children[1].children.append(LCA.Node(6))
        root.children[1].children.append(LCA.Node(7))
        self.assertEqual(LCA.pathTo(root, [], 4), True)

        #Test 5: path to 6
        self.assertEqual(LCA.pathTo(root, [], 6), True)
        
        #Test 6: path to 3
        self.assertEqual(LCA.pathTo(root, [], 3), True)

        #Test 7: path to 2
        self.assertEqual(LCA.pathTo(root, [], 2), True)

    def test_pathsTo(self):
        #Test 1: test all values equal None
        self.assertEqual(LCA.findPathsTo(None, None), [])

        #Test 2: test path to root
        root = LCA.Node(1)
        self.assertEqual(LCA.findPathsTo(root, 1), [[1]])

        #Test 3: test for key not in tree
        self.assertEqual(LCA.findPathsTo(root, 50), [])

        #Test 4: paths to 4
        root.children.append(LCA.Node(2))
        root.children.append(LCA.Node(5))
        root.children.append(LCA.Node(3))
        root.children[0].children.append(LCA.Node(4))
        root.children[2].children.append(LCA.Node(5))
        root.children[2].children.append(LCA.Node(6))
        root.children[2].children.append(LCA.Node(7))
        self.assertEqual(LCA.findPathsTo(root, 4), [[1,2,4]])

        #Test 5: path to 6
        self.assertEqual(LCA.findPathsTo(root, 6), [[1,3,6]])
        
        #Test 6: path to 5
        self.assertEqual(LCA.findPathsTo(root, 5), [[1,5],[1,3,5]])

if(__name__ == '__main__'):
    unittest.main()