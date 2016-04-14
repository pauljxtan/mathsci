"""
Provides generic datatypes.
"""

ERR_INPUT_NOT_LIST_TUPLE = "Input data is not list or tuple"
ERR_INPUT_BAD_DIMS = "Input data has incompatible dimensions"
ERR_KEY_NOT_INT_LIST_TUPLE = "Key is not int, list or tuple"
ERR_OP_BAD_DIMS = "Operand has incompatible dimensions for element-wise operation"
ERR_OP_NOT_VEC = "Operand is not Vector"
ERR_OP_NOT_MAT = "Operand is not Matrix"

import mathsci.math.linalg

class Vector(object):
    """
    The generic vector class.
    """
    def __init__(self, data=None):
        """
        @type  data: list or tuple
        @param data: the data to load into the Vector
        """
        if data == None:
            self.data = []
        else:
            if not (isinstance(data, list) or isinstance(data, tuple)):
                raise ValueError(ERR_INPUT_NOT_LIST_TUPLE)
            self.data = data
        self.n_elems = len(self.data)

    #### Representations

    def __str__(self):
        """
        Returns the string representation of the Vector.

        @rtype: string
        @return: the string representation of the Vector
        """
        data_str = map(str, self.data)
        output = "["
        output += " ".join([elem for elem in data_str])
        output += "]" 

        return output

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
                result = self.data[key]
            else:
                result = self.data[self.n_elems + key]
                
        elif isinstance(key, list) or isinstance(key, tuple):
            result = []
            for k in key:
                if k >= 0:
                    result.append(self.data[k])
                else:
                    result.append(self.data[self.n_elems + k])
        else:
            raise ValueError(ERR_KEY_NOT_INT_LIST_TUPLE)

        return result

    #### Unary operators

    def __pos__(self):
        """
        Implements behaviour for unary positive.

        @rtype: Vector
        @return: the Vector with all elements positive
        """
        result = []
        for i in range(self.n_elems):
            result.append(+self.data[i])

        return Vector(result)

    def __neg__(self):
        """
        Implements behaviour for unary negation.

        @rtype: Vector
        @return: the Vector with all elements negated
        """
        result = []
        for i in range(self.n_elems):
            result.append(-self.data[i])

        return Vector(result)

    def __abs__(self):
        """
        Implements behaviour for absolute value (NOT modulus; use dot()).

        @rtype: Vector
        @return: the Vector containing the absolute value of all elements
        """
        result = []
        for i in range(self.n_elems):
            result.append(abs(self.data[i]))

        return Vector(result)

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
            if self.data[i] != other.data[i]:
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

        result = []
        for i in range(self.n_elems):
            result.append(self.data[i] < other.data[i])

        return Vector(result)

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

        result = []
        for i in range(self.n_elems):
            result.append(self.data[i] > other.data[i])

        return Vector(result)

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

        result = []
        for i in range(self.n_elems):
            result.append(self.data[i] <= other.data[i])

        return Vector(result)

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

        result = []
        for i in range(self.n_elems):
            result.append(self.data[i] >= other.data[i])

        return Vector(result)

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

        result = []
        for i in range(self.n_elems):
            result.append(self.data[i] + other.data[i])
        
        return Vector(result)

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
        
        result = []
        for i in range(self.n_elems):
            result.append(self.data[i] - other.data[i])
        
        return Vector(result)

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
                             
        result = []
        for i in range(self.n_elems):
            result.append(self.data[i] * other.data[i])

        return Vector(result)

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
                             
        result = []
        for i in range(self.n_elems):
            result.append(self.data[i] / other.data[i])

        return Vector(result)

    #### Type conversion

    def set_type(self, ttype):
        """
        Sets the type for all elements.

        @type  ttype: type
        @param ttype: the type to which all elements should be converted
        """
        self.data = map(ttype, self.data)

    #### Scalar arithmetic

    def add_scalar(self, value):
        """
        Returns a new Vector with the input value added to every element.

        @type  value: number
        @param value: the value to be added to each element

        @rtype: Vector
        @return: the resulting Vector
        """
        result = self.data[:]
        for i, v in enumerate(result):
            result[i] += value

        return Vector(result)
    
    def sub_scalar(self, value):
        """
        Returns a new Vector with the input value subtracted from every element.

        @type  value: number
        @param value: the value to be subtracted from each element

        @rtype: Vector
        @return: the resulting Vector
        """
        result = self.data[:]
        for i, v in enumerate(result):
            result[i] -= value

        return Vector(result)
    
    def mul_scalar(self, value):
        """
        Returns a new Vector with every element multiplied by the input value.

        @type  value: number
        @param value: the value to multiply each element

        @rtype: Vector
        @return: the resulting Vector
        """
        result = self.data[:]
        for i, v in enumerate(result):
            result[i] *= value

        return Vector(result)
    
    def div_scalar(self, value):
        """
        Returns a new Vector with every element divided by the input value.

        @type  value: number
        @param value: the value to divide each element

        @rtype: Vector
        @return: the resulting Vector
        """
        result = self.data[:]
        for i, v in enumerate(result):
            result[i] /= value

        return Vector(result)
    
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

        return mathsci.math.linalg.dot_product(self.data, other.data)

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
        if data == None:
            self.data = []
        else:
            if not (isinstance(data, list) or isinstance(data, tuple)):
                raise ValueError(ERR_INPUT_NOT_LIST_TUPLE)
            self.data = data
        # TODO: raise error if not all rows have same length
        self.n_rows = len(data)
        self.n_cols = len(data[0])
   
    #### Representations

    def __str__(self):
        """
        Returns the string representation of the Matrix.
        """
        output = "["
        for i in range(self.n_rows):
            row_str = map(str, self.data[i])
            if i != 0:
                output += " "
            output += "["
            output += " ".join([elem for elem in row_str])
            output += "]"
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
        result = [[0.0 for i in range(self.n_rows)]
                  for j in range(self.n_cols)]
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                result[i][j] = +self.data[i][j]

        return result

    def __neg__(self):
        """
        Implements behaviour for unary negation.
        """
        result = [[0.0 for i in range(self.n_rows)]
                  for j in range(self.n_cols)]
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                result[i][j] = -self.data[i][j]

        return result

    def __abs__(self):
        """
        Implements behaviour for absolute value (NOT modulus; use dot()).
        """
        result = [[0.0 for i in range(self.n_rows)]
                  for j in range(self.n_cols)]
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                result[i][j] = abs(self.data[i][j])

        return result
    
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

        return Matrix(result)

    def __sub__(self, other):
        """
        Perform element-wise subtraction of one Matrix by another.
        """
        if not isinstance(other, Matrix):
            raise ValueError(ERR_OP_NOT_MAT)
        if not (self.n_rows == other.n_rows and self.n_cols == other.n_cols):
            raise ValueError(ERR_OP_BAD_DIMS)

        result = [[0.0 for i in range(self.n_rows)]
                  for j in range(self.n_cols)]

        for i in range(self.n_rows):
            for j in range(self.n_cols):
                result[i][j] = self.data[i][j] - other.data[i][j]
        return Matrix(result)        


    def __mul__(self, other):
        """
        Perform element-wise multiplication of one Matrix by another.
        """
        if not isinstance(other, Matrix):
            raise ValueError(ERR_OP_NOT_MAT)
        if not (self.n_rows == other.n_rows and self.n_cols == other.n_cols):
            raise ValueError(ERR_OP_BAD_DIMS)

        result = [[0.0 for i in range(self.n_rows)]
                  for j in range(self.n_cols)]

        for i in range(self.n_rows):
            for j in range(self.n_cols):
                result[i][j] = self.data[i][j] * other.data[i][j]

        return Matrix(result)

    def __div__(self, other):
        """
        Perform element-wise division of one Matrix by another.
        """
        if not isinstance(other, Matrix):
            raise ValueError(ERR_OP_NOT_MAT)
        if not (self.n_rows == other.n_rows and self.n_cols == other.n_cols):
            raise ValueError(ERR_OP_BAD_DIMS)

        result = [[0.0 for i in range(self.n_rows)]
                  for j in range(self.n_cols)]

        for i in range(self.n_rows):
            for j in range(self.n_cols):
                result[i][j] = float(self.data[i][j]) / other.data[i][j]

        return Matrix(result)

    #### Type conversion

    def set_type(self, ttype):
        for row in range(self.n_rows):
            self.data[row] = map(ttype, self.data[row])

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
                result[i][j] = (mathsci.math.linalg.dot_product
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