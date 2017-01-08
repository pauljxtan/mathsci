"""
Provides generic datatypes.
"""

# TODO: Add missing/incomplete docstrings

ERR_INPUT_NOT_LIST_TUPLE = "Input data is not list or tuple"
ERR_INPUT_BAD_DIMS = "Input data has incompatible dimensions"
ERR_KEY_NOT_INT_LIST_TUPLE = "Key is not int, list or tuple"
ERR_KEY_OUT_OF_BOUNDS = "Key is out of bounds"
ERR_OP_BAD_DIMS = "Operand has incompatible dimensions for element-wise operation"
ERR_OP_NOT_VEC = "Operand is not Vector"
ERR_OP_NOT_MAT = "Operand is not Matrix"
ERR_INPUT_INVALID = "Input data is invalid"

import souffle.math.linalg

class Vector(object):
    """
    The generic vector class.
    """
    def __init__(self, data=None):
        """
        @type  data: iterable
        @param data: the data to load into the Vector
        """
        self.data = []
        if data == None:
            return
        try:
            self.data = [elem for elem in data]
            self.n_elems = len(self.data)
        except:
            raise ValueError(ERR_INPUT_INVALID)

    #### Representations

    def __str__(self):
        """
        Returns the string representation of the Vector.

        @rtype: string
        @return: the string representation of the Vector
        """
        return "[{}]".format(" ".join([str(elem) for elem in self.data]))

    #### Container methods

    def __getitem__(self, key=None):
        """
        Returns the element(s) specified by the index/indices in key. Supports
        backwards indexing. If key is None, returns the entire Vector.

        @type  k: integer, list or tuple
        @param k: the index/indices of the element(s) to access

        @return: the element(s) specified by the given index/indices
        """
        if isinstance(key, int):
            if key >= 0:
                    return self.data[key]
            # Negative index: count from end of vector
            return self.data[self.n_elems + key]
                
        if isinstance(key, list) or isinstance(key, tuple):
            result = []
            for k in key:
                if k >= 0:
                    result.append(self.data[k])
                else:
                    # Negative index: count from end of vector
                    result.append(self.data[self.n_elems + k])
            return result
        else:
            raise ValueError(ERR_KEY_NOT_INT_LIST_TUPLE)

    #### Unary operators

    def __pos__(self):
        """
        Implements behaviour for unary positive.

        @rtype: Vector
        @return: the Vector with all elements positive
        """
        return Vector([+elem for elem in self.data])

    def __neg__(self):
        """
        Implements behaviour for unary negation.

        @rtype: Vector
        @return: the Vector with all elements negated
        """
        return Vector([-elem for elem in self.data])

    def __abs__(self):
        """
        Implements behaviour for absolute value (NOT modulus; use dot()).

        @rtype: Vector
        @return: the Vector containing the absolute value of all elements
        """
        return Vector([abs(elem) for elem in self.data])

    #### Comparisons

    def __eq__(self, other):
        """
        Compares two Vectors by element to determine equality.

        @type  other: Vector
        @param other: the Vector to compare

        @rtype: boolean
        @return: whether the Vectors are equal
        """
        if not isinstance(other, Vector):
            raise ValueError(ERR_OP_NOT_VEC)
        if self.n_elems != other.n_elems:
            raise ValueError(ERR_OP_BAD_DIMS)

        for i in range(self.n_elems):
            if self[i] != other[i]:
                return False
        return True

    def __lt__(self, other):
        """
        Returns a boolean Vector containing the results of element-wise
        less-than comparisons.

        @type  other: Vector
        @param other: the Vector to compare

        @rtype: Vector of booleans
        @return: the comparison result for each element
        """
        if not isinstance(other, Vector):
            raise ValueError(ERR_OP_NOT_VEC)
        if self.n_elems != other.n_elems:
            raise ValueError(ERR_OP_BAD_DIMS)

        return Vector([self[i] < other[i] for i in range(self.n_elems)])

    def __gt__(self, other):
        """
        Returns a boolean Vector containing the results of element-wise
        greater-than comparisons.

        @type  other: Vector
        @param other: the Vector to compare

        @rtype: Vector of booleans
        @return: the comparison result for each element
        """
        if not isinstance(other, Vector):
            raise ValueError(ERR_OP_NOT_VEC)
        if self.n_elems != other.n_elems:
            raise ValueError(ERR_OP_BAD_DIMS)

        return Vector([self[i] > other[i] for i in range(self.n_elems)])

    def __le__(self, other):
        """
        Returns a boolean Vector containing the results of element-wise
        less-than-or-equal comparisons.

        @type  other: Vector
        @param other: the Vector to compare

        @rtype: Vector of booleans
        @return: the comparison result for each element
        """
        if not isinstance(other, Vector):
            raise ValueError(ERR_OP_NOT_VEC)
        if self.n_elems != other.n_elems:
            raise ValueError(ERR_OP_BAD_DIMS)

        return Vector([self[i] <= other[i] for i in range(self.n_elems)])

    def __ge__(self, other):
        """
        Returns a boolean Vector containing the results of element-wise
        greater-than-or-equal comparisons.

        @type  other: Vector
        @param other: the Vector to compare

        @rtype: Vector of booleans
        @return: the comparison result for each element
        """
        if not isinstance(other, Vector):
            raise ValueError(ERR_OP_NOT_VEC)
        if self.n_elems != other.n_elems:
            raise ValueError(ERR_OP_BAD_DIMS)

        return Vector([self[i] >= other[i] for i in range(self.n_elems)])

    #### Element-wise arithmetic

    def __add__(self, other):
        """
        Perform element-wise addition of one Vector by another.

        @type  other: Vector
        @param other: the Vector to add

        @rtype: Vector
        @return: the element-wise sum of the operands
        """
        if not isinstance(other, Vector):
            raise ValueError(ERR_OP_NOT_VEC)
        if not (self.n_elems == other.n_elems):
            raise ValueError(ERR_OP_BAD_DIMS)
        
        return Vector([self[i] + other[i] for i in range(self.n_elems)])

    def __sub__(self, other):
        """
        Perform element-wise subtraction of one Vector by another.

        @type  other: Vector
        @param other: the Vector to subtract

        @rtype: Vector
        @return: the element-wise difference of the operands
        """
        if not isinstance(other, Vector):
            raise ValueError(ERR_OP_NOT_VEC)
        if not (self.n_elems == other.n_elems):
            raise ValueError(ERR_OP_BAD_DIMS)
        
        return Vector([self[i] - other[i] for i in range(self.n_elems)])

    def __mul__(self, other):
        """
        Perform element-wise multiplication of one Vector by another.

        @type  other: Vector
        @param other: the Vector to multiply

        @rtype: Vector
        @return: the element-wise product of the operands
        """
        if not isinstance(other, Vector):
            raise ValueError(ERR_OP_NOT_VEC)
        if not (self.n_elems == other.n_elems):
            raise ValueError(ERR_OP_BAD_DIMS)
                             
        return Vector([self[i] * other[i] for i in range(self.n_elems)])

    def __div__(self, other):
        """
        Perform element-wise division of one Vector by another.

        @type  other: Vector
        @param other: the Vector to divide

        @rtype: Vector
        @return: the element-wise quotient of the operands
        """
        if not isinstance(other, Vector):
            raise ValueError(ERR_OP_NOT_VEC)
        if not (self.n_elems == other.n_elems):
            raise ValueError(ERR_OP_BAD_DIMS)
                             
        return Vector([self[i] / other[i] for i in range(self.n_elems)])

    #### Type conversion

    def get_typecasted(self, ttype):
        """
        Returns a new Vector with each value casted to the input type.

        @type  ttype: type
        @param ttype: the type to which all elements should be casted
        """
        return Vector(map(ttype, self.data))

    #### Scalar arithmetic

    def add_scalar(self, value):
        """
        Returns a new Vector with the input value added to every element.

        @type  value: number
        @param value: the value to be added to each element

        @rtype: Vector
        @return: the resulting Vector
        """
        return Vector([elem + value for elem in self.data])
    
    def sub_scalar(self, value):
        """
        Returns a new Vector with the input value subtracted from every element.

        @type  value: number
        @param value: the value to be subtracted from each element

        @rtype: Vector
        @return: the resulting Vector
        """
        return Vector([elem - value for elem in self.data])
    
    def mul_scalar(self, value):
        """
        Returns a new Vector with every element multiplied by the input value.

        @type  value: number
        @param value: the value to multiply each element

        @rtype: Vector
        @return: the resulting Vector
        """
        return Vector([elem * value for elem in self.data])
    
    def div_scalar(self, value):
        """
        Returns a new Vector with every element divided by the input value.

        @type  value: number
        @param value: the value to divide each element

        @rtype: Vector
        @return: the resulting Vector
        """
        return Vector([elem / value for elem in self.data])
    
    #### Vector operations

    def dot_product(self, other):
        """
        Returns the dot product.

        @type  other: Vector
        @param other: the Vector with which to compute the dot product

        @rtype: Vector
        @return: the dot product of the operands
        """
        if not isinstance(other, Vector):
            raise ValueError(ERR_OP_NOT_VEC)
        if not (self.n_elems == other.n_elems):
            raise ValueError(ERR_OP_BAD_DIMS)

        return souffle.math.linalg.dot_product(self.data, other.data)

    #### Adding/removing elements

    def append(self, value):
        """
        Adds the input value to the end of the Vector.

        @type  value: number
        @param value: the value to append to the Vector
        """
        self.data.append(value)
        self.n_elems = len(self.data)

    def prepend(self, value):
        """
        Adds the input value to the beginning of the Vector.

        @type  value: number
        @param value: the value to prepend to the Vector
        """
        self.data.insert(0, value)
        self.n_elems = len(self.data)

    def insert(self, idx, value):
        """
        Inserts the input value at the given index.

        @type    idx: integer
        @param   idx: the index at which to insert the value
        @type  value: number
        @param value: the value to insert
        """
        self.data.insert(idx, value)
        self.n_elems = len(self.data)

    def remove(self, idx):
        """
        Removes the element at the given index.

        @type    idx: integer
        @param   idx: the index of the element to be removed
        """
        del self.data[idx]
        self.n_elems = len(self.data)

    def get_slice(self, idx_start, idx_end):
        """
        Returns the slice specified by the given start and end indices.

        @type  idx_start: integer
        @param idx_start: the start index of the slice

        @type  idx_end: integer
        @param idx_end: the end index of the slice
        """ 
        return self.data[idx_start : idx_end]

