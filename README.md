A repository containing an example project for 
MNIST classification using [DeepPipe](https://github.com/neuro-ml/deep_pipe).

Folder simple_mnist contains example of resource manager usage based on modified pytorch MNIST example (https://github.com/pytorch/examples/blob/master/mnist/main.py).

You will need to install resource manager via

```
pip install resource_manager
```

To run the model execute command from simple_mnist folder:

```
python run.py do_experiment --config_path mnist_simple.config
```
