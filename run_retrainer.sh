read -p "Enter class directory name: " -e input
bazel-bin/tensorflow/examples/image_retraining/retrain --image_dir ~/$input