class Matrix(object):
    """
    The generic matrix class.
    """
    def __init__(self, data=None):
        """
        @type  data: a 2-dimensional combination of lists and/or tuples
        @param data: the data to load into the Matrix
        """
        self.data = []
        if data == None:
            return
        try:
            self.data = [[elem in row for elem in row] for row in data]
            self.n_rows = len(data)
            self.n_cols = len(data[0])
        except:
            raise ValueError(ERR_INPUT_INVALID)
        row_lens = [len(row) for row in self.data]
        if row_lens[1:] != row_lens[:-1]:
            raise ValueError("Row lengths are not all equal")
   
    #### Representations

    def __str__(self):
        """
        Returns the string representation of the Matrix.
        """
        output = "["
        for i in range(self.n_rows):
            if i != 0:
                output += " "
            output += "[{}]".format(" ".join([str(elem) for elem in self.data]))
            if i != self.n_rows - 1:
                output += "\n"
        output += "]"
        return output

    #### Container methods

    # TODO    
    def __getitem__(self):
        return

    #### Unary operators

    def __pos__(self):
        """
        Implements behaviour for unary positive.
        """
        return Matrix([[+elem for elem in row] for row in self.data])

    def __neg__(self):
        """
        Implements behaviour for unary negation.
        """
        return Matrix([[-elem for elem in row] for row in self.data])

    def __abs__(self):
        """
        Implements behaviour for absolute value (NOT modulus; use dot()).
        """
        return Matrix([[abs(elem) for elem in row] for row in self.data])
    
    #### Comparisons

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError(ERR_OP_NOT_MAT)
        if self.n_rows != other.n_rows and self.n_cols != other.n_cols:
            raise ValueError(ERR_OP_BAD_DIMS)

        for i in range(self.n_rows):
            for j in range(self.n_cols):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True

    #### Element-wise arithmetic

    # TODO: continue refactoring here

    def __add__(self, other):
        """
        Perform element-wise addition of one Matrix by another.
        """
        if not isinstance(other, Matrix):
            raise ValueError(ERR_OP_NOT_MAT)
        if not (self.n_rows == other.n_rows and self.n_cols == other.n_cols):
            raise ValueError(ERR_OP_BAD_DIMS)

        result = [[0.0 for i in range(self.n_rows)]
                  for j in range(self.n_cols)]

        for i in range(self.n_rows):
            for j in range(self.n_cols):
                result[i][j] = self.data[i][j] + other.data[i][j]

        # TODO: use __getitem__() after implemented, e.g. self[i, j] (?)
        return Matrix([[self.data[i][j] + other.data[i][j]
                        for i in self.n_rows] for j in self.n_cols])

    def __sub__(self, other):
        """
        Perform element-wise subtraction of one Matrix by another.
        """
        if not isinstance(other, Matrix):
            raise ValueError(ERR_OP_NOT_MAT)
        if not (self.n_rows == other.n_rows and self.n_cols == other.n_cols):
            raise ValueError(ERR_OP_BAD_DIMS)

        # TODO: use __getitem__() after implemented, e.g. self[i, j] (?)
        return Matrix([[self.data[i][j] - other.data[i][j]
                        for i in self.n_rows] for j in self.n_cols])

    def __mul__(self, other):
        """
        Perform element-wise multiplication of one Matrix by another.
        """
        if not isinstance(other, Matrix):
            raise ValueError(ERR_OP_NOT_MAT)
        if not (self.n_rows == other.n_rows and self.n_cols == other.n_cols):
            raise ValueError(ERR_OP_BAD_DIMS)

        # TODO: use __getitem__() after implemented, e.g. self[i, j] (?)
        return Matrix([[self.data[i][j] * other.data[i][j]
                        for i in self.n_rows] for j in self.n_cols])

    def __div__(self, other):
        """
        Perform element-wise division of one Matrix by another.
        """
        if not isinstance(other, Matrix):
            raise ValueError(ERR_OP_NOT_MAT)
        if not (self.n_rows == other.n_rows and self.n_cols == other.n_cols):
            raise ValueError(ERR_OP_BAD_DIMS)

        # TODO: use __getitem__() after implemented, e.g. self[i, j] (?)
        return Matrix([[self.data[i][j] / other.data[i][j]
                        for i in self.n_rows] for j in self.n_cols])

    #### Type conversion

    def get_typecasted(self, ttype):
        return Matrix([map(ttype, row) for row in self.data])

    #### Matrix operations

    def mul_matrix(self, other):
        """
        Performs matrix multiplication.
        """
        if not isinstance(other, Matrix):
            raise ValueError(ERR_OP_NOT_MAT)

        result = [[0.0 for i in range(self.n_rows)]
                  for j in range(other.n_cols)]

        for i in range(self.n_rows):
            for j in range(other.n_cols):
                result[i][j] = (souffle.math.linalg.dot_product
                                (self.data[i], zip(*other.data)[j]))

        return Matrix(result)

    # TODO
    def inverse(self):
        return

    ### Accessing elements
    
    def get_row(self, row_idx):
        return self.data[row_idx]

    def get_col(self, col_idx):
        col = []
        for row in range(self.n_rows):
            col.append(self.data[row][col_idx])
        return col

    #### Adding/removing elements
    
    def append_row(self, row):
        """
        Adds the input row to the bottom of the Matrix.
        """
        if len(row) != self.n_cols and self.n_rows != 0:
            raise ValueError(ERR_INPUT_BAD_DIMS)
        
        self.data.append(row)
        self.n_rows = len(self.data)

    def append_col(self, col):
        """
        Add the input column to the right of the Matrix.
        """
        if len(col) != self.n_rows and self.n_cols != 0:
            raise ValueError(ERR_INPUT_BAD_DIMS)

        for i in range(self.n_rows):
            self.data[i].append(col[i])
        self.n_cols = len(self.data[0])

    def remove_row(self, row_idx):
        del self.data[row_idx]
        self.n_rows -= 1

    def remove_col(self, col_idx):
        for row in range(self.n_rows):
            del self.data[row][col_idx]
        self.n_cols -= 1