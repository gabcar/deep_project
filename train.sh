# Specify the location of the folder that contains the folders divide into classes as input
read -p "Enter class directory name: " -e input
bazel-bin/tensorflow/examples/image_retraining/retrain --image_dir ~/$input