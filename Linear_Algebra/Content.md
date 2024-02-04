# Linear Algebra 
Linear algebra is the branch of linear equations mathematics that uses vector space and matrices.

The two primary mathematical entities that are of interest in linear algebra are the vector and the matrix. They are examples of a more general entity known as a tensor. Tensors possess an order (or rank), which determines the number of dimensions in a matrix required to represent it.

- vectors: A set of numerical elements of a particular size and one-dimensional.
- Matrix: A set of vectors that form a rectangular structure with rows and columns.
- Tensors: Tensors are a matrix of numbers or functions that transmute with certain rules when the coordinates change. Usually the work with tensors is more advanced and requires more Machine Learning and model oriented libraries like TensorFlow or PyTorch.

#### Vectors
Since scalars exist to represent values, why are vectors necessary? One of the main use cases for vectors is to represent physical quantities that have both a magnitude and a direction. Scalars are only capable of representing magnitudes.

For example, scalars and vectors encode the difference between the speed of a car and its velocity. The velocity contains not only its speed, but also its direction of travel.

In Machine Learning, vectors often represent feature vectors, with their individual components specifying how important a particular feature is. Such features might include the relative importance of words in a text document, the intensity of a set of pixels in a two-dimensional image, or historical price values for a representative sample of financial instruments.

##### Scalar Operations

Scalar operations involve a vector and a number.

##### Vector multiplication

There are two types of vector multiplication: dot product and Hadamard product.

- The dot product of two vectors is a scalar. The dot product of vectors and matrices (matrix multiplication) is one of the most important operations in deep learning.
- The Hadamard product is a multiplication by elements and generates a vector.

##### Matrices

A matrix is a rectangular grid of numbers or terms (like an Excel spreadsheet) with special rules for addition, subtraction, and multiplication.

Matrix dimensions: We describe the dimensions of a matrix in terms of rows by columns.

Scalar matrix operations: work the same way as with vectors. You simply apply the scalar to each element of the matrix - add, subtract, divide, multiply, etc.

Operations with matrix elements: To add, subtract or divide two matrices they must have the same dimensions (same number of rows and columns). We combine the corresponding values in an elementary way to produce a new matrix.

Matrix multiplication

There are two types of matrix multiplication: dot product and Hadamard product.

The dot product of two matrices is a matrix with the number of rows of the first matrix and the number of columns of the second matrix. There must be equality between the number of columns of the first and the number of rows of the second. That is, if matrix A has dimensions of 5 rows and 3 columns and matrix B has dimensions of 3 rows and 2 columns, the resulting matrix after multiplying them will have dimensions of 5x2 (and they can be multiplied because the first one has 3 columns and the second one has 3 rows).

In the dot product of matrices, the element cij of the product matrix is obtained by multiplying each element of row i of matrix A by each element of column j of matrix B and adding them together.

The Hadamard product of matrices is an elementary operation. Positionally corresponding values are multiplied to produce a new matrix.

Matrix transpose 

It provides a way to "rotate" one of the matrices so that the operation meets the multiplication requirements and can continue. There are two steps to transpose a matrix:

Rotate the matrix 90° to the right 2.
Reverse the order of the elements in each row (e.g., abc becomes cba)

#### Applications of linear algebra
Linear algebra has a direct impact on all processes involving data processing:
- The data in a dataset is vectorized. Rows are inserted into a model one at a time for easier and more authentic calculations.
- All images have a tabular (matrix) structure. Image editing techniques, such as cropping and scaling, use algebraic operations.
- Regularization is a method that minimizes the size of coefficients while inserting them into the data.
- Deep learning works with vectors, matrices and even tensors, as it requires aggregated and multiplied linear data structures.
- The 'One hot encoding' method encodes categories to facilitate algebra operations.
- In linear regression, linear algebra is used to describe the relationship between variables.
- When we find irrelevant data, we usually eliminate redundant columns, so PCA works with matrix factorization.
- With the help of linear algebra, recommender systems can have more refined data.