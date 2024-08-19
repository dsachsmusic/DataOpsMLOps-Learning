PyTorch and TensorFlow are primarily for deep learning, while Pandas is for data manipulation, and PySpark is for big data processing.

Graph Computation: PyTorch uses dynamic computation graphs, making it more flexible during development, while TensorFlow traditionally used static graphs, which are more efficient in production.

Computation graph  - A computational graph is a directed acyclic graph (DAG) where:
- Nodes represent operations (like addition, multiplication, matrix multiplication) or variables (like inputs, weights).
- Edges represent the flow of data (tensors) between these operations.

Automatic differentiation - Automatic differentiation (AutoDiff) is a technique used to compute the derivatives (gradients) of functions efficiently. It's particularly important in training neural networks, where we need to compute the gradient of the loss function with respect to model parameters.
- Forward Mode: In forward mode, derivatives are propagated from inputs to outputs in the same direction as the computational graph's evaluation (i.e., forward pass). 
- In reverse mode (also known as backpropagation in neural networks), derivatives are computed in the reverse direction (i.e., backward pass).
- Gradient Computation: In the context of neural networks, after the forward pass computes the loss, reverse mode automatic differentiation (backpropagation) is used to compute the gradients of the loss with respect to each parameter by applying the chain rule of calculus.

A gradient tells you how much a function's output will change if you slightly tweak each input variable.

vector, direction, magnitude
- A vector is like a journey:
-- Direction tells you where you're going.
-- Magnitude tells you how far or how fast you're going

Loss Function - in machine learning, you train a model to make predictions or decisions based on data. To know if your model is improving, you need a way to measure how close or far its predictions are from the actual outcomes. This is where the loss function comes in.
 
It seems to me that the use of the term/concept "DAG" in Airflow is different from its use in training neural networks.  
...while both concepts use the structure of a DAG, they apply it to very different domains: one in task management (Airflow) and the other in data processing and model training (neural networks). The commonality lies in the fact that both involve directed processes with no cycles, but their specific applications and purposes differ significantly.

Training a Model: Imagine you’re a hiker trying to reach the top of a hill (minimizing error). You use a map (computational graph) to plan your route, and each time you take a step, you get feedback (automatic differentiation) on whether you’re going in the right direction and how steep it is (gradient).

Adjusting the Path: With this information, you adjust your path to make sure you’re always heading uphill towards the top (reducing the error), and over time, you get closer and closer to the summit (the best model you can create).

Tensor is a multi-dimensional array of numbers. You can think of it as a generalization of scalars, vectors, and matrices to higher dimensions.

Scalar: A single number (0-dimensional tensor).
Vector: A one-dimensional array of numbers (1-dimensional tensor). 
Matrix: A two-dimensional array of numbers (2-dimensional tensor). 

In machine learning, especially in deep learning, tensors are essential because:

- Data Representation: They represent inputs, outputs, and weights of neural networks. For example, an image can be represented as a 3D tensor with dimensions corresponding to height, width, and color channels.
- Computational Efficiency: Operations on tensors can be efficiently performed using specialized hardware (like GPUs) and optimized libraries (like TensorFlow or PyTorch).

Operations on Tensors
Tensors support a variety of mathematical operations, including:
- Addition and Subtraction: Adding or subtracting tensors element-wise.
- Multiplication: Element-wise multiplication or matrix multiplication.
- Transformation: Reshaping, slicing, or concatenating tensors.

More about tensors...they aren't just arrays
- In mathematics, tensors generalize scalars, vectors, and matrices to higher dimensions and are used to describe more complex relationships between different kinds of quantities.
- Tensors have a well-defined structure that includes properties and operations beyond just indexing and slicing. For example, tensors are often associated with multilinear maps and transformations between vector spaces.

- Computational Graphs: Tensors are part of computational graphs, where each node represents a tensor operation. These graphs help in managing the sequence of operations and optimizing computations.
- Automatic Differentiation: Frameworks use tensors to compute gradients. The structure of tensors allows for efficient computation of gradients using techniques like backpropagation.
- any tensor operations are designed to leverage GPUs or TPUs for acceleration. These devices are optimized for parallel processing of tensor operations, making tasks like matrix multiplications very efficient.

Stochastic Gradient Descent (SGD) is a popular optimization algorithm used in machine learning and deep learning to train models. It's a variation of the gradient descent algorithm, designed to improve the efficiency and effectiveness of the training process. 


torch.nn is a module in the PyTorch library that provides tools for building and training neural networks. It contains various components that are essential for defining, training, and evaluating neural networks in PyTorch. 

Steps for a basic first pytorch task
pip install torch
pip install numpy
import torch
# Sample data: square footage and corresponding house prices
X = torch.tensor([[600.0], [800.0], [1000.0], [1200.0], [1400.0]])
y = torch.tensor([[300.0], [350.0], [400.0], [450.0], [500.0]])

import torch.nn as nn

#note: need to understand a bit about classes to understand this better
class LinearRegressionModel(nn.Module):
    def __init__(self):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(1, 1)  # One input, one output

    def forward(self, x):
        return self.linear(x)

model = LinearRegressionModel()
....
to be continued
